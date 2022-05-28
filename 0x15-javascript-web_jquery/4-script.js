$(document).ready(function(){
    $("#toggle_header").click(function() {
	if (".green") {
	    $("header").toggleClass("green red");
	} else if (".red") {
	    $("header").toggleClass("red green");
	}
      });
});
