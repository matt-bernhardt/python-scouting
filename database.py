# Import libraries
import mysql.connector
import connection

cnx = ''
cursor = ''

def connect():
  global cnx, cursor

  cnx = mysql.connector.connect(user=connection.u, password=connection.p, host=connection.h, database=connection.d)
  cursor = cnx.cursor()

def disconnect():
  global cnx, cursor

  cursor.close()
  cnx.close()

def query(query):
  global cnx, cursor
  cursor.execute(query, ())
  return cursor
