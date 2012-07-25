$(document).ready(function(){
	var metodo = 'palavrachave';
	var busca = '';
	
	function pesquisar() {
		$('#load-box').fadeIn('slow');
		busca = $('#texto-busca').val();
		
		$.get('api/consulta/'+metodo+'/'+busca, {}, function(resposta){
			console.log(resposta);
			if(resposta) {
				$('#load-box').fadeOut('slow');
			}
		}, 'json');
	}
	
	
	$('#tipo-busca').change(function(){
		if($(this).val() == 0) {
			$('.exemplo-pesquisa').html('<strong>Exemplo:</strong>Suprimentos de informática');
			metodo = 'palavrachave';
		}
		else if ($(this).val() == 1) {
			$('.exemplo-pesquisa').html('<strong>Exemplo:</strong> 05.387.348/0001-05');
			metodo = 'cnpj'
		}
		else if ($(this).val() == 2) {
			$('.exemplo-pesquisa').html('<strong>Exemplo:</strong> ASSOC DE JOVENS IDEALIZADORES DO BRASIL');
			metodo = 'empresaVencedora';
		}
		else if ($(this).val() == 3) {
			$('.exemplo-pesquisa').html('<strong> Entre os anos de 2011 e 2012</strong>');
			metodo = 'data';
		}
	});
	
	$('.search-button').click(function(){
		if($('#texto-busca').val()) {
			pesquisar();
		}
		else {
			$('#texto-busca').focus();
		}
	});
});