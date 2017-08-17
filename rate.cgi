#!C:\Users\Gustaf\AppData\Local\Programs\Python\Python35-32\python.exe
# coding: utf-8
import cgi, mums, pymysql.cursors, jwt, json

def main():
	data = cgi.FieldStorage()
	rating = data['rating'].value
	recipeID = data['recipeID'].value
	token = jwt.decode(data['token'].value, mums.mumsHash('Klezmer1991'))
	userID = token['userid']
	if mums.tokenIsCurrent(token):
		connection = mums.sqlConnect()
		sql = """INSERT INTO ratings (userid, contentid, rating)
			VALUES (%s, %s, %s)
			ON DUPLICATE KEY UPDATE rating = %s;"""
		args = userID, recipeID, rating, rating
		mums.sqlExecute(connection, sql, args)
		connection.close()
		jsonData = {'success': True}
	else:
		jsonData = {'success': False}
	
	print("Content-type: application/json\n\n")
	print(json.dumps(jsonData))

main()