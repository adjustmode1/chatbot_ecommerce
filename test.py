import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="laptop_store"
)

cursor = mydb.cursor()

mysql_select_query = ''' SELECT * from san_pham'''
cursor.execute(mysql_select_query)
record = cursor.fetchone()

print("1"+str(record[0]))