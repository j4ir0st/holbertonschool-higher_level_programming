$(document).ready(function(){
    $.ajax({
	url: "https://fourtonfish.com/hellosalut/?lang=fr",
	type: "GET",
	success: function(response) {
	    $("#hello").append(response.hello);
	}
    });
});
