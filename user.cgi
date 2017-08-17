#!C:\Users\Gustaf\AppData\Local\Programs\Python\Python35-32\python.exe
# coding: utf-8
import cgi, mums, pymysql.cursors, json

def main():
	data = cgi.FieldStorage()
	connection = mums.sqlConnect()
	sql = "SELECT username FROM users WHERE id=%s;"
	args = data['id'].value
	username = mums.sqlExecute(connection, sql, args)[0]['username']
	connection.close()
	print("Content-type: text/html\n\n")
	print("""<head>
			<title>Test</title>
			<link href="css/mums.css" type="text/css" rel="stylesheet"/>
			<link href="css/unsemantic-grid-responsive-tablet.css" type="text/css" rel="stylesheet"/>
			<link href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.0/themes/smoothness/jquery-ui.css" rel="stylesheet"/>
			<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1" http-equiv="Content-Type" content="text/html;charset=ISO-8859-1"/>
			<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
			<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.0/jquery-ui.min.js"></script>
			<script src="js/js-cookie.js"></script>
			<script src="js/login.js"></script>
			<script src="js/mums.js"></script>
			<script src="js/user.js"></script>
		</head>""")

	print("<body>")
	print("<h1>" + username + "</h1>")
	print("<p id=""></p>")
	print("""
		<div class="grid-container" id="recipes-container">
			
		</div>
		<div class="grid-container">
			<div class="grid-100 grid-parent tablet-grid-100 mobile-grid-100" id="footer">
				<div class="grid-33 tablet-grid-50 mobile-grid-50">
					<p>Genom att använda Mums godkänner du att sidan sparar <a href="http://ec.europa.eu/ipg/basics/legal/cookies/index_en.htm">cookies</a> på din enhet.</p>
					<p>Grafik formgiven av <a href="http://www.flaticon.com/authors/madebyoliver/">Madebyoliver på Flaticon</a>, använd under <a href="http://file000.flaticon.com/downloads/license/license.pdf">Flaticon Basic License</a>.</p>
				</div>
				<div class="grid-33 hide-on-tablet hide-on-mobile">
					<p>Alla recept på Mums har beräknats av en kraftfull superdator. Eftersom superdatorers matsmältningssystem skiljer sig från människors ges inga garantier för ätbarhet.</p>
				</div>
				<div class="grid-33 tablet-grid-50 mobile-grid-50 grid-parent">
					<div id="not-authenticated" class="hide-on-mobile hide-on-tablet">
						<form id="login" name="login" action="" class="footer-form" onsubmit="return validate()" method="post">
							<input type="text" name="username" id="username-field" class="footer-textbox" placeholder="Användarnamn" onsubmit="">
							<input type="password" name="password" id="password-field" class="footer-textbox" placeholder="Lösenord"><br>
							<input type="submit" class="footer-submit user-control-item" id="login-button" value="Logga in">
							<a class="user-control-item" href="register.html">Registrera konto</a>
							<span id="input-error">Ogiltig kontoinformation</span>
						</form>
					</div>
					<div id="not-authenticated-mobile" class="hide-on-desktop">
						<div class="user-controls">
							<a class="user-control-item" href="login.cgi">Logga in</a>
							<a class="user-control-item" href="register.html">Registrera konto</a>
						</div>
					</div>
					<div id="authenticated">
						<p class="user-controls">
							<span id="identity"></span><br>
							<a class="user-control-item">Nytt recept</a>
							<a class="user-control-item">Dina recept</a>
							<a class="user-control-item" href="javascript:void(0)" id="logout" onclick="logout();">Logga ut</a>
						</p>
					</div>
					<!--p id="copyright">Mums &copy; Gustav Danielsson 2016</p-->
				</div>
				<img href="javascript:void()" src="images/svg/icons/error.svg" id="collapse-icon">
				<img href="javascript:void()" src="images/svg/icons/plus.svg" id="expand-icon">
			</div>
		</div>
	</div>""")
	print("</body></html>")

main()
