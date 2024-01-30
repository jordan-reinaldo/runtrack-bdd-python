import mysql.connector

mydb = mysql.connector.connect( 
    host="localhost",
    user="root",
    password="root",
    database="laplateforme"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT capacite FROM salle")
capacite = mycursor.fetchall()
print(capacite)

somme_capacites = 0

for i in capacite:
    somme_capacites += i[0]  

print(f"La superficie de la plateforme est de {somme_capacites} m2")

mycursor.close()
mydb.close()