$(document).ready(function () {
	var isLoggedIn = localStorage.getItem('loggedin');

	if (isLoggedIn == 1) {
		var post_id = $('#postID').text();
		var email = localStorage.getItem('email');
		$.ajax({
			method: "POST",
			url: '/checkVoteStatus',
			contentType: 'application/json;charset=UTF-8',
			data: JSON.stringify({ 'email': email, 'post_id': post_id}),
			dataType: "json",
			success: function (data) {
				localStorage.setItem("post_id:"+post_id+"email:"+email, data.voteStatus);
				localStorage.setItem("post_id:"+post_id+"email:"+email + "star", data.bookmarkStatus);
				var voteStatus = localStorage.getItem("post_id:"+post_id+"email:"+email);
				var bookmarkStatus = localStorage.getItem("post_id:"+post_id+"email:"+email + "star");
				if (voteStatus == 1){
					document.getElementById("upvote").classList.add("upvote-on"); 
					document.getElementById("downvote").classList.remove("downvote-on");
				}
				else if (voteStatus == 2){
					document.getElementById("downvote").classList.add("downvote-on"); 
					document.getElementById("upvote").classList.remove("upvote-on");
				}
				if (bookmarkStatus == 1){
					document.getElementById("star").classList.add("star-on");
				}
				else if (bookmarkStatus == 0){
					document.getElementById("star").classList.remove("star-on");
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
	
	$('#upvote').on('click', function (e) {
		e.preventDefault();
		var post_id = $('#postID').text();
		if (isLoggedIn == 1) {
			var email = localStorage.getItem('email');
			$.ajax({
				method: "POST",
				url: '/upvote',
				contentType: 'application/json;charset=UTF-8',
				data: JSON.stringify({ 'email': email, 'post_id': post_id}),
				dataType: "json",
				success: function (data) {
					document.getElementById("upvote").classList.add("upvote-on"); 
					document.getElementById("downvote").classList.remove("downvote-on");
					var voteStatus = localStorage.getItem("post_id:"+post_id+"email:"+email);
					if (voteStatus == 2){
						var count = document.getElementById('count')
						var number = Number(count.innerHTML);
						number = number + 2
						count.innerHTML = number;	
					}
					else if (voteStatus == 0){
						var count = document.getElementById('count')
						var number = Number(count.innerHTML);
						number = number + 1
						count.innerHTML = number;
					}
					else if (voteStatus === null) {
						var count = document.getElementById('count')
						var number = Number(count.innerHTML);
						number = number + 1
						count.innerHTML = number;
					}
					localStorage.setItem("post_id:"+post_id+"email:"+email, 1);
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
	});
	
	$('#downvote').on('click', function (e) {
		e.preventDefault();
		var post_id = $('#postID').text();
		if (isLoggedIn == 1) {
			var email = localStorage.getItem('email');
			$.ajax({
				method: "POST",
				url: '/downvote',
				contentType: 'application/json;charset=UTF-8',
				data: JSON.stringify({ 'email': email, 'post_id': post_id}),
				success: function (data) {
					document.getElementById("downvote").classList.add("downvote-on"); 
					document.getElementById("upvote").classList.remove("upvote-on");
					var voteStatus = localStorage.getItem("post_id:"+post_id+"email:"+email);
					if (voteStatus == 1){
						var count = document.getElementById('count')
						var number = Number(count.innerHTML);
						number = number - 2
						count.innerHTML = number;	
					}
					else if (voteStatus === 0) {
						var count = document.getElementById('count')
						var number = Number(count.innerHTML);
						number = number - 1
						count.innerHTML = number;
					}
					else if (voteStatus === null) {
						var count = document.getElementById('count')
						var number = Number(count.innerHTML);
						number = number - 1
						count.innerHTML = number;
					}
					localStorage.setItem("post_id:"+post_id+"email:"+email, 2);
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
	});
	
	$('#star').on('click', function (e) {
		e.preventDefault();
		var post_id = $('#postID').text();
		if (isLoggedIn == 1) {
			var email = localStorage.getItem('email');
			$.ajax({
				method: "POST",
				url: '/star',
				contentType: 'application/json;charset=UTF-8',
				data: JSON.stringify({ 'email': email, 'post_id': post_id}),
				success: function (data) {
					var bookmarkStatus = localStorage.getItem("post_id:"+post_id+"email:"+email + "star");
					if(bookmarkStatus==0){
						document.getElementById("star").classList.add("star-on"); 
						localStorage.setItem("post_id:"+post_id+"email:"+email + "star", 1);
					}
					else if(bookmarkStatus==1){
						document.getElementById("star").classList.remove("star-on");
						localStorage.setItem("post_id:"+post_id+"email:"+email + "star", 0);
					}
					else{
						document.getElementById("star").classList.add("star-on");
						localStorage.setItem("post_id:"+post_id+"email:"+email + "star", 1);
					}
				},
				error: function (err) {
					console.log(err);
				}
			});
		} else {
		window.alert("Please login in order to be able to bookmark posts.")
		}
	});
	
});