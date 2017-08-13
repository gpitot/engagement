<html>
<head>
<title>Engagement</title>
<link rel="stylesheet" type="text/css" href="static/engage.css">
<script src="static/jquery-3.2.1.js" type="text/javascript"></script>

<script>
	$(function() {
		var code;
		var last_valid = '';
		$('.photo_queue').click(function()
		{
			//validate like/comment
			code = $(this).attr('id').split('-')[1];
			//ajax command to check if like
			
			//only one valid class at a time
			last_valid = add_valid_button(code, last_valid)
			
		})

		$('.photo_area').on('click', '.validate', function()
		{
			console.log("validate clicked");
			$.ajax({
	            data:{'photoID':code},
	            url: "/check_engagement",
	            type: "POST",
	            contentType: 'application/json',
	            success: function (data) {
	                console.log("success");
	                console.log(data);

	                if (data["outcome"] == "valid")
	                {
	                	$('#div-'+code).hide();
	                }
	                
	            }
        	});

		})
		

	});


	function add_valid_button(code, last_valid)
	{
		
		$('div#div-'+code+' > div.validate').show();


		
		$('div#div-'+last_valid+' > div.validate').hide();
		

		return code
		
	}


</script>



</head>
<body>
<div class = "stage">
	

	{{!photo_queue_html}}

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