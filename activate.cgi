#!C:\Users\Gustaf\AppData\Local\Programs\Python\Python35-32\python.exe
# coding: utf-8
import pymysql.cursors, mums, cgi

def main():
	code = cgi.FieldStorage()['code'].value
	sql = """
		UPDATE users
		SET active=true
		WHERE activationcode=%s;
	"""
	connection = mums.sqlConnect()
	mums.sqlExecute(connection, sql, code)
	connection.close()
	mums.setEncoding()
	staticHTML = mums.getStaticHTML()
	print(staticHTML['preTitle'])
	print("Mums")
	print(staticHTML['upper'])
	print("<div class=\"grid-100\"><h2>Meddelande</h2><p class=\"feedback-text\">Ditt konto har aktiverats. Du kan nu logga in.</p></div>")
	print(staticHTML['lower'])

main()