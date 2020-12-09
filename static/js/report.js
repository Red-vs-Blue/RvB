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

	$('#reportSubmit').on('click', function (e) {
		e.preventDefault();

		var name = $('#reporterName').val();
        var email = $('#reporterEmail').val();
        var reason = $("#report_reason option:selected").val();
        var comment_id = $('#comment_id').text();
        var message = $('#subject').val();

        var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/i;
		if (email != "" && name != "" && message != "" && reason != "" && comment_id != "") {
			if (!regex.test(email)) {
				$('#msg').html('<span style="color: red;">Invalid email address typed in</span>');
			} else {
				$.ajax({
					method: "POST",
					url: '/report',
					contentType: 'application/json;charset=UTF-8',
					data: JSON.stringify({ 'name': name, 'email': email, 'reason': reason, 'comment_id': comment_id, 'message': message }),
					dataType: "json",
					success: function (data) {
                        $('#msg').html('<span style="color: green;">Successfully sent a report</span>');
					},
					statusCode: {
						400: function () {
							$('#msg').html('<span style="color: red;">Failed sending report"</span>');
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