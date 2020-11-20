function upvote_click(post_id) {
	var isLoggedIn = localStorage.getItem('loggedin');
	if (isLoggedIn == 1) {
		var email = localStorage.getItem('email');
		$.ajax({
			method: "POST",
			url: '/upvote',
			contentType: 'application/json;charset=UTF-8',
			data: JSON.stringify({ 'email': email, 'post_id': post_id }),
			dataType: "json",
			success: function (data) {
				document.getElementById("upvote_" + post_id).classList.add("upvote-on");
				document.getElementById("downvote_" + post_id).classList.remove("downvote-on");
				var voteStatus = localStorage.getItem("post_id:" + post_id + "email:" + email);
				var count = document.getElementById('count_' + post_id)
				var number = Number(count.innerHTML);
				if (voteStatus == 2) {
					number = number + 2
					count.innerHTML = number;
				}
				else if (voteStatus == 0 || voteStatus === null) {
					number = number + 1
					count.innerHTML = number;
				}

				localStorage.setItem("post_id:" + post_id + "email:" + email, 1);
			},
			statusCode: {
				400: function () {

				}
			},
			error: function (err) {
				console.log(err);
			}
		});
	} else {
		window.alert("Please login in order to be able to vote.")
	}
}

function downvote_click(post_id) {
	var isLoggedIn = localStorage.getItem('loggedin');
	if (isLoggedIn == 1) {
		var email = localStorage.getItem('email');
		$.ajax({
			method: "POST",
			url: '/downvote',
			contentType: 'application/json;charset=UTF-8',
			data: JSON.stringify({ 'email': email, 'post_id': post_id }),
			success: function (data) {
				document.getElementById("downvote_" + post_id).classList.add("downvote-on");
				document.getElementById("upvote_" + post_id).classList.remove("upvote-on");
				var voteStatus = localStorage.getItem("post_id:" + post_id + "email:" + email);
				if (voteStatus == 1) {
					count = document.getElementById('count_' + post_id)
					number = Number(count.innerHTML);
					number = number - 2
					count.innerHTML = number;
				}
				else if (voteStatus == 0 || voteStatus == null) {
					var count = document.getElementById('count_' + post_id)
					var number = Number(count.innerHTML);
					number = number - 1
					count.innerHTML = number;
				}
				localStorage.setItem("post_id:" + post_id + "email:" + email, 2);
			},
			statusCode: {
				400: function () {

				}
			},
			error: function (err) {
				console.log(err);
			}
		});
	} else {
		window.alert("Please login in order to be able to vote.")
	}
}

function star_click(post_id) {
	var isLoggedIn = localStorage.getItem('loggedin');
	if (isLoggedIn == 1) {
		var email = localStorage.getItem('email');
		$.ajax({
			method: "POST",
			url: '/star',
			contentType: 'application/json;charset=UTF-8',
			data: JSON.stringify({ 'email': email, 'post_id': post_id }),
			success: function (data) {
				var bookmarkStatus = localStorage.getItem("post_id:" + post_id + "email:" + email + "star");
				if (bookmarkStatus == 0 || bookmarkStatus == null) {
					document.getElementById("star_" + post_id).classList.add("star-on");
					localStorage.setItem("post_id:" + post_id + "email:" + email + "star", 1);
				}
				else if (bookmarkStatus == 1) {
					document.getElementById("star_" + post_id).classList.remove("star-on");
					localStorage.setItem("post_id:" + post_id + "email:" + email + "star", 0);
				}
			},
			error: function (err) {
				console.log(err);
			}
		});
	} else {
		window.alert("Please login in order to be able to vote.")
	}
}

$(document).ready(function () {
	var isLoggedIn = localStorage.getItem('loggedin');

	if (isLoggedIn == 1) {
		//var post_id = $('#postID').text();
		var email = localStorage.getItem('email');
		$.ajax({
			method: "POST",
			url: '/checkVoteStatus',
			contentType: 'application/json;charset=UTF-8',
			//data: JSON.stringify({ 'email': email, 'post_id': post_id }),
			data: JSON.stringify({ 'email': email }),
			success: function (data) {
				for (var voteRow in data) {
					var post_id = data[voteRow].post_id
					var voteStatus = data[voteRow].voteStatus
					var bookmarkStatus = data[voteRow].bookmarkStatus
					localStorage.setItem("post_id:" + post_id + "email:" + email, voteStatus);
					localStorage.setItem("post_id:" + post_id + "email:" + email + "star", bookmarkStatus);
					if (voteStatus == 1) {
						document.getElementById("upvote_" + post_id).classList.add("upvote-on");
						document.getElementById("downvote_" + post_id).classList.remove("downvote-on");
					}
					else if (voteStatus == 2) {
						document.getElementById("downvote_" + post_id).classList.add("downvote-on");
						document.getElementById("upvote_" + post_id).classList.remove("upvote-on");
					}
					if (bookmarkStatus == 1) {
						document.getElementById("star_" + post_id).classList.add("star-on");
					}
					else if (bookmarkStatus == 0) {
						document.getElementById("star_" + post_id).classList.remove("star-on");
					}
				}

			},
			error: function (err) {
				console.log(err);
			}
		});
		$('#sign').hide();
		$('#loginform').hide();
		$('#signupform').hide();
		$('#logoff').show();
	} else {
		$('#sign').show();
		$('#logoff').hide();
	}


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