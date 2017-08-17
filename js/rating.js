function singularOrPlural(input) {
	if(input > 1)
		return " stjärnor";
	else
		return " stjärna";
}

function updateRatings() {
	var token = Cookies.get('token');
	if((token === null) || (token === "null")) {
		token = false;
	}
	$.get({
		url: "getRatings.cgi",
		data: {
			recipeID: window.location.search.split("=")[1],
			token: token
		},
		dataType: "json",
		success: function(data) {
			var stars = $('.rating-icon');
			if(data.average) {
				var roundedAverage = Math.round(data.average);
				for(var i = 0; i < roundedAverage; i++) {
					stars.eq(i).attr("src", "/images/svg/icons/star2.svg");
				}
				for(var i = roundedAverage; i < stars.length; i++) {
					stars.eq(i).attr("src", "/images/svg/icons/star.svg");
				}
				$('#rating-average').html(data.entries + " användare gav receptet i genomsnitt " + Number(data.average.toFixed(2)) + singularOrPlural(data.average));
				if(data.user)
					$('#rating-user').html("Du gav receptet " + data.user + singularOrPlural(data.user));
			}
		}
	});
}

function rate(r) {
	$.post({
		url: "rate.cgi",
		data: {
			rating: r,
			recipeID: queryStringToJSON().id,
			token: Cookies.get('token')
		},
		dataType: "json",
		success: function() {
			updateRatings();
		}
	});
}

$(document).ready(function() {
	if(window.location.href.indexOf("/recipe.cgi?") !== -1) {
		updateRatings();
		$('.rating-icon').each(function(index, value) {
			$(this).click(function() {
				rate(index + 1);
			});
		})
	}
});
