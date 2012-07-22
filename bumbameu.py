#!/usr/bin/python
import os,sys

def makedir(diretorio):
	print 'Criando diretorio %s' %(diretorio)
	
	if not os.path.isdir(diretorio):
		os.mkdir(diretorio)

def makefile(local,conteudo):
	try:
		f = open(local, 'w')
		f.write(conteudo)
		f.close
		print 'Criando arquivo %s' %(local)
		
	except:
		print 'Erro ao criar o arquivo %s' %(local)

def criarDiretorios():
	makedir('css')
	makedir('imgs')
	makedir('imgs/layout')
	makedir('includes')
	makedir('includes/classes')
	makedir('js')
	makedir('modelos')
	makedir('modelos/geradores')
	makedir('templates')
	makedir('includes/classes/conexao')
	
def criarArquivos(projetoNome):
	appTopPhp = """<? //seu codigo aqui ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title>%s</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title>Powered by Bumbameuboi</title>
		<link rel="stylesheet" type="text/css" href="css/estilo.css" />
	</head>
    <body>""" %(projetoNome)
	
	appBotPhp = """
	</body>
</html>"""
	
	funcoesPhp = """<!--powered by bumbameuboi-->
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
"""
	indexPhp = """<?
	session_start();
	
	$cfgXml = simplexml_load_file('config.xml');

	define('DB_HOST',$cfgXml->connection->host);
	define('DB_USER',$cfgXml->connection->user);
	define('DB_PASS',$cfgXml->connection->pass);
	define('DB_DATABASE',$cfgXml->connection->database);
	define('DIR_SITE', $cfgXml->domain."/");
	
	include('includes/funcoes.php');
	include('includes/classes/conexao/mysqlclass.php');
	include('rules.php');
	
	function __autoload($class_name) {
    	include 'includes/classes/'. $class_name . '.class.php';
	}
	
	$pagina = $arrayUrl[0];
	include("includes/app.top.php");
	
	if(file_exists("templates/$arrayUrl[0].php")) {
		include("templates/$arrayUrl[0].php");
	}
	else {
		include("templates/home.php");
	}
	
	include("includes/app.bot.php");
?>"""
	htaccess = """RewriteEngine On
RewriteCond %{SCRIPT_FILENAME} !-f
RewriteCond %{SCRIPT_FILENAME} !-d

RewriteRule ^(.+)\/?$ index.php?endereco=$1

<Files ~ "\.xml$">
Order allow,deny
Deny from all
</Files>
<Files ~ "\.py$">
Order allow,deny
Deny from all
</Files>
<Files ~ "\.inc$">
Order allow,deny
Deny from all
</Files>"""

	rulesPhp = """<?
	//Recebendo URLs Amigaveis

	if(isset($_GET["endereco"]))
		$endereco = $_GET["endereco"];
	else
		$endereco = false;

	$ultimo = strlen($endereco)-1;

	if($endereco[$ultimo] == "/")
		$endereco = substr($endereco, 0, $ultimo);

	$arrayUrl = explode("/", $endereco);
?>""" 
	
	estiloCss = """li { list-style:none;}
body {
	padding:0;
	margin:0 auto;
	text-align:center;
}
a, a:hover, a:visited {
	text-decoration:none;
}
img {
	border:none;
}"""
	modeloPy = """import sys
import MySQLdb
from tabela import *
from objeto import *
import xml.dom.minidom
from xml.dom.minidom import parse

def modelo(name,data):
	xml = open('config.xml', 'r')
	xmldoc = parse(xml)  
	xml.close()

	try:
		xmlHost = xmldoc.getElementsByTagName('host')
		mysqlHost = xmlHost[0].childNodes[0].nodeValue

		xmlUser = xmldoc.getElementsByTagName('user')
		mysqlUser = xmlUser[0].childNodes[0].nodeValue

		xmlPass = xmldoc.getElementsByTagName('pass')
		mysqlPass = xmlPass[0].childNodes[0].nodeValue

		xmlDataBase = xmldoc.getElementsByTagName('database')
		mysqlDB = xmlDataBase[0].childNodes[0].nodeValue

		xmlDataCharset = xmldoc.getElementsByTagName('charset')
		mysqlCharSet = xmlDataCharset[0].childNodes[0].nodeValue

		xmlDataEngine = xmldoc.getElementsByTagName('engine')
		mysqlEngine = xmlDataEngine[0].childNodes[0].nodeValue

	except:
		print 'XML de configuracao com dados imcompletos'
		sys.exit()

	try:
		db = MySQLdb.connect(host = mysqlHost, user = mysqlUser, passwd = mysqlPass, db=mysqlDB)
	except:
		print 'Nao foi possivel conectar ao banco de dados'
		sys.exit()

	con = db.cursor()
	newObject(name,data)
	newTable(con,name,data,mysqlCharSet,mysqlEngine)
"""
	
	objetoPy = """
import sys, os, errno
from xml.dom.minidom import parse
from urlparse import urlparse

def salvar(nome, conteudo):
	try:
	    os.makedirs('includes/classes')
	except OSError, e:
	    if e.errno != errno.EEXIST:
	        raise

	f = open( 'includes/classes/' + nome + '.class.php', 'w')
	f.write(conteudo)
	f.close
	print 'Criado o arquivo includes/classes/%s.class.php' %(nome)

def newObject(name, data):
	#xmldoc = parse('templates/class.txt')
	tmp = '<?\\n\\n //Desativado por seguranca, aprenda a fazer testes!\\n ini_set(\\'display_errors\\', 0);\\n\\n'
	tmp += 'class %s extends conexao {\\n\\n\\tvar $con;\\n\\n\\tfunction __construct() { \\n\\t\\t $this->con = new conexao;\\n\\t}\\n\\n' %(name)

	#INSERT
	tmp += '\\t function inserir('

	i = 0
	while i < len(data):

		if not i == len(data) - 1:
			if not data[i][0] == 'id' or data[i][0] == 'ID':
				tmp += '$' + data[i][0] + ', '
		else:
			if not data[i][0] == 'id' or data[i][0] == 'ID':
				tmp += '$' + data[i][0]	

		i = i + 1

	tmp += ') { \\n'
	tmp += "\\t\\t$dados = array("

	i = 0
	while i < len(data):

		if not i == len(data) - 1:
			if not data[i][0] == 'id' or data[i][0] == 'ID':
				tmp += '$' + data[i][0] + ', '
		else:
			if not data[i][0] == 'id' or data[i][0] == 'ID':
				tmp += '$' + data[i][0]	

		i = i + 1

	tmp += ');\\n' 
	tmp += "\\t\\t$colunas = array("

	i = 0
	while i < len(data):

		if not i == len(data) - 1:
			if not data[i][0] == 'id' or data[i][0] == 'ID':
				tmp += "'" + data[i][0] + "', "
		else:
			if not data[i][0] == 'id' or data[i][0] == 'ID':
				tmp += "'" + data[i][0]	 + "'"

		i = i + 1

	tmp += ');\\n'
	tmp +=	"\\t\\t$this->con->insert('%s', $dados, $colunas);\\n" %(name)

	tmp += '\\t}\\n\\n'

	#UPDATE
	tmp += '\\t function atualizar('

	i = 0
	while i < len(data):
		
		if not i == len(data) - 1:
			tmp += '$' + data[i][0] + ', '
		else:
			tmp += '$' + data[i][0]	

		i = i + 1

	tmp += ') { \\n'
	tmp += "\\t\\t$dados = array("

	i = 0
	while i < len(data):
		
		if not data[i][0] == 'id':
			if not i == len(data) - 1:
				tmp += '$' + data[i][0] + ', '
			else:
				tmp += '$' + data[i][0]	

		i = i + 1

	tmp += ');\\n' 
	tmp += "\\t\\t$colunas = array("

	i = 0
	while i < len(data):
		
		if not data[i][0] == 'id':
			if not i == len(data) - 1:
				tmp += "'" + data[i][0] + "', "
			else:
				tmp += "'" + data[i][0]	 + "'"

		i = i + 1

	tmp += ');\\n'
	tmp +=	"\\t\\t$this->con->update('%s', $dados, $colunas, $id);\\n" %(name)

	tmp += '\\t}\\n\\n'

	#DELETE
	tmp += "\\t function deletar($coluna,$criterio) { \\n\\t\\t$this->con->delete('%s', $coluna, $criterio);\\n" %(name)

	tmp += '\\t}\\n\\n'
	
	tmp += "\\tfunction todos() { \\n\\t\\t$todos = $this->con->sql_query('SELECT * FROM %s');\\n" %(name)
	
	tmp += "\\n\\t\\treturn $todos;\\n\\t}\\n"
	
	tmp += '}\\n\\n?>'	

	salvar(name,tmp)
"""
	
	tabelaPy = """import sys
import MySQLdb

def newTable(con,name,data,charSet,engine):
	dropTable = "DROP TABLE IF EXISTS %s" %(name)
	con.execute(dropTable)

	sql = "CREATE TABLE %s (" %(name)

	i = 0
	while i < len(data):

		if not i == len(data) - 1:
				if data[i][1] == 'id' or data[i][1] == 'ID':
					sql += 'id int(11) NOT NULL AUTO_INCREMENT,'
				else:
					sql += data[i][0] + ' ' + data[i][1] + ', '
		else:
				if data[i][1] == 'id' or data[i][1] == 'ID':
					sql += 'id int(11) NOT NULL AUTO_INCREMENT'
				sql += data[i][0] + ' ' + data[i][1]	

		i = i + 1
		
	sql += ", PRIMARY KEY (`id`)) ENGINE=%s AUTO_INCREMENT=5 DEFAULT CHARSET=%s;" %(engine, charSet)

	con.execute(sql)"""
	
	exampleModelPy = """from geradores.modelo import *

name = 'Exemplo'
data = (
	['id','id'],
	['nome','VARCHAR(255)'],
	['email','TEXT'],
	['data','DATE'],
	['endereco','DOUBLE'],
	['cep','VARCHAR(11)'],
	['telefone','VARCHAR(50)']
)

modelo(name,data)"""
 	
	configXml = """<?xml version="1.0" encoding="UTF-8"?>
<data>
	<domain>http://localhost</domain>
	<connection>
		<app>%s</app>
		<host>127.0.0.1</host>
		<user>root</user>
		<pass>mypassword</pass>
		<database>bumbameuboi</database>
		<!--Sinta-se a vontade para utilizar qualquer codificacao-->
		<charset>utf8</charset>
		<!--Sinta-se a vontade para utilizar qualquer motor-->
		<engine>MyISAM</engine>
	</connection>
</data>
""" %(projetoNome)
	
	mysqlClassPhp = """<?
			class conexao {

			    var $host = DB_HOST;
			    var $user = DB_USER;
			    var $senha = DB_PASS;
			    var $dbase = DB_DATABASE;

			    var $query;
			    var $link;
			    var $resultado;

			    function MySQL(){ 

			    }

			    function conecta(){
			        $this->link = mysql_connect($this->host,$this->user,$this->senha);

			        if(!$this->link)
			        {
			            echo "<br>Ocorreu um Erro na conexao MySQL:";
			            echo "<b>".mysql_error()."</b></br>";
			            die();
			        }

			        elseif(!mysql_select_db($this->dbase,$this->link))
			        {
			            echo "<br>Ocorreu um Erro em selecionar o Banco:";
			            echo "<b>".mysql_error()."</b></br>";
			            die();
			        }
			    }

			    function sql_query($query)
			    {
			        $this->conecta();
			        $this->query = $query;

			        if($this->resultado = mysql_query($this->query))
			        {
			            $this->desconecta();
			            return $this->resultado;
			        }
			        else
			        {
			            echo "<br>Ocorreu um erro ao executar a Query MySQL: <b>$query</b></br>";
			            echo "<br>Erro no MySQL: <b>".mysql_error()."</b></br>";
			            die();
			            $this->desconecta();
			        }        
			    }

			    function desconecta(){
			        return mysql_close($this->link);
			    }

					function insert($tabela,$dados,$colunas) {

						$str = "INSERT INTO $tabela(";

						for($i=0; $i < count($colunas); $i++){
								$str .= "$colunas[$i],";
						}

						$str = substr($str,0,-1);

						$str .= ") VALUES(";

						for($i=0; $i < count($dados); $i++){
								$str .= "'$dados[$i]',";
						}

						$str = substr($str,0,-1);
						$str .= ")";

						$this->sql_query($str);

					}

					function update($tabela,$dados,$colunas,$id) {
						$str = "UPDATE $tabela SET";

						for($i=0; $i < count($colunas); $i++){
							if($dados[$i] != 'NULL') {
								$str .= " $colunas[$i] = '$dados[$i]',";
							}
						}

						$str = substr($str,0,-1);

						$str .= " WHERE id = '$id'";

						echo $str;
						$this->sql_query($str);
					}

					function delete($tabela, $coluna, $criterio) {
						$str = "DELETE FROM $tabela WHERE $coluna = '$criterio'";

						$this->sql_query($str);
					}
			}
		?>
"""

	makefile('includes/app.top.php',appTopPhp)
	makefile('includes/app.bot.php',appBotPhp)
	makefile('includes/funcoes.php',funcoesPhp)
	makefile('includes/classes/conexao/mysqlclass.php',mysqlClassPhp)
	makefile('templates/home.php','<div style="font-family:Helvetica,Verdana; font-size:30px; color:#000; margin-top:20px;">Funcionou!<br>Bumba meu site!</div>');
	makefile('css/estilo.css',estiloCss)
	makefile('index.php',indexPhp)
	makefile('.htaccess',htaccess)
	makefile('rules.php',rulesPhp)
	makefile('modelos/geradores/__init__.py','')
	makefile('modelos/geradores/modelo.py',modeloPy)
	makefile('modelos/geradores/objeto.py',objetoPy)
	makefile('modelos/geradores/tabela.py',tabelaPy)
	makefile('modelos/example.model.py',exampleModelPy)
	makefile('config.xml',configXml)

def criarAplicativo(appNome):
	
	modeloPy = """from geradores.modelo import *

name = '%s'
data = (
	['id','id'],
)

modelo(name,data)	
""" %(appNome)
	
	templatePhp = """<div id="%s">
	Pagina %s
</div>""" %(appNome,appNome)
	
	modeloLocalNome = 'modelos/' + appNome + '.model.py'
	templateLocalNome = 'templates/' + appNome + '.php'
	
	makefile(modeloLocalNome,modeloPy)
	makefile(templateLocalNome,templatePhp)
	
try:
	acao = sys.argv[1]
	
	if(acao == 'projeto' or acao == 'Projeto' or acao == 'PROJETO'):
		print 'Iniciando Projeto %s' %(sys.argv[2])
		
		projetoNome = sys.argv[2]
		criarDiretorios()
		criarArquivos(projetoNome)
		
	elif(acao == 'banco' or acao == 'Banco' or acao == 'BANCO'):
		if not sys.argv[2] == '' or sys.argv[2] == null:
			try:
				print 'Executando modelo %s' %(sys.argv[2]+'.model.py')
				os.system('python modelos/%s' %(sys.argv[2]+'.model.py'))
			except:
				print 'Diretorio modelos ainda nao existe, inicie um projeto!'
		else:
			try:
				for modelo in os.listdir('modelos'):
					if modelo.count('model.py'):
						print 'Executando modelo %s' %(modelo)
						os.system('python modelos/%s' %(modelo)) 
			except:
				print 'Diretorio modelos ainda nao existe, inicie um projeto!'		
	elif(acao == 'aplicativo' or acao == 'Aplicativo' or acao == 'APLICATIVO'):
		if not sys.argv[2] == '' or sys.argv[2] == null:
			try:
				print 'Criando aplicativo %s' %(sys.argv[2])
				appNome = sys.argv[2]
				criarAplicativo(appNome)
			except:
				print 'Erro ao criar aplicativo, verifique o nome do mesmo!'					
except:
	print """
Bumba Meu Boi - A framwwork de desenvolvimento agil PHP

Modo de Usar:
	
	python bumbameu.py projeto [nome_do_projeto]
	python bumbameu.py aplicativo [nome_do_app]
	python bumbameu.py banco
"""