<?
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
