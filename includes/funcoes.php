<?
			// ID
			function getID($id) {
				if (function_exists('filter_var'))
					$id = filter_var($id, FILTER_VALIDATE_INT);
				$id = (int) $id;

				return $id;
			}

			//STRING
			function getSTR($egg) {
				$egg = stripslashes($egg);
				return $egg;
			}

			// FlOAT
			function getFloat($input) {
				if (is_float($input))
					return $input;
				else
					return false;
			}

			// Alfanumerico
			function getAlpha($input) {
				if (ctype_alnum($input))
					return $input;
				else
					return false;
			}

			//EMAIL
			function getEmail($email) {
				$email = htmlspecialchars($email);
				if (function_exists('filter_var'))
					$email = filter_var($email, FILTER_VALIDATE_EMAIL);

				$email = htmlspecialchars($email);
				$email = trim($email);
				if (ereg("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$", $email)) {
					return $email;
				} else {
					return false;
				}
			}

			function getCPF($cpf) {
				$orig_cpf = $cpf;
				// Verifiva se o numero digitado contem todos os digitos
			    $cpf = str_pad(ereg_replace('[^0-9]', '', $cpf), 11, '0', STR_PAD_LEFT);

				// Verifica se nenhuma das sequencias abaixo foi digitada, caso seja, retorna falso
			    if (strlen($cpf) != 11 || $cpf == '00000000000' || $cpf == '11111111111' || $cpf == '22222222222' || $cpf == '33333333333' || $cpf == '44444444444' || $cpf == '55555555555' || $cpf == '66666666666' || $cpf == '77777777777' || $cpf == '88888888888' || $cpf == '99999999999') {
					return false;
			    } else {   // Calcula os numeros para verificar se o CPF e verdadeiro
			        for ($t = 9; $t < 11; $t++) {
			            for ($d = 0, $c = 0; $c < $t; $c++) {
			                $d += $cpf{$c} * (($t + 1) - $c);
			            }

			            $d = ((10 * $d) % 11) % 10;

			            if ($cpf{$c} != $d) {
			                return false;
			            }
			        }
			        return $orig_cpf;
			    }
			}

			function getCNPJ($cnpj) {
				$orig_cnpj = $cnpj;
			    $cnpj = ereg_replace('[^0-9]', '', $cnpj);

				if (strlen($cnpj) <> 14)
					return false;

				$soma = 0;

				$soma += ($cnpj[0] * 5);
				$soma += ($cnpj[1] * 4);
				$soma += ($cnpj[2] * 3);
				$soma += ($cnpj[3] * 2);
				$soma += ($cnpj[4] * 9);
				$soma += ($cnpj[5] * 8);
				$soma += ($cnpj[6] * 7);
				$soma += ($cnpj[7] * 6);
				$soma += ($cnpj[8] * 5);
				$soma += ($cnpj[9] * 4);
				$soma += ($cnpj[10] * 3);
				$soma += ($cnpj[11] * 2);

				$d1 = $soma % 11;
				$d1 = $d1 < 2 ? 0 : 11 - $d1;

				$soma = 0;
				$soma += ($cnpj[0] * 6);
				$soma += ($cnpj[1] * 5);
				$soma += ($cnpj[2] * 4);
				$soma += ($cnpj[3] * 3);
				$soma += ($cnpj[4] * 2);
				$soma += ($cnpj[5] * 9);
				$soma += ($cnpj[6] * 8);
				$soma += ($cnpj[7] * 7);
				$soma += ($cnpj[8] * 6);
				$soma += ($cnpj[9] * 5);
				$soma += ($cnpj[10] * 4);
				$soma += ($cnpj[11] * 3);
				$soma += ($cnpj[12] * 2);


				$d2 = $soma % 11;
				$d2 = $d2 < 2 ? 0 : 11 - $d2;

				if ($cnpj[12] == $d1 && $cnpj[13] == $d2) {
					return $orig_cnpj;
				} else {
					return false;
				}
			}

			// ESCAPAR STRINGS
			function escape($str) {
				if (get_magic_quotes_gpc()) {
					$clean = mysql_real_escape_string(stripslashes($str));
				} else {
					$clean = mysql_real_escape_string($str);
				}
				return $clean;
			}

			############### VERIFICA SE REQUISICAO E FEITA POR BOTS ###############
			function is_bot() {
				/* This function will check whether the visitor is a search engine robot */
				$botlist = array("Teoma", "alexa", "froogle", "Gigabot", "inktomi",
				"looksmart", "URL_Spider_SQL", "Firefly", "NationalDirectory",
				"Ask Jeeves", "TECNOSEEK", "InfoSeek", "WebFindBot", "girafabot",
				"crawler", "www.galaxy.com", "Googlebot", "Scooter", "Slurp",
				"msnbot", "appie", "FAST", "WebBug", "Spade", "ZyBorg", "rabaz",
				"Baiduspider", "Feedfetcher-Google", "TechnoratiSnoop", "Rankivabot",
				"Mediapartners-Google", "Sogou web spider", "WebAlta Crawler","TweetmemeBot",
				"Butterfly","Twitturls","Me.dium","Twiceler");

				foreach($botlist as $bot) {
					if(strpos($_SERVER['HTTP_USER_AGENT'],$bot)!==false)
						return true; // Is a bot
				}
				return false; // Not a bot
			}

			//PARSER XML
			function get_tag($tag,$xml) {
				preg_match_all('/<'.$tag.'>(.*)<\/'.$tag.'>$/imU',$xml,$match);
				return $match[1];
			}


			############### VERIFICA CONEXAO SEGURA (HTTPS) ###############
			function verificaConexao($flag) {
				$flag = (empty($flag)) ? $_SERVER['HTTPS'] : $flag;

				if ($flag == 1 or $flag = 'on')
					$security = true;
				else
					$security = false;

				return $security;
			}

			############### VERIFICA SE O DOMINIO DO EMAIL E VALIDO ###############
			function verificaEmail($email) {
				list($user, $domain) = explode("@", $email);
					if (function_exists('checkdnsrr'))
						$result = checkdnsrr($domain, 'MX');
					else
						$result = TRUE;
					return($result);
			}

			############### EXIBICAO DE URL ###############
			function exibeUrl($url) {
				$url = trim($url);
				if (empty($url)) {
					$retorno = NULL;
				} else {
					if (substr($url, 0, 7) == 'http://') {
						$url = str_replace('http://', '', $url);
					} elseif (substr($url, 0, 8) == 'https://') {
						$url = str_replace('https://', '', $url);
					}
					if (substr($url, 0, 4) == 'www.') {
						$url = str_replace('www.', '', $url);
					}
					$retorno = 'http://www.'.$url;
				}

				return $retorno;
			}



			############### CONVERTE DIAS PARA SEMANAS ###############
			function diasSemanas($dias) {
				$dias = (int)$dias;
				if ($dias == 0)
					$retorno = 'Hoje';
				elseif ($dias < 0)
					$retorno = 'Finalizado';
				else {
					if ($dias % 7 == 0) {
						$nr_semana = ($dias / 7);
						$retorno = $nr_semana.' semana';
						$retorno .= ($nr_semana > 1) ? 's' : '';
					} else {
						$retorno = $dias.' dia';
						$retorno .= ($dias > 1) ? 's' : '';
					}
				}
				return $retorno;
			}

			function converteSegundos($total_segundos, $inicio = 'Y') {
				// @autor: Carlos H. Reche
				define('dias_por_mes', ((((365*3)+366)/4)/12) );

				$comecou = false;

				if ($inicio == 'Y') {
					$array['anos'] = floor( $total_segundos / (60*60*24* dias_por_mes *12) );
					$total_segundos = ($total_segundos % (60*60*24* dias_por_mes *12));
					$comecou = true;
				}
				if (($inicio == 'm') || ($comecou == true)) {
					$array['meses'] = floor( $total_segundos / (60*60*24* dias_por_mes ) );
					$total_segundos = ($total_segundos % (60*60*24* dias_por_mes ));
					$comecou = true;
				}
				if (($inicio == 'd') || ($comecou == true)) {
					$array['dias'] = floor( $total_segundos / (60*60*24) );
					$total_segundos = ($total_segundos % (60*60*24));
					$comecou = true;
				}
				if (($inicio == 'H') || ($comecou == true)) {
					$array['horas'] = floor( $total_segundos / (60*60) );
					$total_segundos = ($total_segundos % (60*60));
					$comecou = true;
				}
				if (($inicio == 'i') || ($comecou == true)) {
					$array['minutos'] = floor($total_segundos / 60);
					$total_segundos = ($total_segundos % 60);
					$comecou = true;
				}
				$array['segundos'] = $total_segundos;

				return $array;
			}


			############### CALCULA PORCENTAGEM ###############
			function porcentagem ($valor, $total, $precisao) {
				$resultado = ($valor / $total) * 100;

				return round($resultado, $precisao)."%";
			}

			############### PEGA EXTENSAO ###############
			function getExt($arquivo) {
				$path_parts = pathinfo($arquivo);
				$ext = strtolower($path_parts['extension']);

				return $ext;
			}

			############### DATA (YYYY-MM-DD para DD/MM/YYYY) ###############
			function dataBarra($data_c) {

				$data = date($data_c);
				$data_fim = explode("-", $data);

				return $data_fim[2]."/".$data_fim[1]."/".$data_fim[0];
			}

			function dataHoraBarra($data) {
				$date = new DateTime($data);
				$date = $date->format('d/m/Y H:i:s');
				return $date;
			}

			############### DATA (DD/MM/YYYY para YYYY-MM-DD) ###############
			function dataTraco($data) {
				$dia = substr($data, 0, 2);
				$mes = substr($data, 3, 2);
				$ano = substr($data, 6, 4);

				return ($ano."-".$mes."-".$dia);
			}

			############### HORA (HH:MM:SS para HH:MM) ###############
			function horaHM($hora) {
				$nova_hora = substr($hora, 0, 5);

				return $nova_hora;
			}

			############### DIA COMPLETO (Quinta-feira, 10 de Setembro de 2008 ###############
			function diaCompleto($semana = 1, $time) { //Ativar semana: 1
				$texto = "";
				if ($semana == 1)
					$texto .= ucwords(strftime('%A', $time)).', ';
				$texto .= date('j', $time).' de '.ucwords(strftime('%B', $time)).' de '.date('Y', $time);

				return $texto;
			}

			############### CALCULA IDADE (ENTRADA YYYY-MM-DD, DD/MM/YYYY, time()) ###############
			function calculaIdade ($dataNasc) {
				if (getID($dataNasc)) {
					$dia = date("d", $dataNasc);
					$mes = date("m", $dataNasc);
					$ano = date("Y", $dataNasc);
				} else {
					if (strpos($dataNasc, "/")) {
						$data = explode("/", $dataNasc);
						$dia = $data[0];
						$mes = $data[1];
						$ano = $data[2];
					} else {
						$data = explode("-", $dataNasc);
						$dia = $data[2];
						$mes = $data[1];
						$ano = $data[0];
					}
				}

				if (!checkdate($mes, $dia, $ano)) {
					return false;
				} else {
					$dia_atual = date("d");
					$mes_atual = date("m");
					$ano_atual = date("Y");
					$idade = $ano_atual - $ano;
					if ($mes > $mes_atual) {
						$idade--;
					}
					if ($mes == $mes_atual and $dia_atual < $dia) {
						$idade--;
					}
					return $idade;
				}
			} 

			############### PRECO 9.99,99 para 999.99 ###############
			function floatPreco($valor) {
				return str_replace(",", ".", str_replace(".", "", $valor));
			}

			############### PRECO 999.99 para 9.99,99 ###############
			function formataPreco($valor) {
				if (!empty($valor)) {
					$xValor = explode (".", $valor);
					$antesVirgula = $xValor[0];
					$depoisVirgula = $xValor[1];

					if (strlen($depoisVirgula) == 0) {
						$centavos = "00";
					} elseif (strlen($depoisVirgula) == 1) {
						$centavos = $depoisVirgula . "0";
					} else {
						$centavos = $depoisVirgula;
					}

					$tamanhoReais = strlen($antesVirgula);

					if ($tamanhoReais > 3) {
						for ($x=0;$x<$tamanhoReais;$x++) {
							$xStart = ($tamanhoReais-1) - $x;
							if ($x%3 == 0) {
								$xPonto = substr($antesVirgula, $xStart, 1) . ".";
							} else {
								$xPonto = substr($antesVirgula, $xStart, 1);
							}
							$reais = $xPonto . $reais;
						}
						$reais = substr($reais,0,-1);
					} else {
						$reais = $antesVirgula;
					}
					$valorFormatado = $reais . "," . $centavos;
					return $valorFormatado;
				} else {
					$valorFormatado = "0,00";
					return $valorFormatado;
				}
			}


			############### JAVASCRIPT ###############
			function alerta($mensagem) {
				$return = '<script type="text/javascript">alert("'.$mensagem.'");</script>';
				return $return;
			}

			function redirect($egg) {
				echo "<script>window.location='$egg';</script>";
			}

			function getYoutubeID($egg) {
				$regex = "/youtu(be.com|.b)(\/v\/|\/watch\?v=|e\/)(.{11})/";

				preg_match_all($regex , $egg, $matches);

				if(!empty($matches[3]))
				{
				    $codigos_unicos = array();
				    $quantidade_videos = count($matches[3]);
				    foreach($matches[3] as $code)
				    {
				        if(!in_array($code,$codigos_unicos))
				            array_push($codigos_unicos,$code);
				    }

				return $codigos_unicos;

				}else{
				   die('Nenhuma url valida encontrada');
				}
			}
?>