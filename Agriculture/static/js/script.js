
$(document).ready(function(){
	$(".btn").click(function(){

	if(confirm("are you sure you want to delete"))
	{
		var arr_id = [];
		
		$(":checkbox:checked").each(function(i){
			arr_id[i] = $(this).val();
		})
		if(arr_id.length == 0){
			alert("atleast check one");
		}else{
			for(var i = 0;i<arr_id.length;i++){
				
				$("."+arr_id[i]).css({"background":"red"});
								$("."+arr_id[i]).fadeOut("slow");

				
			}
		}
		
	}
else{
	return false;
}
	})
	
})