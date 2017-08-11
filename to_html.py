


def photo_queue(recent_photos):
	html =''

	for i, p in enumerate(recent_photos):
		html += f'<img src = "{p}" class = "photo_queue" id = "recentphotos-{i}">'

	return html




def current_image(image_url):
	html =''
	if image_url:
		html += f'<img class = "current_picture" src = "{image_url}">'
		

	html += '''
	<form name = "select_current_image" action = "/choose_new" id = "new_picture" method = "post">
		<input type = "submit" value = "Select engagement image.">
	</form>'''


	return html