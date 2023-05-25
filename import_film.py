import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="MARVEL"
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS MARVEL")


mycursor.execute("DROP TABLE IF EXISTS  MARVEL.Film_Marvel")
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS MARVEL.Film_Marvel ( 
    ID INTEGER PRIMARY KEY AUTO_INCREMENT,
    PERSONAGGIO VARCHAR(50),
    FILM VARCHAR (1000)
 );""")

mycursor.execute("DELETE FROM MARVEL.Film_Marvel")
mydb.commit()

clash_data = pd.read_csv('./film.csv', index_col=False, delimiter = ',')
clash_data = clash_data.fillna('Null')
print(clash_data.head(20))
print (len(clash_data.columns))
#Fill the table
for i,row in clash_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO Film_Marvel (PERSONAGGIO,FILM) VALUES (%s,%s)"
    cursor.execute(sql, tuple(row))
   
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM MARVEL.Film_Marvel")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

