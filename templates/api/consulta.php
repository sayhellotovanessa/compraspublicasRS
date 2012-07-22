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
	
		switch($arrayUrl[2]) {
			case 'palavrachave':
				if($arrayUrl[3]) {
					$dadosRS = new jsonFinder($allJsons);
					
					$pesquisa = $dadosRS->search('descricaoObjeto', $arrayUrl[3]);
					if(count($pesquisa) > 0) {
						echo json_encode($pesquisa);
					}
					else {
						echo json_encode(array("resposta"=>"Dados não encontrados"));
					}
				}
				else {
					echo json_encode(array("erro"=>"Favor passar termos para pesquisa."));
				}
			break;

			case 'cnpj':
			break;
			
			case 'empresaVencedora':
			break;
			
			case 'licitacao':
			break;
			
			case 'data':
			break;
		}
	}
?>