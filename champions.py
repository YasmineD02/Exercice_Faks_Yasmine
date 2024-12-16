   
def find_champions(players):
    """"
    param players : liste des tuples (nom, âge, score)
    return champions : liste des champions (nom, âge, score)
    """
    #Trie les joueurs par âge croissant et en cas d'égalité par score décroissant 
    players_sorted = sorted(players, key=lambda x: (x[1], -x[2]))  
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
       
