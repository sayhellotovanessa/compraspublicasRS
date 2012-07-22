
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
	tmp = '<?\n\n //Desativado por seguranca, aprenda a fazer testes!\n ini_set(\'display_errors\', 0);\n\n'
	tmp += 'class %s extends conexao {\n\n\tvar $con;\n\n\tfunction __construct() { \n\t\t $this->con = new conexao;\n\t}\n\n' %(name)

	#INSERT
	tmp += '\t function inserir('

	i = 0
	while i < len(data):

		if not i == len(data) - 1:
			if not data[i][0] == 'id' or data[i][0] == 'ID':
				tmp += '$' + data[i][0] + ', '
		else:
			if not data[i][0] == 'id' or data[i][0] == 'ID':
				tmp += '$' + data[i][0]	

		i = i + 1

	tmp += ') { \n'
	tmp += "\t\t$dados = array("

	i = 0
	while i < len(data):

		if not i == len(data) - 1:
			if not data[i][0] == 'id' or data[i][0] == 'ID':
				tmp += '$' + data[i][0] + ', '
		else:
			if not data[i][0] == 'id' or data[i][0] == 'ID':
				tmp += '$' + data[i][0]	

		i = i + 1

	tmp += ');\n' 
	tmp += "\t\t$colunas = array("

	i = 0
	while i < len(data):

		if not i == len(data) - 1:
			if not data[i][0] == 'id' or data[i][0] == 'ID':
				tmp += "'" + data[i][0] + "', "
		else:
			if not data[i][0] == 'id' or data[i][0] == 'ID':
				tmp += "'" + data[i][0]	 + "'"

		i = i + 1

	tmp += ');\n'
	tmp +=	"\t\t$this->con->insert('%s', $dados, $colunas);\n" %(name)

	tmp += '\t}\n\n'

	#UPDATE
	tmp += '\t function atualizar('

	i = 0
	while i < len(data):
		
		if not i == len(data) - 1:
			tmp += '$' + data[i][0] + ', '
		else:
			tmp += '$' + data[i][0]	

		i = i + 1

	tmp += ') { \n'
	tmp += "\t\t$dados = array("

	i = 0
	while i < len(data):
		
		if not data[i][0] == 'id':
			if not i == len(data) - 1:
				tmp += '$' + data[i][0] + ', '
			else:
				tmp += '$' + data[i][0]	

		i = i + 1

	tmp += ');\n' 
	tmp += "\t\t$colunas = array("

	i = 0
	while i < len(data):
		
		if not data[i][0] == 'id':
			if not i == len(data) - 1:
				tmp += "'" + data[i][0] + "', "
			else:
				tmp += "'" + data[i][0]	 + "'"

		i = i + 1

	tmp += ');\n'
	tmp +=	"\t\t$this->con->update('%s', $dados, $colunas, $id);\n" %(name)

	tmp += '\t}\n\n'

	#DELETE
	tmp += "\t function deletar($coluna,$criterio) { \n\t\t$this->con->delete('%s', $coluna, $criterio);\n" %(name)

	tmp += '\t}\n\n'
	
	tmp += "\tfunction todos() { \n\t\t$todos = $this->con->sql_query('SELECT * FROM %s');\n" %(name)
	
	tmp += "\n\t\treturn $todos;\n\t}\n"
	
	tmp += '}\n\n?>'	

	salvar(name,tmp)
