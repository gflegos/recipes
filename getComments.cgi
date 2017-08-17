#!C:\Users\Gustaf\AppData\Local\Programs\Python\Python35-32\python.exe
# coding: utf-8
import cgi, mums, pymysql.cursors, json
from datetime import datetime

inputRecipeID = cgi.FieldStorage()['recipeID'].value
connection = mums.sqlConnect()
sql = "SELECT userid, post, posttime FROM comments WHERE contentid=%s ORDER BY posttime DESC;"
commentsResult = mums.sqlExecute(connection, sql, inputRecipeID)
jsonArray = []
for commentToPrint in commentsResult:
	usernameSQL = "SELECT username FROM users WHERE id=%s;"
	username = mums.sqlExecute(connection, usernameSQL, commentToPrint['userid'])[0]['username']
	jsonArray.append({'username': username, 'time': commentToPrint['posttime'].strftime('%Y-%m-%d %H:%M:%S'), 'text': commentToPrint['post']})
print("Content-type: application/json\n\n")
print(json.dumps(jsonArray))	
connection.close()
