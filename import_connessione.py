import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="MARVEL"
)
mycursor = mydb.cursor()

# Query to join the two tables
sql = """
SELECT Marvel_Characters.name, Marvel_Characters.ID, Marvel_Characters.ALIGN, Marvel_Characters.EYE, Marvel_Characters.HAIR,
       Marvel_Characters.SEX, Marvel_Characters.GSM, Marvel_Characters.ALIVE, Marvel_Characters.APPEARANCES,
       Marvel_Characters.FIRST_APPEARANCE, Marvel_Characters.Year, Film_Marvel.FILM
FROM Marvel_Characters
JOIN Film_Marvel ON Marvel_Characters.name = Film_Marvel.PERSONAGGIO
"""

# Execute the query
mycursor.execute(sql)

# Fetch all the rows
result = mycursor.fetchall()

# Print the result
for row in result:
    print(row)
