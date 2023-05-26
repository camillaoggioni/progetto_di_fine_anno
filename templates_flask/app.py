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
    mycursor.execute("""SELECT Marvel_Characters.name, Marvel_Characters.ID, Marvel_Characters.ALIGN, Marvel_Characters.EYE, Marvel_Characters.HAIR,
       Marvel_Characters.SEX, Marvel_Characters.GSM, Marvel_Characters.ALIVE, Marvel_Characters.APPEARANCES,
       Marvel_Characters.FIRST_APPEARANCE, Marvel_Characters.Year, Film_Marvel.FILM, Marvel_Characters.IB
       FROM Marvel_Characters
       JOIN Film_Marvel ON Marvel_Characters.name = Film_Marvel.PERSONAGGIO
       LIMIT 20 """)
    myresult= mycursor.fetchall()
    return render_template('marvel_personaggi.html', personaggi=myresult)
