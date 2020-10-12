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

	$('#signupSubmit').on('click', function (e) {
		e.preventDefault();
		var username = $('#username').val();
		var party = $('#party').val();
		var first = $('#first').val();
		var last = $('#last').val();
		var email = $('#email').val();
		var pwd = $('#password').val();
		var pwd_2 = $('#password_2').val();

		var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/i;

		if (email != "" && pwd != "") {
			if (pwd != pwd_2) {
				$('#msg').html('<span style="color: red;">Your second Password does not match with the first.</span>');
			}
			else if (!regex.test(email)) {
				$('#msg').html('<span style="color: red;">Invalid email address typed in</span>');
			} else {
				$.ajax({
					method: "POST",
					url: '/signup',
					contentType: 'application/json;charset=UTF-8',
					data: JSON.stringify({ 'username': username, 'first': first, 'last': last, 'email': email, 'party': party, 'password': pwd, 'password_2': pwd_2 }),
					dataType: "json",
					success: function (data) {
						localStorage.setItem('loggedin', 1);
						$('#user_profile').html(username);
						$('#sign').hide();
						$('#loginform').hide();
						$('#signupform').hide();
						$('#logoff').show();
						$('#msg').html('<span style="color: green;">Successfully created an account. You are logged in</span>');
						window.location.href = "/";
					},
					statusCode: {
						400: function () {
							$('#msg').html('<span style="color: red;">Bad request - email already in use</span>');
						}
					},
					error: function (err) {
						console.log(err);
					}
				});
			}
		} else {
			$('#msg').html('<span style="color: red;">Invalid username and password</span>');
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
				window.location.href = "/";
			},
			error: function (err) {
				console.log(err);
			}
		});
	});
});