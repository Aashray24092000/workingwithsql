# workingwithsql

connecting sql with python

1- inserting the data 

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into test3.ashraya values(125,'shubh')")
mycursor.execute("insert into test3.ashraya values(126,'ashu')")
mycursor.execute("insert into test3.ashraya values(127,'amit')")
mydb.commit()
mydb.close()

2- query or fetch the data

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("select * from test3.ashraya")
for i in mycursor.fetchall():
    print(i)
mydb.close()

3- create database and table by python


import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if not exists test3.ashraya(c1 INT,c2 VARCHAR(50));")
OR 
mycursor.execute("CREATE DATABASE if not exists test3")
mydb.close()

by sql-

CREATE TABLE table_name(c1 INT ,c2 VARCHAR(50));

4- select * from database.tablename;







