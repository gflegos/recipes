#!C:\Users\Gustaf\AppData\Local\Programs\Python\Python35-32\python.exe

import cgi, mums, pymysql.cursors

categories = {
	0: 'förrätt',
	1: 'varmrätt',
	2: 'dessert',
	3: 'dryck'
}

def getTitleArgs(data, connection):
	if 'user' in data:
		sql = "SELECT username FROM users WHERE id=%s;"
		args = data['user'].value
		username = mums.sqlExecute(connection, sql, args)[0]['username']
	else:
		username = None
	if 'cat' in data:
		category = categories[int(data['cat'].value)]
	else:
		category = None
	return {'username': username, 'category': category}

def getRecipes(data, connection):
	sql = """
		SELECT
			IFNULL(AVG(ratings.rating), 0) AS avgrating,
			users.username,
			content.*
		FROM content
		LEFT JOIN ratings
		ON ratings.contentid = content.id
		LEFT JOIN users
		ON users.id = content.userid
		WHERE {0}
		GROUP BY id
		ORDER BY
			avgrating DESC,
			content.id DESC;
	"""
	recipes = []
	pageTitle = ""
	if 'user' in data and 'cat' in data:
		whereClause = "content.userid=%s AND content.category=%s"
		args = data['user'].value, data['cat'].value
		pageTitle = "{0}er av {1} – Mums"
	elif 'user' in data:
		whereClause = "content.userid=%s"
		args = data['user'].value
		pageTitle = "Recept av {1} – Mums"
	elif 'cat' in data:
		whereClause = "content.category=%s"
		args = data['cat'].value
		pageTitle = "{0}er – Mums"
	else:
		whereClause = "1=1"
		args = None
		pageTitle = "Mums"
	sql = sql.format(whereClause)
	recipeResults = mums.sqlExecute(connection, sql, args)
	if recipeResults:
		for recipe in recipeResults:
			if recipe['avgrating']:
				rating = recipe['avgrating']
			else:
				rating = 0
			recipes.append({
				'id': recipe['id'],
				'title': recipe['title'],
				'userID': recipe['userid'],
				'username': recipe['username'],
				'category': recipe['category'],
				'rating': rating
			})
		pageTitle = pageTitle.format(categories[recipe['category']].title(), recipe['username'])
	return {'recipes': recipes, 'title': pageTitle}
	
def recipesToHTML(recipes):
	recipesHTML = "<div id=\"recipe-list-container\" class=\"grid-container grid-parent\">"
	for recipe in recipes:
		stars = "<div class=\"rating-passive\">"
		for i in range(1, 6):
			if i <= round(recipe['rating']):
				graphicPath = "/images/svg/icons/star2passive.svg"
			else:
				graphicPath = "/images/svg/icons/starpassive.svg"
			stars += "<img class=\"icon rating-icon-passive\" src=\"" + graphicPath + u"\"/>"
		stars += u"</div>"
		s = """
			<a href="/recipe.cgi?id={0}" class="grid-33 tablet-grid-33 mobile-grid-50 recipe-link" title="{1} av {2}">
				<span class="recipe-info">
					<p class="recipe-title">{1}</p>
					<p class="recipe-details">En {3} av {2}</p>
				</span>
				<span class="recipe-rating">{4}</span>
			</a>"""
		recipesHTML += s.format(recipe['id'], recipe['title'], recipe['username'], categories[recipe['category']], stars)
	recipesHTML += """
		</div>
		<div id="page-nav-container" class="grid-parent grid-30 prefix-35 suffix-35 mobile-grid-30 mobile-prefix-35 mobile-suffix-35 tablet-grid-30 tablet-prefix-35 tablet-suffix-35">
			<div class="grid-33 mobile-grid-33 tablet-grid-33">
				<img id="back-icon" class="icon page-nav-icon" src="images/svg/icons/back-button.svg">
			</div>
			<div id="page-number-container" class="grid-33 mobile-grid-33 tablet-grid-33">
				<p id="page-number">1</p>
			</div>
			<div class="grid-33 mobile-grid-33 tablet-grid-33">
				<img id="forward-icon" class="icon page-nav-icon" src="images/svg/icons/forward-button.svg">
			</div>
		</div>"""
	return recipesHTML

def main():
	mums.setEncoding()
	data = cgi.FieldStorage()
	connection = mums.sqlConnect()
	content = getRecipes(data, connection)
	if content['recipes']:
		recipes = content['recipes']
		title = content['title'].format(getTitleArgs(data, connection))
		recipesHTML = recipesToHTML(recipes)
	else:
		recipesHTML = ""
		title = "Mums"
	connection.close()
	staticHTML = mums.getStaticHTML()
	print(staticHTML['preTitle'], title, staticHTML['upper'], recipesHTML, staticHTML['lower'])

main()
