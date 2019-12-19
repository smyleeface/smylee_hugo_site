$(document).ready(function() {
	$("#single_page img").not('.no_border').each(function(index) {
		$(this).wrap('<div class="img_border"></div>').after('<span class="img_cap">'+$(this).attr('title')+'</span>');
	});
	$("#single_page .img_border").after('<div class="clear-all"></div>');
});