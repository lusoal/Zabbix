$(document).ready(function(){
    $("#enviar").click(function(){
		$("#modal").hide();
	    var name =("Nome: "+ $("#nome").val());
		var email =("Email: "+ $("#email").val());
		var msg =("Mensagem: "+ $("#mensagem").val());

		$("#name").append(name + "<br /><br />" + email + "<br /><br />" + msg);
		$("#modal").show();
    });

	$("#salvar").click(function(){
		$("#modal").hide();
	});

	$("#fechar").click(function(){
		$("#modal").hide();
	});
});

$('.carousel').carousel({
  interval: 1000
})
