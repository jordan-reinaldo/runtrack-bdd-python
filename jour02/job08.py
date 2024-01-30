import mysql.connector
import time

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

def ajouter_cage(superficie, capacite_max):
    try:
        query = """INSERT INTO cage (superficie, capacite_max)
                   VALUES (%s, %s);"""
        mycursor.execute(query, (superficie, capacite_max))
        mydb.commit()
        print("Cage ajoutée avec succès")
    except mysql.connector.Error as error:
        print(f"Échec de l'insertion de la cage : {error}")

def supprimer_cage(cage_id):
    try:
        query = "DELETE FROM cage WHERE id = %s;"
        mycursor.execute(query, (cage_id,))
        mydb.commit()
        print("Cage supprimée avec succès")
    except mysql.connector.Error as error:
        print(f"Échec de la suppression de la cage : {error}")

def modifier_cage(cage_id, superficie, capacite_max):
    try:
        query = """UPDATE cage
                   SET superficie = %s, capacite_max = %s
                   WHERE id = %s;"""
        mycursor.execute(query, (superficie, capacite_max, cage_id))
        mydb.commit()
        print("Cage modifiée avec succès")
    except mysql.connector.Error as error:
        print(f"Échec de la modification de la cage : {error}")

def afficher_cages():
    try:
        query = "SELECT * FROM cage;"
        mycursor.execute(query)
        result = mycursor.fetchall()
        print("Cages dans le zoo :")
        for row in result:
            print(row)
    except mysql.connector.Error as error:
        print(f"Échec de la récupération des cages : {error}")


while True:
    print("\nMenu:")
    print("1. Ajouter un animal")
    print("2. Supprimer un animal")
    print("3. Modifier un animal")
    print("4. Afficher tous les animaux")
    print("5. Afficher les animaux dans une cage spécifique")
    print("6. Calculer la superficie totale des cages")
    print("7. Ajouter une cage")
    print("8. Supprimer une cage")
    print("9. Modifier une cage")
    print("10. Afficher toutes les cages")
    print("11. Quitter")

    choix = input("Monsieur le directeur, veuillez faire votre choix : ")

    if choix == '1':
        nom = input("Entrez le nom de l'animal : ")
        race = input("Entrez la race de l'animal : ")
        cage_id = input("Entrez l'ID de la cage (laisser vide si inconnu) : ")
        date_de_naissance = input("Entrez la date de naissance (YYYY-MM-DD) : ")
        pays_origine = input("Entrez le pays d'origine : ")
        ajouter_animal(nom, race, cage_id or None, date_de_naissance, pays_origine)
    elif choix == '2':
        animal_id = input("Entrez l'ID de l'animal à supprimer : ")
        supprimer_animal(animal_id)
    elif choix == '3':
        animal_id = input("Entrez l'ID de l'animal à modifier : ")
        nom = input("Entrez le nouveau nom de l'animal : ")
        race = input("Entrez la nouvelle race de l'animal : ")
        cage_id = input("Entrez le nouvel ID de la cage (laisser vide si inconnu) : ")
        date_de_naissance = input("Entrez la nouvelle date de naissance (YYYY-MM-DD) : ")
        pays_origine = input("Entrez le nouveau pays d'origine : ")
        modifier_animal(animal_id, nom, race, cage_id or None, date_de_naissance, pays_origine)
    elif choix == '4':
        afficher_animaux()
    elif choix == '5':
        cage_id = input("Entrez l'ID de la cage dont vous voulez voir les animaux : ")
        afficher_animaux_par_cage(cage_id)
    elif choix == '6':
        superficie_totale()
    elif choix == '7':
        superficie = input("Entrez la superficie de la cage : ")
        capacite_max = input("Entrez la capacité maximale de la cage : ")
        ajouter_cage(superficie, capacite_max)
    elif choix == '8':
        cage_id = input("Entrez l'ID de la cage à supprimer : ")
        supprimer_cage(cage_id)
    elif choix == '9':
        cage_id = input("Entrez l'ID de la cage à modifier : ")
        superficie = input("Entrez la nouvelle superficie de la cage : ")
        capacite_max = input("Entrez la nouvelle capacité maximale de la cage : ")
        modifier_cage(cage_id, superficie, capacite_max)
    elif choix == '10':
        afficher_cages()
    elif choix == '11':
        print("Fermeture du programme...")
        break
    else:
        print("Choix non valide, veuillez réessayer.")
    time.sleep(1)
mycursor.close()
mydb.close()