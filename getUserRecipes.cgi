#!C:\Users\Gustaf\AppData\Local\Programs\Python\Python35-32\python.exe
# coding: utf-8
import cgi, mums, pymysql.cursors, json

def main():
	userID = cgi.FieldStorage()['userID'].value
	connection = mums.sqlConnect()
	sql = "SELECT id, title, category FROM content WHERE userid=%s ORDER BY id DESC;"
	args = userID
	recipeResults = mums.sqlExecute(connection, sql, args)
	jsonArray = []
	for recipe in recipeResults:
		jsonArray.append('id': recipe['id'], 'title': recipe['title'], 'category': recipe['category'])
	print("Content-type: application/json\n\n")
	print(json.dumps(jsonArray))
	connection.close()

main()
