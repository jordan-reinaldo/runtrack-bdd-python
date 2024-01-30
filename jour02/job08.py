import mysql.connector

mydb = mysql.connector.connect( 
    host="localhost",
    user="root",
    password="root",
    database="zoo"
)

mycursor = mydb.cursor()

def ajouter_animal(nom, race, cage_id, date_de_naissance, pays_origine):
    try:
        query = """INSERT INTO animal (nom, race, cage_id, date_de_naissance, pays_origine) 
                   VALUES (%s, %s, %s, %s, %s);"""
        mycursor.execute(query, (nom, race, cage_id, date_de_naissance, pays_origine))
        mydb.commit()
        print("Animal ajouté avec succès")
    except mysql.connector.Error as error:
        print(f"Échec de l'insertion de l'animal : {error}")

def supprimer_animal(animal_id):
    try:
        query = "DELETE FROM animal WHERE id = %s;"
        mycursor.execute(query, (animal_id,))
        mydb.commit()
        print("Animal supprimé avec succès")
    except mysql.connector.Error as error:
        print(f"Échec de la suppression de l'animal : {error}")

def modifier_animal(animal_id, nom, race, cage_id, date_de_naissance, pays_origine):
    try:
        query = """UPDATE animal
                   SET nom = %s, race = %s, cage_id = %s, date_de_naissance = %s, pays_origine = %s
                   WHERE id = %s;"""
        mycursor.execute(query, (nom, race, cage_id, date_de_naissance, pays_origine, animal_id))
        mydb.commit()
        print("Animal modifié avec succès")
    except mysql.connector.Error as error:
        print(f"Échec de la modification de l'animal : {error}")

def afficher_animaux():
    try:
        query = "SELECT * FROM animal;"
        mycursor.execute(query)
        result = mycursor.fetchall()
        print("Animaux dans le zoo :")
        for row in result:
            print(row)
    except mysql.connector.Error as error:
        print(f"Échec de la récupération des animaux : {error}")


def afficher_animaux_par_cage(cage_id):
    try:
        query = "SELECT * FROM animal WHERE cage_id = %s;"
        mycursor.execute(query, (cage_id,))
        result = mycursor.fetchall()
        print(f"Animaux dans la cage {cage_id} :")
        for row in result:
            print(row)
    except mysql.connector.Error as error:
        print(f"Échec de la récupération des animaux : {error}")

def superficie_totale():
    try:
        query = "SELECT SUM(superficie) FROM cage;"
        mycursor.execute(query)
        result = mycursor.fetchone()
        print(f"Superficie totale des cages : {result[0]} m²")
    except mysql.connector.Error as error:
        print(f"Échec de la récupération de la superficie totale : {error}")

ajouter_animal("zoe","chien",1,"2019-01-02","france")  
ajouter_animal("billy","singe",2,"2017-03-11","Tanzanie")  
ajouter_animal("abdou","chat",2,"2016-04-10","Rouamnie")
ajouter_animal("lili","chien",1,"2015-06-01","france")
afficher_animaux()
afficher_animaux_par_cage(2)
modifier_animal(1,"zoe","fouine",1,"2019-01-02","france")
supprimer_animal(6)
afficher_animaux()

mycursor.close()
mydb.close()