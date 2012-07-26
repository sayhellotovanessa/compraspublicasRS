$(document).ready(function(){
	var metodo = 'palavraChave';
	var busca = '';
	
	function CNPJtoInt(egg) {
		egg = egg.replace('.','');
		egg = egg.replace('.',''); 
		egg = egg.replace('/','');
		egg = egg.replace('-','');
		
		return egg;
	}
	
	function DatetoInt(egg) {
		//17052011 > 20110517
		egg = egg.replace('/','');
		egg = egg.replace('/','');
		
		egg = egg.substring(4,8)+egg.substring(2,4)+egg.substring(0,2);
		
		return egg;
	}
	
	function pesquisar() {
		$('#erro-box').fadeOut('fast');
		$('#load-box').fadeIn('slow');
		
		busca = $('#texto-busca').val();
		
		if($('#tipo-busca').val() == 1) {
			busca = CNPJtoInt(busca);
		}
		else if ($('#tipo-busca').val() == 3) {
			busca = DatetoInt(busca);
			//20110517
		}
		
		$.get('api/consulta/'+metodo+'/'+busca, {}, function(resposta){
			if(resposta) {
				$('#load-box').fadeOut('fast');
				if(resposta.erro){
					alert('Erro no aplicativo, tente novamente.');
					location.href="";
					
					$('#erro-box').html("<span class=\"doh\">D'Oh!</span> <br/>"+resposta.erro);
					$('#erro-box').fadeIn('slow');
				}
				else {
					if(resposta.resposta == 'Dados não encontrados') {
						$('#erro-box').html("<span class=\"doh\">D'Oh!</span> <br/>Dados não encontrados...");
						$('#erro-box').fadeIn('slow');
					}
					else {
						var linhas = '';
						var tabela = '<table class="tabela"><tr><th>Descrição</th><th>Portal</th><th>Licitação</th><th>Empresa Vencedora</th><th>CNPJ</th><th>Valor</th><th>Quantidade</th><th>Data</th></tr>';
						
						for (var i=0; i < resposta.resposta.length; i++) {
							linhas += '<tr><td>'+resposta.resposta[i].descricaoObjeto+'</td><td>'+resposta.resposta[i].nomePortal+'</td><td>'+resposta.resposta[i].tipoLicitacao+'</td><td>'+resposta.resposta[i].razaoSocialVencedor+'</td><td>'+resposta.resposta[i].cnpjVencedor+'</td><td>'+resposta.resposta[i].valorVencedor+'</td><td>'+resposta.resposta[i].quantidadeItensLote+'</td><td>14/05/2011</td></tr>';
						};
						
						tabela = tabela + linhas +'</table>';
						
						$('#data-table').html(tabela);
						$('.datatablelink').click();
						$('body').css('overflow', 'auto');
					}
				}
			}
		}, 'json');
	}
	
	
	$('#tipo-busca').change(function(){
		if($(this).val() == 0) {
			$('.exemplo-pesquisa').html('<strong>Exemplo:</strong> Suprimentos de informática');
			metodo = 'palavraChave';
			$('#texto-busca').unmask('99.999.999/9999-99');
			$('#texto-busca').unmask('99/99/9999');
		}
		else if ($(this).val() == 1) {
			$('.exemplo-pesquisa').html('<strong>Exemplo:</strong> 05.387.348/0001-05');
			metodo = 'cnpj'
			$('#texto-busca').mask('99.999.999/9999-99', {placeholder:" "});
		}
		else if ($(this).val() == 2) {
			$('.exemplo-pesquisa').html('<strong>Exemplo:</strong> ASSOC DE JOVENS IDEALIZADORES DO BRASIL');
			metodo = 'empresaVencedora';
			$('#texto-busca').unmask('99.999.999/9999-99');
			$('#texto-busca').unmask('99/99/9999');
		}
		else if ($(this).val() == 3) {
			$('.exemplo-pesquisa').html('<strong> Entre os anos de 2011 e 2012</strong>');
			metodo = 'data';
			$('#texto-busca').mask('99/99/9999',{placeholder:" "});
		}
		
		$('#texto-busca').focus();
	});
	
	$('.search-button').click(function(){
		if($('#texto-busca').val()) {
			pesquisar();
		}
		else {
			$('#texto-busca').focus();
		}
	});
	
	$('#texto-busca').click(function() {
		$('#erro-box').fadeOut('fast');
	});
});