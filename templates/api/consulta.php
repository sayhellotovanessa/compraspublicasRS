<?	
	if($_SERVER['REQUEST_METHOD'] == 'GET') {
		
		function jsonJoin($jsons) {
			foreach($jsons as $json) {
				$content = file_get_contents("dados/$json");
				$eggs = array('[',']');
				$content = str_replace($eggs , '', $content);
				$result .= "$content ,";
			}
			
			$result = substr($result, 0, -1);
 			return "[$result]";
		}
		
		$jsons = array();

		foreach(scandir('dados/') as $dir) {
				if($dir !== '.' && $dir !== '..' && $dir !== '.DS_Store') {
					array_push($jsons, $dir);
				}
		}
		
		$allJsons = jsonJoin($jsons);
		$dadosRS = new jsonFinder($allJsons);
		
		switch($arrayUrl[2]) {
			case 'palavrachave':
				if($arrayUrl[3]) {
					$pesquisa = $dadosRS->search('descricaoObjeto', $arrayUrl[3]);
					
					if(count($pesquisa) > 0) {
						echo json_encode(array('resposta'=>$pesquisa));
					}
					else {
						echo json_encode(array('resposta'=>'Dados não encontrados'));
					}
				}
				else {
					echo json_encode(array('erro'=>'Favor passar termos para pesquisa.'));
				}
			break;

			case 'cnpj':
				if($arrayUrl[3]) {
					$pesquisa = $dadosRS->search('cnpjVencedor', (int) $arrayUrl[3]);
					
					if(count($pesquisa) > 0) {
						echo json_encode(array('resposta'=>$pesquisa));
					}
					else {
						echo json_encode(array('resposta'=>'Dados não encontrados'));
					}
				}
				else {
					echo json_encode(array('erro'=>'Favor passar cnpj para pesquisa.'));
				}
			break;
			
			case 'empresaVencedora':
				if($arrayUrl[3]) {		
					$pesquisa = $dadosRS->search('razaoSocialVencedor', $arrayUrl[3]);
					
					if(count($pesquisa) > 0) {
						echo json_encode(array('resposta'=>$pesquisa));
					}
					else {
						echo json_encode(array('resposta'=>'Dados não encontrados'));
					}
				}
				else {
					echo json_encode(array('erro'=>'Favor passar dados para pesquisa.'));
				}
			break;
			
			case 'data':
				//Formato da data 20110517
				
					if($arrayUrl[3]) {		
						$pesquisa = $dadosRS->search('dataPublicacaoLegal', $arrayUrl[3]);

						if(count($pesquisa) > 0) {
							echo json_encode(array('resposta'=>$pesquisa));
						}
						else {
							echo json_encode(array('resposta'=>'Dados não encontrados'));
						}
					}
					else {
						echo json_encode(array('erro'=>'Favor passar data para pesquisa.'));
					}
				
			break;
		}
	}
?>