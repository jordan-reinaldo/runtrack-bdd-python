 UPDATE etudiant
    -> SET age = 20
    -> WHERE nom = 'Spaguetti' and prenom = 'Betty';

SELECT * FROM etudiant
    -> WHERE prenom = 'Betty' AND nom = 'Spaguetti'
    -> ;