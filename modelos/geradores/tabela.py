import sys
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

	con.execute(sql)