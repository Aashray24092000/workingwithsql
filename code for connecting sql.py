#for inserting data

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if not exists test3.ashraya(c1 INT,c2 VARCHAR(50));")
mycursor.execute("CREATE DATABASE if not exists test3")
mydb.close()

#querying and fetching data

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

#create database and table by python

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if not exists test3.ashraya(c1 INT,c2 VARCHAR(50));")
mycursor.execute("CREATE DATABASE if not exists test3")
mydb.close()

#for retrieving the data

select * from database.table_name;
