function loadRecipes() {
	$.get({
		url: "getUserRecipes.cgi",
		data: {
			userID: window.location.search.split("=")[1]
		},
		dataType: "json",
		success: function() {
			
		}
	});
}

$(document).ready(function() {
	
});