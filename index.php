<?
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
	
	if($arrayUrl[0] == 'js') {
		include("js/$arrayUrl[1]");
	}
	else if($arrayUrl[0] == 'css') {
		include("css/$arrayUrl[1]");
	}
	else if($arrayUrl[0] == 'api' && file_exists("templates/api/$arrayUrl[1].php")) {
		header('Content-type: application/json');
		include("templates/api/$arrayUrl[1].php");
	}
	else if($arrayUrl[0] == 'dados') {
		include("dados/$arrayUrl[1].php");
	}
	else if(file_exists("templates/$arrayUrl[0].php")) {
		include("includes/app.top.php");
		include("templates/$arrayUrl[0].php");
		include("includes/app.bot.php");
	}
	else {
		include("includes/app.top.php");
		include("templates/home.php");
		include("includes/app.bot.php");
	}
?>