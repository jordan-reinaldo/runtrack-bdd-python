import mysql.connector

class Salarie:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.mycursor = self.mydb.cursor()

    def create(self, nom, prenom, salaire, id_service):
        sql = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.mycursor.execute(sql, values)
        self.mydb.commit()

    def read(self, employee_id):
        sql = "SELECT * FROM employe WHERE id = %s"
        self.mycursor.execute(sql, (employee_id,))
        resultat = self.mycursor.fetchone()
        if resultat:
            print(f"Employee ID: {resultat[0]}")
            print(f"Nom: {resultat[1]}")
            print(f"Prenom: {resultat[2]}")
            print(f"Salaire: {resultat[3]}")
            print(f"ID Service: {resultat[4]}")
        else:
            print(f"Employee avec id {employee_id} non trouvé.")

    def update(self, employe_id, nouveau_salaire):
        sql = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (nouveau_salaire, employe_id)
        self.mycursor.execute(sql, values)
        self.mydb.commit()

    def delete(self, employe_id):
        sql = "DELETE FROM employe WHERE id = %s"
        self.mycursor.execute(sql, (employe_id,))
        self.mydb.commit()

    def close(self):
        self.mycursor.close()
        self.mydb.close()