function updateComments() {
	$.get({
		url: "getComments.cgi",
		data: {
			recipeID: window.location.search.split("=")[1]
		},
		dataType: "json",
		success: function(data) {
			$('#comments').html("");
			if(data.length === 0) {
				$('#no-comments-text').css('display', 'inline');
			}
			else {
				$('#no-comments-text').css('display', 'none');
				for(i = data.length - 1; i >= 0; i--) {
					var html = "<li class=\"comment\"><p class=\"feedback-text\"><span class=\"comment-time\">" + data[i].time + "</span><span class=\"comment-username\">" + data[i].username + "</span></p><p class=\"recipe-text\">" + data[i].text.htmlEscape() + "</p></li>";
					$('#comments').append(html);
				}
			}
		}
	});
}

function postComment() {
	token = Cookies.get('token');
	if(isLoggedIn()) {
		$.post({
			url: "comment.cgi",
			data: {
				token: token,
				recipeID: window.location.search.split("=")[1],
				comment: $('#comment-input').val()
			},
			dataType: "json",
			success: function(data) {
				if(!data.success)
					logout();
				updateComments();
				$('#post input').prop('disabled', false);
				$('#comment-input').val("");
			}
		});
	}
}

$(document).ready(function() {
	if(window.location.href.indexOf("/recipe.cgi?") !== -1) {
		updateComments();
		if(isLoggedIn()) {
			$('#post').css('display', 'inline');
		}
		$('#post').submit(function(e) {
			e.preventDefault();
			$('#post input').prop('disabled', true);
			postComment();
		});
	}
});
