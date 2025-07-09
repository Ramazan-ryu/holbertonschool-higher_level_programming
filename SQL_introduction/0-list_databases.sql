#!/usr/bin/python3
# list_databases
import mysql.connector
mysql.connector.connect(
	host="localhost",
       	user="root"
	)
cursor=connection.cursor
cursor execute("SHOW DATABASES ")
for db in cursor: print(db[0])
