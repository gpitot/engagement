<html>
<head>
<title>Engagement</title>
<link rel="stylesheet" type="text/css" href="static/engage.css">
<script src="static/jquery-3.2.1.js" type="text/javascript"></script>

<script>
	$(function() {
		var recent_photos_urls = {{!recent_photos_urls}};
		var recent_photos = {{!recent_photos}}

		var url;
		var image_url;
		
		$('.select_photo').click(function()
		{
			url = recent_photos_urls[Number($(this).attr('id').split('-')[1])];
			image_url = recent_photos[Number($(this).attr('id').split('-')[1])];
			
			$('input[name=image_url]').val(url+'?SPLIT?'+image_url);
			
			$(this).toggleClass('image_selected');

			

		});
		
		

	});


</script>



</head>
<body>
<div class = "stage">
	

	{{!images_html}}

	<form method = "post" name = "upload_image" action = "/upload" class = "upload_class">
		<input type = "hidden" name = "image_url" value = "None">
		<input type = "submit" value = "Upload">

	</form>
</div>
<div class = "right_side">
	<div class = "profile_username">
		{{!username}}
	</div>

	<img class = "profile_picture" src = "{{!profile_picture}}">
	

	<form name = "logout" method = "post" action = "/logout">
		<input type = "submit" value = "logout">
	</form>
</div>

</body>
</html>