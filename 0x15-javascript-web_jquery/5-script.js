let count = 0;
$(document).ready(function(){
    $("#add_item").click(function() {
	count++;
	$(".my_list").append("<li>Item " + count + "</li>");
    });
});
