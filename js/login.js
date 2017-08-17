function loginValidate() {
	var loginMessage = $('#login-message');
	var usernameInput = $('#username-field').val();
	var passwordInput = $('#password-field').val();
	if((usernameInput.replace(/^(?=.{8,20}$)[a-zA-Z0-9._]+/i, '') === "")
		&& usernameInput && passwordInput) {
		loginMessage.html('Loggar in...');
		loginMessage.css('visibility', 'inherit');
		return true;
	}
	else {
		loginMessage.html('Ogiltiga uppgifter');
		loginMessage.css('visibility', 'inherit');
		return false;
	}
}

function updateUserStatus() {
	var token = Cookies.get('token');
	if(token !== null && token !== "null") {
		$.post({
			url: "update.cgi",
			data: {
				token: token
			},
			dataType: "json",
			success: function(data) {
				if(data.current) {
					$('#login-message').css('visibility', 'hidden');
					$('#input-error').css('visibility', 'hidden');
					$('#identity').html("Inloggad som " + data.username);
					$('#user-link').attr('href', "/showRecipes.cgi?user=" + data.userID);
					$('#authenticated').css('visibility', 'inherit');
					$('#not-authenticated').css('visibility', 'hidden');
					$('#not-authenticated-mobile').css('visibility', 'hidden');
				}
				else {
					logout();
				}
			}
		});
	}
	else {
		$('#authenticated').css('visibility', 'hidden');
		$('#not-authenticated').css('visibility', 'inherit');
		$('#not-authenticated-mobile').css('visibility', 'inherit');
	}
}

function logout() {
	Cookies.set('token', null);
	updateUserStatus();
}

$(document).ready(function() {
	$('#login').submit(function(e) {
		e.preventDefault();
		$.post({
			url: "login.cgi",
			data: $('#login').serialize(),
			dataType: "text",
			success: function(data) {
				token = data.split("'")[1];
				if(token !== null && token !== "null") {
					Cookies.set('token', token);
					updateUserStatus();
				}
				else {
					var loginMessage = $('#login-message');
					loginMessage.html('Ogiltiga uppgifter');
					loginMessage.css('visibility', 'inherit');
				}
			}
		});
	});
	updateUserStatus();
});
