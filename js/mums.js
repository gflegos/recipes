String.prototype.htmlEscape = function() {
	return this.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#039;');
}

function queryStringToJSON() {            
	var pairs = location.search.slice(1).split('&');
	var result = {};
	pairs.forEach(function(pair) {
		pair = pair.split('=');
		result[pair[0]] = decodeURIComponent(pair[1] || '');
	});
	return JSON.parse(JSON.stringify(result));
}

function toggleFooter(value) {
	if(value) {
		$('#footer').css('visibility', 'visible');
		$('#expand-icon').css('visibility', 'hidden');
	}
	else {
		$('#footer').css('visibility', 'hidden');
		$('#expand-icon').css('visibility', 'visible');
	}
	Cookies.set('footer', value);
}

function hoverIconEffect(el, value) {
	el.each(function() {
		var newPath = $(this).attr('src').toString();
		if(value)
			newPath = newPath.replace('.svg', '-hover.svg');
		else
			newPath = newPath.replace('-hover.svg', '.svg');
		$(this).attr('src', newPath);
	});
}

function getFooterCookieBool() {
	cookie = Cookies.get('footer');
	if(cookie === "false")
		return false;
	else
		return true;
}

function isLoggedIn() {
	var token = Cookies.get('token');
	var loggedIn;
	if(token !== null && token !== "null") {
		$.post({
			url: "update.cgi",
			data: {
				token: token
			},
			dataType: "json",
			async: false,
			success: function(data) {
				if(data.current) {
					loggedIn = true;
				}
				else {
					logout();
					loggedIn = false;
				}
			}
		});
	}
	else {
		loggedIn = false;
	}
	return loggedIn;
}

$(document).ready(function() {
	toggleFooter(getFooterCookieBool());
	links = $('.category-link, .recipe-link');
	$('#expand-icon').click(function() {toggleFooter(true);});;
	$('#collapse-icon').click(function() {toggleFooter(false);});
	$('.footer-icon').hover(
		function() {
			hoverIconEffect($(this), true);
		},
		function() {
			hoverIconEffect($(this), false);
		}
	);
	links.hover(
		function() {
			hoverIconEffect($(this).find('.icon'), true);
		},
		function() {
			hoverIconEffect($(this).find('.icon'), false);
		}
	);
});
