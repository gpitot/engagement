<html>
<head>
<title>Engagement</title>
<link rel="stylesheet" type="text/css" href="static/engage.css">
<script src="static/jquery-3.2.1.js" type="text/javascript"></script>

<script>
	$(function() {
		
		
		

	});


</script>



</head>
<body>
<div class = "stage">
	

	

</div>

<div class = "right_side">
	<div class = "profile_username">
		{{!username}}
	</div>

	<img class = "profile_picture" src = "{{!profile_picture}}">
	

	<form name = "logout" method = "post" action = "/logout">
		<input type = "submit" value = "logout">
	</form>

	{{!current_image_html}}
</div>


	
</body>
</html>