from geradores.modelo import *

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

modelo(name,data)