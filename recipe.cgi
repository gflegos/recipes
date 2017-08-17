#!C:\Users\Gustaf\AppData\Local\Programs\Python\Python35-32\python.exe
# coding: utf-8
import pymysql.cursors, cgi, mums, json
def generateRecipeHTML(data):
	connection = mums.sqlConnect()
	sql = "SELECT title, content, category, userid FROM content WHERE id=%s;"
	args = data['id'].value
	result = mums.sqlExecute(connection, sql, args)[0]
	content = json.loads(result['content'])
	description = cgi.escape(content['description'])
	ingredients = content['ingredients']
	ingredientsHTML = ""
	for ingredient in ingredients:
		ingredientsHTML += "<li class=\"ingredient\">" + cgi.escape(ingredient['amount'] + " " + ingredient['ingredient']) + "</li>"
	instructions = content['instructions']
	instructionsHTML = ""
	for instruction in instructions:
		instructionsHTML += "<li class=\"instruction\">" + cgi.escape(instruction) + "</li>"
	instructions = content['instructions']
	title = cgi.escape(result['title'])
	category = result['category']
	sql = "SELECT username FROM users WHERE id=%s;"
	args = result['userid']
	username = mums.sqlExecute(connection, sql, args)[0]['username']
	connection.close()
	html = """
		<div id="recipe-container">
			<h2>{0} av {1}</h2>
			<div class="grid-container">
				<div id="description-container" class="grid-100 mobile-grid-100">
					<h3 class="input-label">Beskrivning</h3>
					<p class="recipe-text">{2}</p>
				</div>
			</div>
			<div class="grid-container">
				<div id="ingredients-container" class="grid-50 mobile-grid-100">
					<h3 class="input-label">Ingredienser</h3>
					<ul class="ingredients-list">{3}</ul>
				</div>
				<div id="instructions-container" class="grid-50 mobile-grid-100">
					<h3 class="input-label">Instruktioner</h3>
					<ol class="instructions-list">{4}</ol>
				</div>
			</div>
		</div>
		<div class="grid-container">
			<div id="rating-container" class="grid-100 mobile-grid-100">
				<h3 class="input-label">Betyg</h3>
				<div id="rating-stars">
					<img href="javascript:void()" class="rating-icon" id="rate-1" src="images/svg/icons/star.svg">
					<img href="javascript:void()" class="rating-icon" id="rate-2" src="images/svg/icons/star.svg">
					<img href="javascript:void()" class="rating-icon" id="rate-3" src="images/svg/icons/star.svg">
					<img href="javascript:void()" class="rating-icon" id="rate-4" src="images/svg/icons/star.svg">
					<img href="javascript:void()" class="rating-icon" id="rate-5" src="images/svg/icons/star.svg">
				</div>
				<div id="rating-stats">
					<p id="rating-average" class="feedback-text"></p>
					<p id="rating-user" class="feedback-text"></p>
				</div>
			</div>
		</div>
		<div class="grid-container">
			<div id="comment-container" class="grid-100 mobile-grid-100">
				<h3 class="input-label">Kommentarer</h3>
				<p id="no-comments-text" class="feedback-text">Inga kommentarer</p>
				<ul id="comments">
				</ul>
				<form id="post" name="comment" action="" method="post">
					<textarea name="comment" id="comment-input" class="recipe-input active" cols="50" rows="5" maxlength="256" placeholder="Kommentar"></textarea>
					<input type="submit" id="comment-button" class="recipe-input" value="Kommentera">
				</form>
			</div>
		</div>
	"""
	html = html.format(title, username, description, ingredientsHTML, instructionsHTML)
	return {'html': html, 'title': title, 'username': username}

def main():
	data = cgi.FieldStorage()
	mums.setEncoding()
	recipeHTML = generateRecipeHTML(data)
	staticHTML = mums.getStaticHTML()
	print(staticHTML['preTitle'] + recipeHTML['title'] + " av " + recipeHTML['username'] + " – Mums" + staticHTML['upper'] + recipeHTML['html'] + staticHTML['lower'])

main()
