$(document).ready(function(){
	$('#dateOfBirth').datepicker();
	$("#formRegister").click(function(e){
		if ($("#password_confirmation").val() != $("#password").val()){
			alert("Passwords don't watch");
			e.preventDefault();
		}	
	});	
});