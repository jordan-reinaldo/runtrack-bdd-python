 SELECT * FROM etudiant
    -> WHERE age = (SELECT max(age) FROM etudiant);