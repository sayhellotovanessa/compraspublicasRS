import sys
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
