$(document).ready(function () {
	var isLoggedIn = localStorage.getItem('loggedin');

	if (isLoggedIn == 1) {
		$('#sign').hide();
		$('#loginform').hide();
		$('#signupform').hide();
		$('#logoff').show();
	} else {
		$('#sign').show();
		$('#logoff').hide();
	}

	$('#contactSubmit').on('click', function (e) {
		e.preventDefault();

		var name = $('#name').val();
		var email = $('#email').val();
		var message = $('#message').val();

		var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/i;

		if (email != "" && name != "" && message != "") {
			if (!regex.test(email)) {
				$('#msg').html('<span style="color: red;">Invalid email address typed in</span>');
			} else {
				$.ajax({
					method: "POST",
					url: '/contact',
					contentType: 'application/json;charset=UTF-8',
					data: JSON.stringify({ 'name': name, 'email': email, 'message': message }),
					dataType: "json",
					success: function (data) {
						$('#msg').html('<span style="color: green;">Successfully sent an email</span>');
					},
					statusCode: {
						400: function () {
							$('#msg').html('<span style="color: red;">Failed sending email"</span>');
						}
					},
					error: function (err) {
						console.log(err);
					}
				});
			}
		} else {
			$('#msg').html('<span style="color: red;">Box is empty</span>');
		}
	});

	$('#logout').on('click', function (e) {
		e.preventDefault();

		$.ajax({
			url: '/logout',
			dataType: "json",
			success: function (data) {
				localStorage.setItem('loggedin', 0);
				$('#sign').show();
				$('#logoff').hide();
				$('#msg').html('<span style="color: green;">You are logged off</span>');
			},
			error: function (err) {
				console.log(err);
			}
		});
	});
});