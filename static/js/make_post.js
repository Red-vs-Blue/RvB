function make_post() {
	var isLoggedIn = localStorage.getItem('loggedin');
	if (isLoggedIn == 1) {
		window.location.href = '/make_post/page';
	} else {
		window.alert("Please login in order to make a post.")
	}
}
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

	$('#loginSubmit').on('click', function (e) {
		e.preventDefault();

		var email = $('#email').val();
		var pwd = $('#password').val();

		var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/i;

		if (email != "" && pwd != "") {
			if (!regex.test(email)) {
				$('#msg').html('<span style="color: red;">Invalid email address</span>');
			} else {
				$.ajax({
					method: "POST",
					url: '/login',
					contentType: 'application/json;charset=UTF-8',
					data: JSON.stringify({ 'email': email, 'password': pwd }),
					dataType: "json",
					success: function (data) {
						localStorage.setItem('loggedin', 1);
						localStorage.setItem('email', email);
						$('#user_profile').html(email);
						$('#sign').hide();
						$('#loginform').hide();
						$('#logoff').show();
						$('#msg').html('<span style="color: green;">You are logged in</span>');
						window.location.href = "/";
					},
					statusCode: {
						400: function () {
							$('#msg').html('<span style="color: red;">Bad request - invalid credentials</span>');
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

	$('#make_post_button').on('click', function (e) {
		e.preventDefault();

		var party_affiliation = $("#party_affiliation option:selected").val();
		var post_topic = $("#post_topic option:selected").val();
		var post_title = $('#post_title').val();
		var post_text = $('#post_text').val();

		if (party_affiliation != "" && post_topic != "" && post_title != "" && post_text != "") {
			$.ajax({
				method: "POST",
				url: '/make_post',
				contentType: 'application/json;charset=UTF-8',
				data: JSON.stringify({ 'party_affiliation': party_affiliation, 'post_topic': post_topic, 'post_title': post_title, 'post_text': post_text }),
				dataType: "json",
				success: function (data) {

					window.alert("Post made")
				},
				statusCode: {
					400: function () {
						$('#msg').html('<span style="color: red;">Bad request - invalid credentials</span>');
					}
				},
				error: function (err) {
					console.log(err);
				}
			});
		} else {
			$('#msg').html('<span style="color: red;">Please fill out the missing content</span>');
		}
	});

	$('#logout').on('click', function (e) {
		e.preventDefault();

		$.ajax({
			url: '/logout',
			dataType: "json",
			success: function (data) {
				localStorage.clear()
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