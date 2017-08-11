<html>
<head>
<title>Engagement</title>
<link rel="stylesheet" type="text/css" href="static/engage.css">
<script src="static/jquery-3.2.1.js" type="text/javascript"></script>

<script>
	$(function() {
		

	}


</script>



</head>
<body>
<div class = "stage">
	{{!error}}
	<form name = "login" method = "post" action = "/login">
		<input type = "text" name = "username" placeholder = "@">
		<input type = "password" name = "password">
		<input type = "submit" value = "Login">
	</form>

	<form name = "create" method = "post" action = "/create">
		<input type = "text" name = "username" placeholder = "@">
		<input type = "password" name = "password1">
		<input type = "password" name = "password2">
		<a href = "{{!image_url}}" target="_blank">
		    	<img src = "{{!image}}">
		 </a>
		<input type = "submit" value = "Validate">
	</form>

</div>


</body>
</html>