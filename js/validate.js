function validate() {
	var usernameInput = $('#username-field').val();
	var passwordInput = $('#password-field').val();
	if((usernameInput.replace(/^(?=.{8,20}$)[a-zA-Z0-9._]+/i, '') === "") && passwordInput) {
		$('#input-error').css('visibility', 'hidden');
		return true;
	}
	else {
		$('#input-error').css('visibility', 'visible');
		return false;
	}
}
