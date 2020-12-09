$(document).ready(function () {
	var isLoggedIn = localStorage.getItem('loggedin');
    
    if (isLoggedIn == 1) {
        $('#sign').hide();
        $('#areaButton').show();
		$('#loginform').hide();
		$('#signupform').hide();
		$('#logoff').show();
	} else {
        $('#sign').show();
        $('#areaButton').hide();
		$('#logoff').hide();
	}
    
	$('#areaSubmit').on('click', function (e) {
        e.preventDefault();
       
        var area = $('#areaID').val();
        var description = $('#descriptionID').val();
        $.ajax({
            method: "POST",
            url: '/addarea',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({'area': area, 'description': description}),
            dataType: "json",
            success: function (data) {
                $('#msg').html('<span style="color: green;">Successfully added area!</span>');
            },
            statusCode: {
                400: function () {
                    $('#msg').html('<span style="color: red;">Area already exists!</span>');
                }
            },
            error: function (err) {
                console.log(err);
            }
        });
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