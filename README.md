# Exercice_Faks_Yasmine : Détection des champions dans une liste de joueurs d'échecs

## Description
Cet exercice consiste à créer une fonction permettant d'extraire les "champions" d'une liste de joueurs d'échecs, où un joueur est considéré comme un champion si personne ne l'élimine, selon des critères d'âge et de score.


## Fichiers du projet :
`champions.py` : Contient la fonction `find_champions`.
`test.py` : Contient les tests unitaires pour vérifier le comportement de `find_champions`.


## Test : 
Les cas traités : 
    -Liste vide 
    -Liste avec un seul joueur 
    -Liste avec des joueurs ayant le même score 
    -Liste avec des joueurs ayant le même âge 
    -Liste avec deux joueurs, l'un domine l’autre 
    -Liste avec deux joueurs aucun ne domine l’autre 
    -Liste avec plusieurs joueurs ayant les mêmes caractéristiques 
    -Liste avec plusieurs joueurs

# Exécution des tests
Pour exécuter tous les tests : `python3 test.py`

Pour exécuter un test spécifique : `python3 -m unittest test.TestFindChampions.<nom_de_la_fonction_test>`


## Autre : Logique/Raisonnement 
Soit player(nom, age, score ) un joueur 
player est champion ssi player n’est éliminé par aucun autre joueur 

—---------------------------------------------------------------------------------------------------------------

player1(nom1, age1, score 1) n’est pas éliminé par player2(nom2, age2, score 2 ) ssi 
not ( score2 > score1 and age2 <= age 1) and not ( age2 < age1 and score2 >= score1)

c.a.d 

player1(nom1, age1, score 1) est éliminé par player2(nom2, age2, score 2 ) ssi 
( score2 > score1 and age2 <= age 1)  or ( age2 < age1 and score2 >= score1)

