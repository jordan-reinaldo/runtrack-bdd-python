SELECT * FROM etudiant
    -> WHERE age = (SELECT min(age) FROM etudiant);