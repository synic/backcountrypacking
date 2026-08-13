$(function() {
	$.each(["#si1", "#si2", "#si3"], function(index, value) {
		// preload
		var url = $(value + '_url').val();
		$.preLoadImages(url);

		$(value).mouseenter(function() {
			$('#hoverimage_img').attr({"src": url});
		});

		$(value).mousemove(function(e) {
			$('#hoverimage').css(
				{
					"left": e.pageX + 10, 
					"top": (e.pageY - $('#hoverimage').height()) - 60 
				}).show();
		});

		$(value).mouseleave(function() {
			$('#hoverimage').hide();
		});
	});
});

