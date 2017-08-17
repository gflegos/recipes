#!C:\Users\Gustaf\AppData\Local\Programs\Python\Python35-32\python.exe
# coding: utf-8
import cgi, mums, pymysql.cursors

def generateAccountForm():
	form = """
		<div id="account-form-container">
			<h2>Nytt konto</h2>
			<form class="grid-container" id="account-form" name="account-form" action="" onsubmit="" method="post">
				<div class="grid-50 tablet-grid-50 mobile-grid-100 input-container">
					<h3 class="input-label">Användarnamn</h3>
					<input type="text" id="username-input" class="account-input active" name="username-input" onsubmit="">
				</div>
				<div class="grid-50 tablet-grid-50 mobile-grid-100 input-container">
					<h3 class="input-label">E-postadress</h3>
					<input type="text" id="email-input" class="account-input active" name="email-input">
				</div>
				<div class="grid-50 tablet-grid-50 mobile-grid-100 input-container">
					<h3 class="input-label">Lösenord</h3>
					<input type="password" id="password-input" class="account-input active" name="password-input">
				</div>
				<div class="grid-50 tablet-grid-50 mobile-grid-100 input-container">
					<h3 class="input-label">Upprepa lösenord</h3>
					<input type="password" id="password-match-input" class="account-input active" name="password-match-input">
				</div>
				<input type="submit" id="account-submit" class="account-input" name="account-submit" value="Registrera">
				<div id="feedback-container">
					<div id="error-container">
						<h3 class="input-label">Fel</h3>
						<ul id="error-list" class="register-feedback-text">
							<li id="error-usernameregistered" class="error-item">Användarnamnet är redan registrerat.</li>
							<li id="error-usernameinvalid" class="error-item">Användarnamnet måste bestå av 8-20 alfanumeriska tecken.</li>
							<li id="error-emailregistered" class="error-item">E-postadressen är redan registrerad.</li>
							<li id="error-emailinvalid" class="error-item">E-postadressen är ogiltig.</li>
							<li id="error-passwordsdonotmatch" class="error-item">Lösenorden matchar inte.</li>
							<li id="error-passwordinvalid" class="error-item">Lösenordet måste vara minst 8 tecken långt.</li>
							<li id="error-incomplete" class="error-item">Alla fält måste fyllas i.</li>
						</ul>
					</div>
					<div id="success-container">
						<h3 class="input-label">Registrerad</h3>
						<p class="feedback-text">Ditt konto har registrerats och en aktiveringslänk har skickats till den angivna e-postadressen. Klicka på aktiveringslänken för att aktivera ditt konto.</p>
					</div>
				</div>
			</form>
		</div>
	"""
	return form

def main():
	mums.setEncoding()
	formHTML = generateAccountForm()
	staticHTML = mums.getStaticHTML()
	print(staticHTML['preTitle'] + "Nytt konto – Mums" + staticHTML['upper'] + formHTML + staticHTML['lower'])

main()
