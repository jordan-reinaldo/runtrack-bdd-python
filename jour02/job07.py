import mysql.connector
from Salarie import Salarie

mydb = mysql.connector.connect( 
    host="localhost",
    user="root",
    password="root",
    database="salarie"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM employe WHERE salaire >= 3000;")
salaire = mycursor.fetchall()
print(salaire)

mycursor.close()

mycursor = mydb.cursor()
mycursor.execute("SELECT employe.id_service, prenom, employe.nom, service.nom AS nom_service FROM employe JOIN service ON employe.id_service = service.id;")
service = mycursor.fetchall()
print(service)

mycursor.close()

mon_salarie = Salarie("localhost", "root", "root", "salarie")
mon_salarie.create("Base", "Billy", 5000, 1)
mon_salarie.read(1)
mon_salarie.update(1, 7000)
mon_salarie.delete(3)

mon_salarie.close()