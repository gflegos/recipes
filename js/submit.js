function recipeValidate() {
	var id;
	var pass = {
		"title": true,
		"category": true,
		"description": true,
		"login": true
	};
	if(!($('#recipe-title-input').val())) {
		pass.title = false;
	}
	if(!($('#category-input').val())) {
		pass.category = false;
	}
	if(!($('#description-input').val())) {
		pass.description = false;
	}
	var token = Cookies.get('token');
	if(token != null && token != "null") {
		$.post({
			url: "update.cgi",
			data: {
				token: token
			},
			dataType: "json",
			async: false,
			success: function (data) {
				if(data.current) {
					id = data.userID;
				}
				else {
					pass.login = false;
					id = 0;
				}
			}
		});
	}
	else {
		pass.login = false;
		id = 0;
	}
	return {
		"pass": pass,
		"id": id
	};
}

$(document).ready(function() {
	$('#recipe-form').submit(function(e) {
		e.preventDefault();
		var ingredients = [];
		var instructions = [];
		var amount;
		var ingredient;
		var instruction;
		$('.ingredients-entry').each(function() {
			amount = $(this).children('.value-input').first().val();
			ingredient = $(this).children('.ingredient-input').first().val();
			if(ingredient) {
				ingredients.push({
					"amount": amount,
					"ingredient": ingredient
				});
			}
		});
		$('.instructions-entry').each(function() {
			instruction = $(this).children('.instruction-input').first().val();
			if(instruction) {
				instructions.push(instruction);
			}
		});
		var json = JSON.stringify({
			"description": $('#description-input').val(),
			"ingredients": ingredients,
			"instructions": instructions
		});
		var validateResult = recipeValidate();
		var id = validateResult.id;
		var pass = validateResult.pass;
		var success = true;
		Object.keys(pass).forEach(function(key) {
			var selector = "#error-" + key.toLowerCase();
			if(pass[key])
				$(selector).css('display', 'none');
			else {
				$(selector).css('display', 'list-item');
				success = false;
			}
		});
		if(success) {
			$('#error-container').css('display', 'none');
			$.post({
				url: "submitRecipe.cgi",
				data: {
					title: $('#recipe-title-input').val(),
					category: $('#category-input').val(),
					content: json,
					id: id
				},
				dataType: "json",
				success: function(data) {
					if(data.success) {
						$('#recipe-form input').prop('disabled', 'true');
						$('#success-container').css('display', 'inline-block');
						setTimeout(function() {
							window.location.href = "/showRecipes.cgi?user=" + id;
						}, 3000);
					}
				}
			});
		}
		else {
			$('#error-container').css('display', 'inline-block');
		}
	});
});
