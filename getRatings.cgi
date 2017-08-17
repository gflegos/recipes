#!C:\Users\Gustaf\AppData\Local\Programs\Python\Python35-32\python.exe
# coding: utf-8
import cgi, mums, pymysql.cursors, json, jwt

def main():
	recipeID = cgi.FieldStorage()['recipeID'].value
	token = cgi.FieldStorage()['token'].value
	connection = mums.sqlConnect()
	sql = "SELECT AVG(rating), COUNT(*) FROM ratings WHERE contentid=%s;"
	args = recipeID
	ratingResults = mums.sqlExecute(connection, sql, args)
	try:
		average = float(ratingResults[0]['AVG(rating)'])
	except TypeError:
		average = 0
	entries = ratingResults[0]['COUNT(*)']
	userRating = None
	if token:
		token = jwt.decode(token, mums.mumsHash('Klezmer1991'))
		sql = "SELECT rating FROM ratings WHERE contentid=%s AND userid=%s;"
		args = recipeID, token['userid']
		userRatingResult = mums.sqlExecute(connection, sql, args)
		if len(userRatingResult) and mums.tokenIsCurrent(token):
			userRating = userRatingResult[0]['rating']
	jsonData = {'average': average, 'entries': entries, 'user': userRating}
	connection.close()
	print("Content-type: application/json\n\n")
	print(json.dumps(jsonData))

main()
