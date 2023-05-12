from flask import render_template
from flask import Flask
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "MARVEL"
)
mycursor = mydb.cursor()


app = Flask(__name__)


@app.route('/personaggi')
def personaggList():
    mycursor.execute("SELECT * FROM Marvel_Characters limit 20")
    myresult= mycursor.fetchall()
    return render_template('marvel_personaggi.html', personaggi=myresult)
