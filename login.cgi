#!C:\Users\Gustaf\AppData\Local\Programs\Python\Python35-32\python.exe
# coding: utf-8
import pymysql.cursors, cgi, http.cookies, time, re, mums, os, json, jwt
from datetime import datetime, timedelta

def getID(connection, username, hashedpassword):
	idResult = mums.sqlExecute(connection, "SELECT id FROM users WHERE username=%s AND hashedpassword=%s AND active=true;", (username, hashedpassword))
	if idResult:
		return idResult[0]['id']
	else:
		return None
		
def generateToken(userID, username):
	token = jwt.encode({'exp': (datetime.utcnow() + timedelta(weeks = 1)).timestamp(), 'userid': userID, 'username': username}, mums.mumsHash('Klezmer1991'), algorithm = 'HS256')
	return token

def generateCookie(connection, userID):
	c = http.cookies.SimpleCookie()
	c['id'] = userID
	mums.sqlExecute(connection, "DELETE FROM tokens WHERE userid=%s;", userID)
	mums.sqlExecute(connection, "INSERT INTO tokens (userid) VALUES (%s);", userID)
	tokenResult = mums.sqlExecute(connection, "SELECT id FROM tokens WHERE userid=%s;", userID)
	usernameResult = mums.sqlExecute(connection, "SELECT username FROM users WHERE id=%s", userID)
	try:
		c['token'] = tokenResult[0]['id']
	except TypeError:
		c['token'] = None
	try:
		referer = os.getenv('HTTP_REFERER')
	except KeyError:
		referer = None
	if referer and (referer != "/login.html"):
		c['referer'] = referer
	return c
	
def printCookie(connection, cookie):
	if cookie['id'].value != "None":
		referer = mums.getCookieValue('referer')
		if referer == None:
			referer = "/"
		print(cookie)
		print("Location: " + referer)
	else:
		print("Location: http://localhost:122/register.html")
	print("Content-type: text/html\n\n<head><link href=\"css/mums.css\" type=\"text/css\" rel=\"stylesheet\"/><title>ffewf</title><script src=\"//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js\"></script></head><html><body><p>" + cookie['id'].value + " fdfd</p></body></html>")

def main():
	form = cgi.FieldStorage()
	username = form["username"].value.lower()
	password = form["password"].value
	connection = mums.sqlConnect()
	userID = getID(connection, username, mums.mumsHash(password))
	if userID:
		token = generateToken(userID, username)
	else:
		token = None
	print("Content-type: text\n")
	print(token)
	connection.close()

main()
