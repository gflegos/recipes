function browse(value) {
	var pageNumber = $('#page-number');
	newPage = parseInt(pageNumber.html()) + value;
	pageNumber.html(newPage);
	loadPage(newPage);
}

function loadPage(page) {
	var pageLength = 12;
	var iconForward = $('#forward-icon');
	var iconBack = $('#back-icon');
	var recipeLink = $('.recipe-link');
	iconForward.unbind('click');
	iconBack.unbind('click');
	recipeLink.css('display', 'none');
	recipeLink.slice((page - 1) * pageLength, page * pageLength).each(function() {
		$(this).css('display', 'block');
	});
	if(page === 1) {
		iconBack.attr('src', 'images/svg/icons/back-button.svg');
		iconBack.attr('class', 'page-nav-icon-passive');
	}
	else {
		iconBack.attr('src', 'images/svg/icons/back-button (1).svg');
		iconBack.attr('class', 'page-nav-icon');
		iconBack.click(function() {
			browse(-1);
		});
	}
	if(recipeLink.eq(page * pageLength + 1).length) {
		iconForward.attr('src', 'images/svg/icons/forward-button (1).svg');
		iconForward.attr('class', 'page-nav-icon');
		iconForward.click(function() {
			browse(1);
		});
	}
	else {
		iconForward.attr('src', 'images/svg/icons/forward-button.svg');
		iconForward.attr('class', 'page-nav-icon-passive');
	}
}

$(document).ready(function() {
	loadPage(1);
});
