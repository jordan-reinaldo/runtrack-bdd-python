import mysql.connector

mydb = mysql.connector.connect( 
    host="localhost",
    user="root",
    password="root",
    database="laplateforme"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT superficie FROM etage")
superficies = mycursor.fetchall()
print(superficies)

somme_superficies = 0

for i in superficies:
    somme_superficies += i[0]  

print(f"La superficie de la plateforme est de {somme_superficies} m2")

mycursor.close()
mydb.close()