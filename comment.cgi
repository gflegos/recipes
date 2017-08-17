#!C:\Users\Gustaf\AppData\Local\Programs\Python\Python35-32\python.exe
# coding: utf-8
import cgi, jwt, mums, pymysql.cursors, json
from datetime import datetime

def main():
	data = cgi.FieldStorage()
	comment = data['comment'].value
	token = jwt.decode(data['token'].value, mums.mumsHash('Klezmer1991'))
	userID = token['userid']
	recipeID = data['recipeID'].value
	connection = mums.sqlConnect()
	if mums.tokenIsCurrent(token):
		sql = "INSERT INTO comments (userid, contentid, post, posttime) VALUES (%s, %s, %s, %s)"
		args = userID, recipeID, comment, datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		mums.sqlExecute(connection, sql, args)
		jsonData = {'success': True}
	else:
		jsonData = {'success': False}
	connection.close()
	print("Content-type: application/json\n\n")
	print(json.dumps(jsonData))
	
main()
