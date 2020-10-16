$(document).ready(function () {
	var isLoggedIn = localStorage.getItem('loggedin');

	//$( function() {
	//	$.ajax({ 
	//	method: "GET",
	//	url: '/retrieve_thread',
	//	contentType: 'application/json;charset=UTF-8',
	//	success: function(){
	//		}});
	//} );

	if (isLoggedIn == 1) {
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