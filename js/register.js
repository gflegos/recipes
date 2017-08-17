function registerValidate() {
	var username = $('#username-input').val();
	var emailAddress = $('#email-input').val();
	var userPassword = $('#password-input').val();
	var userPasswordMatch = $('#password-match-input').val();
	var success = true;
	var pass = {
		"usernameRegistered": true,
		"usernameInvalid": true,
		"emailRegistered": true,
		"emailInvalid": true,
		"passwordsDoNotMatch": true,
		"passwordInvalid": true,
		"incomplete": true
	};
	if(!username)
		pass.incomplete = false;
	else if(!(username.replace(/^(?=.{8,20}$)[a-zA-Z0-9._]+/i, '') === ""))
		pass.usernameInvalid = false;
	if(!emailAddress)
		pass.incomplete = false;
	else if(!(emailAddress.replace(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/, '') === ""))
		pass.emailInvalid = false;
	if(!userPassword)
		pass.incomplete = false;
	else if(userPassword.length < 8)
		pass.passwordInvalid = false;
	if(!userPasswordMatch)
		pass.incomplete = false;
	else if(userPassword != userPasswordMatch)
		pass.passwordsDoNotMatch = false;
	if(pass.incomplete) {
		$.post({
			url: "credentialsInUse.cgi",
			data: {
				emailAddress: emailAddress,
				username: username
			},
			dataType: "json",
			async: false,
			success: function(data) {
				pass.emailRegistered = data.emailRegisteredPass;
				pass.usernameRegistered = data.usernameRegisteredPass;
			}
		});
	}
	Object.keys(pass).forEach(function(key) {
		var selector = "#error-" + key.toLowerCase();
		if(pass[key])
			$(selector).css('display', 'none');
		else {
			$(selector).css('display', 'list-item');
			success = false;
		}
	});
	if(success)
		$('#error-container').css('display', 'none');
	else
		$('#error-container').css('display', 'inline-block');
	return success;
}

$(document).ready(function() {
	$('#account-form').submit(function(e) {
		e.preventDefault();
		if(registerValidate()) {
			$.post({
				url: "register.cgi",
				data: {
					username: $('#username-input').val(),
					password: $('#password-input').val(),
					emailAddress: $('#email-input').val()
				},
				dataType: "json",
				success: function(data) {
					if(data.success) {
						$('#account-form :input').attr('disabled', true);
						$('#error-container').css('display', 'none');
						$('#success-container').css('display', 'inline-block');
					}
				}
			});
		}
	});
});
