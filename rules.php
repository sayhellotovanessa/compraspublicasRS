<?
	//Recebendo URLs Amigaveis

	if(isset($_GET["endereco"]))
		$endereco = $_GET["endereco"];
	else
		$endereco = false;

	$ultimo = strlen($endereco)-1;

	if($endereco[$ultimo] == "/")
		$endereco = substr($endereco, 0, $ultimo);

	$arrayUrl = explode("/", $endereco);
?>