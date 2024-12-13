# Exercice_Faks_Yasmine : Détection des champions dans une liste de joueurs d'échecs

## Description
Cet exercice consiste à créer une fonction permettant d'extraire les "champions" d'une liste de joueurs d'échecs, où un joueur est considéré comme un champion si personne ne l'élimine, selon des critères d'âge et de score.


## Logique/Raisonnement 
Soit player(nom, age, score ) un joueur 
player est champion ssi player n’est éliminé par aucun autre joueur 

—---------------------------------------------------------------------------------------------------------------

player1(nom1, age1, score 1) n’est pas éliminé par player2(nom2, age2, score 2 ) ssi 

not ( score2 > score1 and age2 <= age 1) and not ( age2 < age1 and score2 >= score1)

c.a.d 

player1(nom1, age1, score 1) est éliminé par player2(nom2, age2, score 2 ) ssi 

( score2 > score1 and age2 <= age 1)  or ( age2 < age1 and score2 >= score1)


## Fonctionnalités principales
- **`find_champions`** : Cette fonction compare chaque joueur avec tous les autres pour vérifier s'il est éliminé. Si un joueur n'est éliminé par personne, il est considéré comme champion. Elle utilise la fonction "is_eliminated" pour déterminer si un joueur est éliminé. Sa complexité est O(n²).
- **`find_champions_optimized`** : Cette fonction trie d'abord les joueurs par âge croissant et score décroissant avec un tri par fusion. Ensuite, elle sélectionne les champions en parcourant la liste triée. Sa complexité de O(n log n).


## Performance : 
Implémentation 1 : Complexité temporel **o(n^2)** ce qui est acceptable pour les listes de petites tailles, mais peut devenir lente pour les listes de plus grandes tailles. 

Implémentation 2 : Complexité temporel **o(n log (n) )** ce qui offre une meilleure performance pour les grandes listes. 


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



## Instructions d'exécution
1- Installer Python.

2- Clonez ce repository sur votre machine locale.

3- Exécuter le fichier `champions.py`
