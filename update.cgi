#!C:\Users\Gustaf\AppData\Local\Programs\Python\Python35-32\python.exe
# coding: utf-8
import cgi, jwt, mums, json, time
from datetime import datetime

def main():
	token = cgi.FieldStorage()["token"].value
	try:
		data = jwt.decode(token.encode(), mums.mumsHash('Klezmer1991'))
	except InvalidTokenError:
		current = False
		username = None
		userId = None
	else:
		current = True
		username = data['username']
		userId = data['userid']
	finally:
		jsonData = {'current': current, 'username': username, 'userID': userId}
		print("Content-type: application/json\n\n")
		print(json.dumps(jsonData))

main()
