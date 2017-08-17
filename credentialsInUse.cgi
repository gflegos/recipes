#!C:\Users\Gustaf\AppData\Local\Programs\Python\Python35-32\python.exe
# coding: utf-8
import cgi, mums, pymysql.cursors, json

def main():
	data = cgi.FieldStorage()
	username = data['username'].value
	emailAddress = data['emailAddress'].value
	jsonData = {
		'usernameRegisteredPass': True,
		'emailRegisteredPass': True
	}
	connection = mums.sqlConnect()
	sql = """
		SELECT * FROM users
		WHERE username=%s
		LIMIT 1;
	"""
	args = username
	if len(mums.sqlExecute(connection, sql, args)) > 0:
		jsonData['usernameRegisteredPass'] = False
	sql = """
		SELECT * FROM users
		WHERE emailaddress=%s
		LIMIT 1;
	"""
	args = emailAddress
	if len(mums.sqlExecute(connection, sql, args)) > 0:
		jsonData['emailRegisteredPass'] = False
	connection.close()
	print("Content-type: application/json\n\n")
	print(json.dumps(jsonData))

main()