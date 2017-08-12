

#html for photo queue
def photo_queue(photos):
	

	html =''
	
	for i, (code, url) in enumerate(photos):
		print(code)
		html += f'''
		<div id = "div-{code}" class = "photo_area">
		<a href = "https://www.instagram.com/p/{code}" target="_blank">
			<img src = "{url}" class = "photo_queue" id = "code-{code}">
		</a>
		</div>
		'''

	return html

#html to select photos
def select_photo(photos):
	html =''

	for i, p in enumerate(photos):
		html += f'<img src = "{p}" class = "select_photo" id = "select_photoID-{i}">'

	return html



#html to show current image
def current_image(image_url):
	html =''
	if image_url:
		html += f'<img class = "current_picture" src = "{image_url}">'
		

	html += '''
	<form name = "select_current_image" action = "/choose_new" id = "new_picture" method = "post">
			<input type = "submit" value = "Select engagement image.">
	</form>'''


	return html