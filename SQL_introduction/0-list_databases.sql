#!/usr/bin/python3
# list_databases


import mysql.connector
connection=mysql.connector.connect(
	host="localhost",
       	user="root",
	password=""
)
cursor=connection.cursor()
cursor.execute("SHOW DATABASES")
for db in cursor: print(db[0])
