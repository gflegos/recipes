# coding: utf-8
import pymysql.cursors, cgi, hashlib, uuid, http.cookies
import time, re, math, os, json, sys, codecs
from datetime import datetime

def mumsHash(input):
	config = json.loads(open("config.json").read())
	saltStripChars = config['saltStripChars']
	saltLength = config['saltLength']
	saltFill = config['saltFill']
	salt = hashlib.sha224(
		(input.lower().strip(saltStripChars).center(math.ceil(len(input)
		* saltLength), saltFill)).encode()).hexdigest()
	output = hashlib.sha256((input + salt).encode()).hexdigest()
	return output
	
def sqlExecute(connection, sql, args):
	result = None
	try:
		with connection.cursor() as cursor:
			cursor.execute(sql, args)
			connection.commit()
			result = cursor.fetchall()
	except:
		connection.rollback()
	finally:
		return result
	
def sqlConnect():
	config = json.loads(open("config.json").read())
	dbHost = config["dbHost"]
	dbUser = config["dbUser"]
	dbPassword = config["dbPassword"]
	connection = pymysql.connect(
		host = dbHost,
		user = dbUser,
		password = dbPassword,
		db = 'mums',
		charset = 'utf8mb4',
		cursorclass = pymysql.cursors.DictCursor)
	return connection

def validateInput(input):
	if re.sub(r'^(?=.{8,20}$)[a-zA-Z0-9._]+', "", input) == "":
		return true
	else:
		return false

def getCookieValue(name):
	cookie = http.cookies.SimpleCookie()
	cookie.load(os.environ.get('HTTP_COOKIE'))
	return cookie[name].value

def printJSON(token):
	print("Content-type: application/json\n")
	print(json.dumps({'token': token}))

def tokenIsCurrent(token):
	if datetime.utcfromtimestamp(token['exp']) > datetime.utcnow():
		return True
	else:
		return False

def setEncoding():
	sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

def getStaticHTML():
	preTitleHTML = open('static-content/pretitle.html', encoding = 'utf-8').read()
	upperHTML = open('static-content/upper.html', encoding = 'utf-8').read()
	lowerHTML = open('static-content/lower.html', encoding = 'utf-8').read()
	return {'preTitle': preTitleHTML, 'upper': upperHTML, 'lower': lowerHTML}

def getConfig():
	config = json.loads(open("config.json").read())
	return config