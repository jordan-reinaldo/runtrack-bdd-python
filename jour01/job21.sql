mysql> SELECT COUNT(*) AS nombre_etudiants_mineurs FROM etudiant
    -> WHERE age BETWEEN 18 AND 25;