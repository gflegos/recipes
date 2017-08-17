function formListToJSON(el) {
	var json = [];
	el.children().each(function() {
		
	});
}
function modifySubform(el) {
	var elItem = el.parent();
	var elList = elItem.parent();
	var maxItems = 256;
	if(el.hasClass('subform-add-icon active')) {
		var newPath = "/images/svg/icons/plus1.svg";
		var itemPath = "/images/svg/icons/error1.svg";
		var itemClass = "subform-delete-icon active";
		if(elItem.index() === 0) {
			itemPath = itemPath.replace('.svg', '-passive.svg');
			itemClass = itemClass.replace(' active', '');
		}
		var elNew = elList.children('li').last().clone();
		elNew.children('img').attr({
			'src': newPath,
			'class': 'subform-add-icon active'
		});
		elItem.children('img').attr({
			'src': itemPath,
			'class': itemClass
		});
		elNew.children('input').removeClass('active');
		elItem.children('input').addClass('active');
		elNew.appendTo(elList).find('input').val('');
		activateInputs(elNew.find('input'), false);
		activateInputs(elItem.find('input'), true);
	}
	else if(el.hasClass('subform-delete-icon active'))
		el.parent().remove();
	var elLast = elList.children('li').last();
	if(elLast.index() > maxItems - 1) {
		elLast.css('display', 'none');
	}
	else {
		elLast.css('display', 'default');
	}
}

/*function submitRecipe() {
	token = Cookies.get('token');
	var ingredients = formListToJSON($('#ingredients-input-list'));
	var instructions = formListToJSON($('#instructions-input-list'));
	if(token != null && token != "null") {
		$('')
		$.post({
			url: "submitRecipe.cgi",
			data: {
				token: token,
				title: $('#title-input').val(),
				category: $('#category-input').val(),
				description: $('#description-input').val(),
				ingredients: ingredients,
				instructions: instructions
			},
			success: function(data) {
				
			}
		});
	}
	else
}*/

function activateInputs(el, value) {
	el.each(function() {$(this).prop('disabled', !value)});
}

$(document).ready(function() {
	$(document).on('click', '.subform-add-icon, .subform-delete-icon.active', function() {
		modifySubform($(this))
	});
	$('.subform-add-icon.active').each(function() {
		modifySubform($(this));
	});
});