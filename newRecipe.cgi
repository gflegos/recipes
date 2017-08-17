#!C:\Users\Gustaf\AppData\Local\Programs\Python\Python35-32\python.exe
# coding: utf-8
import cgi, mums, pymysql.cursors

def generateRecipeForm():
	form = """
		<div id="recipe-form-container">
			<h2>Nytt recept</h2>
			<form class="grid-container" id="recipe-form" name="recipe-form" method="post" action="" onsubmit="" >
				<div id="inner-form-container">
					<div id="title-input-container" class="grid-33 input-container">
						<h3 class="input-label">Titel</h3>
						<input type="text" name="recipe-title" id="recipe-title-input" class="recipe-input active" maxlength="32">
						<h3 class="input-label">Kategori</h3>
						<select id="category-input" class="recipe-input active">
							<option value="" disabled selected></option>
							<option value="0">Förrätt</option>
							<option value="1">Varmrätt</option>
							<option value="2">Dessert</option>
							<option value="3">Dryck</option>
						</select>
					</div>
					<div id="description-input-container" class="grid-66 input-container">
						<h3 class="input-label">Beskrivning</h3>
						<textarea name="recipe-description" id="description-input" class="recipe-input active" cols="50" rows="5" maxlength="256"></textarea>
					</div>
					<div id="ingredients-input-container" class="grid-50 input-container">
						<h3 class="input-label">Ingredienser</h3>
						<ul id="ingredients-input-list" class="input-list">
							<li class="input-list-entry ingredients-entry">
								<input class="value-input recipe-input active" type="text" placeholder="Mängd" disabled="true" name="value-1" maxlength="16">
								<input class="ingredient-input recipe-input active" type="text" placeholder="Ingrediens" disabled="true" name="ingredient-1" maxlength="32">
								<img class="subform-add-icon active" src="images/svg/icons/plus1.svg">
							</li>
						</ul>
						
					</div>
					<div id="instructions-input-container" class="grid-50 input-container">
						<h3 class="input-label">Instruktioner</h3>
						<ol id="instructions-input-list" class="input-list" type="1">
							<li class="input-list-entry instructions-entry">
								<input class="instruction-input recipe-input active" type="text" placeholder="Instruktion" name="instruction-1" maxlength="64">
								<img class="subform-add-icon active" src="images/svg/icons/plus1.svg">
							</li>
						</ol>
					</div>
				</div>
				<input type="submit" class="recipe-input" id="recipe-submit" value="Skicka">
				<div id="feedback-container">
					<div id="error-container">
						<h3 class="input-label">Fel</h3>
						<ul id="error-list">
							<li id="error-title" class="error-item">Receptet måste ha en titel.</li>
							<li id="error-category" class="error-item">Receptet måste ha en kategori.</li>
							<li id="error-description" class="error-item">Receptet måste ha en beskrivning.</li>
							<li id="error-login" class="error-item">Du måste logga in för att ladda upp ett recept.</li>
						</ul>
					</div>
					<div id="success-container">
						<h3>Skickat</h3>
						<p class="feedback-text">Ditt recept har sparats. Du skickas nu till din receptsida.</p>
					</div>
				</div>
			</form>
		</div>
	"""
	return form

def main():
	mums.setEncoding()
	formHTML = generateRecipeForm()
	staticHTML = mums.getStaticHTML()
	print(staticHTML['preTitle'] + "Nytt recept – Mums" + staticHTML['upper'] + formHTML + staticHTML['lower'])

main()
