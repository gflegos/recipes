#!C:\Users\Gustaf\AppData\Local\Programs\Python\Python35-32\python.exe
# coding: utf-8
import pymysql.cursors, cgi, hashlib, uuid, time, re, mums, json, smtplib, random

def main():
	form = cgi.FieldStorage()
	username = form['username'].value.lower()
	password = mums.mumsHash(form['password'].value)
	emailAddress = form['emailAddress'].value
	code = mums.mumsHash(username + str(random.randint(0, 65535)))
	connection = mums.sqlConnect()
	sql = "INSERT INTO users (username, hashedpassword, emailaddress, active, activationcode) VALUES(%s, %s, %s, false, %s);"
	args = username, password, emailAddress, code
	mums.sqlExecute(connection, sql, args)
	connection.close()
	
	config = json.loads(open("config.json").read())
	subject = "Aktivera ditt Mums-konto"
	text = "<html><body><a href=\"{0}activate.cgi?code={1}\">Aktivera ditt Mums-konto.</a></body></html>".format(config['url'], code)
	message = "From: Mums <{0}>\nTo: {1}\nSubject: {2}\nContent-Type: text/html; charset=utf-8\nContent-Transfer-Encoding: 7bit\n\n{3}".format(config['emailAddress'], emailAddress, subject, text)
	emailServer = smtplib.SMTP(config['emailServer'], config['emailServerPort'])
	emailServer.ehlo()
	emailServer.starttls()
	emailServer.login(config['emailUsername'], config['emailPassword'])
	emailServer.sendmail(config['emailAddress'], emailAddress, message)
	emailServer.close()
	print("Content-type: application/json\n\n")
	print(json.dumps({'success': True}))

main()
