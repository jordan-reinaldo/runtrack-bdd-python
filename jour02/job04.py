import mysql.connector

mydb = mysql.connector.connect( 
    host="localhost",
    user="root",
    password="root",
    database="laplateforme"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT nom, capacite FROM salle")
salle = mycursor.fetchall()
print(salle)

mycursor.close()
mydb.close()