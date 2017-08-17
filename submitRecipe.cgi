#!C:\Users\Gustaf\AppData\Local\Programs\Python\Python35-32\python.exe
# coding: utf-8
import cgi, mums, pymysql.cursors, json
from dicttoxml import dicttoxml
from jsonschema import validate

def main():
	data = cgi.FieldStorage()
	success = True
	schema = json.loads(open('static-content/recipeschema.json', encoding = 'utf-8').read())
	content = data['content'].value
	validate(json.loads(content), schema)
	title = data['title'].value
	id = data['id'].value
	category = data['category'].value
	connection = mums.sqlConnect()
	sql = """
		INSERT INTO content(title, content, category, userid)
		VALUES(%s, %s, %s, %s);
	"""
	args = title, content, category, id
	mums.sqlExecute(connection, sql, args)
	connection.close()
	print("Content-type: application/json\n\n")
	print(json.dumps({'success': success}))

main()
