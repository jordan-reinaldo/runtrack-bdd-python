import mysql.connector

mydb = mysql.connector.connect( 
    host="localhost",
    user="root",
    password="root",
    database="laplateforme"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM etudiant")
etudiant = mycursor.fetchall()
print(etudiant)

mycursor.close()
mydb.close()