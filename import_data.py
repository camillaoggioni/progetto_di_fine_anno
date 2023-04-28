import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS MARVEL")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS MARVEL.Marvel_Characters (
    IB INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    ID VARCHAR(50),
    ALIGN VARCHAR(50),
    EYE VARCHAR(30),
    HAIR VARCHAR(30),
    SEX VARCHAR(50),
    GSM VARCHAR(50),
    ALIVE VARCHAR(30),
    APPEARANCES VARCHAR(30),
    FIRST_APPEARANCE VARCHAR(30),
    Year VARCHAR(30)
  );""")


mycursor.execute("DELETE FROM MARVEL.Marvel_Characters")
mydb.commit()

#Read data from a csv file
clash_data = pd.read_csv('./Marvel Movies.csv', index_col=False, delimiter = ',')
clash_data = clash_data.fillna('Null')
print(clash_data.head(20))
print (len(clash_data.columns))
#Fill the table
for i,row in clash_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO MARVEL.Marvel_Characters (name, ID, ALIGN, EYE, HAIR, SEX, GSM, ALIVE, APPEARANCES, FIRST_APPEARANCE, Year) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM MARVEL.Marvel_Characters")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)