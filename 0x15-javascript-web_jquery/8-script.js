$(document).ready(function(){
    $.ajax({
	url: "https://swapi-api.hbtn.io/api/films/?format=json",
	type: "GET",
	success: function(response) {
	    for (i=0; i<=5; i++) {
		$("#list_movies").append("<li>" + response.results[i].title + "</li>");
	    }
	}
    });
});
