
#Implémentation 1 : o(n^2)

def is_eliminated(player1, player2):
    """
    Vérifie si player1 est éliminé par player2
    param player1, player2 : listes des tuples (nom, âge, score)
    retourne True si player1 est éliminé par player2, False sinon
    """
    _, age1, score1 =player1
    _, age2, score2 =player2
    return (age2 < age1 and score2 >= score1) or (age2 <= age1 and score2 > score1)

def find_champions(players):
    """
    Renvoie les champions dans une liste de joueurs
    Un joueur est champion s'il n'est éliminé par aucun autre joueur
    param players : liste des tuples (nom, âge, score)
    retourne champions : liste des champions (nom, âge, score)
    """
    champions =[]
    for i in range( len(players)) : 
        eliminated=False
        for j in range( len(players)) :
            if i != j : 
                #Vérifie si le joueur i est éliminé par le joueur j
                if (is_eliminated(players[i],players[j])) :
                    eliminated=True
                    break
        if not eliminated :
            champions.append(players[i])
    return champions



#Implémentation 2: o(nlog(n))

def merge(left, right):
    """
    Fusionne et trie deux listes triées selon le critère : 
    'âge croissant et en cas d'égalité selon le score décroissant'
    param left première liste triée
    param right deuxième liste triée
    retourne la liste fusionnée et triée
    """
    sorted_list=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i][1]<right[j][1] or (left[i][1]==right[j][1] and left[i][2]>right[j][2]):
            sorted_list.append(left[i])
            i+=1
        else :
            sorted_list.append(right[j])
            j+=1
    #Ajoute les élèments restants
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

def merge_sort(players):
    """
    Trie par fusion les joueurs selon l'âge croissant, et en cas d'égalité 
    selon le score décroissant
    param players : liste des tuples (nom, âge, score)
    retourne la liste players triée
    """
    if len(players)<=1 :
        return players
    #Divise la liste en deux moitiés
    left=merge_sort(players[:len(players)//2])
    right=merge_sort(players[len(players)//2:])
    #Fusionne les deux listes triées 
    return merge(left, right)

    
def find_champions_optimized(players):
    """"
    param players : liste des tuples (nom, âge, score)
    return champions : liste des champions (nom, âge, score)
    """
    #Trie (par fusion) les joueurs par âge croissant et en cas d'égalité par score décroissant 
    players_sorted=merge_sort(players)   #On peut également utiliser la fonction 'sorted' de python
    champions=[]
    max_score=float('-inf') #Le score maximum de la liste champions
    prev_age=0              #L'âge du dernier joueur ajouté à la liste des champions
    for player in players_sorted :
        _, age, score=player
        #Ajoute le joueur s'il a un score supérieur strictement au maximum actuel 
        #ou s'il a les mêmes caractéristiques avec le dernier champion ajouté
        if score>max_score or (score==max_score and prev_age==age) : 
            champions.append(player)
            max_score=score
            prev_age=age
    return champions
       

#Test 

def test_players(players, expected):
    """
    Fonction de test permettant de comparer les résultats attendus avec les résultats obtenus
    des fonctions 'find_champions' et 'find_champions_optimized'
    """
    print(f"Attendu :                   {expected}")
    print(f"Résultat implémentation 1 : {find_champions(players)}")
    print(f"Résultat implémentation 2 : {find_champions_optimized(players)}")
    print()
    

def Test():
    # Cas 1 : Liste vide
    players1 = []
    print("Test 1 : Liste vide")
    test_players(players1, [])

    # Cas 2 : Liste avec un seul joueur
    players2 = [("A", 20, 70)]
    print("Test 2 : Liste avec un seul joueur")
    test_players(players2,[("A", 20, 70)] )
    
    # Cas 3 : Liste de joueurs ayant le même score
    players3 = [("A", 20, 70), ("B", 25, 70), ("C", 18, 70), ("D", 21, 70)]
    print("Test 3 : Liste de joueurs ayant le même score")
    test_players(players3,[("C", 18, 70)] )
    
    # Cas 4 : Liste de joueurs ayant le même âge
    players4 = [("A", 20, 70), ("B", 20, 75), ("C", 20, 80), ("D",20, 85)]  
    print("Test 4 : Liste de joueurs ayant le même âge")
    test_players(players4, [("D", 20, 85)] )

    # Cas 5 : Liste avec deux joueurs, l'un domine l'autre
    players5 = [("A", 20, 70), ("B", 18, 75)]  
    print("Test 5 : Liste avec deux joueurs, l'un domine autre")
    test_players(players5, [("B", 18, 75)] )

    # Cas 6 : Liste avec deux joueurs, aucun ne domine l'autre
    players6 = [("A", 20, 70), ("B", 18, 60)]  
    print("Test 6 : Liste avec deux joueurs, un domine l'autre")
    test_players(players6, [("A", 20, 70), ("B", 18, 60)]  )

    # Cas 7 : Liste de joueurs ayant les mêmes caractéristiques
    players7 = [("A", 20, 70), ("B", 20, 70), ("C", 20, 70)]
    print("Test 7 : Liste de joueurs ayant les mêmes caractéristiques")
    test_players(players7, [("A", 20, 70), ("B", 20, 70), ("C", 20, 70)])

    # Cas 8 : 
    players8 = [("A", 20, 70), ("B", 18, 75), ("C", 22, 72), ("D", 25, 80)]
    print("Test 8 :")
    test_players(players8, [("B", 18, 75), ("D", 25, 80)] )

    # Cas 9 : 
    players9 = [("A", 20, 70), ("B", 18, 75), ("C", 22, 80), ("D", 19, 85)]
    print("Test 9 :")
    test_players(players9, [("B", 18, 75), ("D", 19, 85)])

    # Cas 10 : 
    players10 = [("A", 20, 10), ("B", 20, 20), ("C", 20, 30), ("D", 20, 40), ("E", 20, 50)]
    print("Test 10 :")
    test_players(players10, [("E", 20, 50)] )

    # Cas 11 :
    players11 = [("A", 20, 100), ("B", 22, 80), ("C", 18, 85), ("D", 25, 90), ("E",18, 85)]
    print("Test 11 :")
    test_players(players11, [("A", 20, 100),("C", 18, 85), ("E",18, 85)] )

    # Cas 12 : 
    players12 = [("A", 20, 70), ("B", 18, 75), ("C", 25, 80), ("D", 30, 90), ("E", 30, 90)]
    print("Test 12 :")
    test_players(players12, [("B", 18, 75), ("C", 25, 80), ("D", 30, 90), ("E", 30, 90)] )


# Appel de la fonction de test
Test()