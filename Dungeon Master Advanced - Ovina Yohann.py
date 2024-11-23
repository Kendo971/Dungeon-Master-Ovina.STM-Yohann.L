import random

# Génère un labyrinthe avec des ennemis
def generer_labyrinthe():
    laby = []
    for i in range(2): 
        ligne = [random.randint(0, 1) for i in range(20)]
        laby.append(ligne)
    return laby

# Fonction qui gère la rencontre avec un ennemi
def rencontre_ennemi(vie):
    dice = random.randint(1, 6)  
    if dice in [1, 2, 3]:  
        vie -= 1
    return vie

# Affiche le labyrinthe sur deux lignes
def labyrinthe(laby):
    for ligne in laby:
        print(" ".join(str(cell) for cell in ligne))
    print()

# Fonction qui vérifie s'il reste des ennemis dans le labyrinthe
def verif_ennemis(laby):
    for ligne in laby:
        if 1 in ligne: 
            return True
    return False

def main():
    niveaux_traverses = 0
    vie = 3  
    position_joueur = [0, 0] 
    arrivee = [1, 19]
    laby = generer_labyrinthe()  
    laby[position_joueur[0]][position_joueur[1]] = 9 
    print("Labyrinthe initial :")
    labyrinthe(laby)
    finished = False


    
    while not finished and vie > 0:
        deplacement = input("Déplacement (q: gauche, d: droite, z: haut, s: bas) : ").lower()
        # Enlève la position_joueur actuelle du joueur dans le labyrinthe
        laby[position_joueur[0]][position_joueur[1]] = 0
        # Déplacements du joueur dans le labyrinthe
        if deplacement == "q" and position_joueur[1] > 0:  # Gauche
            position_joueur[1] -= 1
        elif deplacement == "d" and position_joueur[1] < 19:  # Droite
            position_joueur[1] += 1
        elif deplacement == "z" and position_joueur[0] > 0:  # Haut
            position_joueur[0] -= 1
        elif deplacement == "s" and position_joueur[0] < 1:  # Bas
            position_joueur[0] += 1
        else:
            print ("Vous ne pouvez pas vous déplacer ici car c'est hors du labyrinthe")
            laby[position_joueur[0]][position_joueur[1]] = 9

        # Vérifie si le joueur rencontre un ennemi sur sa nouvelle position_joueur
        if laby[position_joueur[0]][position_joueur[1]] == 1:
            print("Rencontré un ennemi !")
            vie = rencontre_ennemi(vie)  
        laby[position_joueur[0]][position_joueur[1]] = 9
        

        
        labyrinthe(laby)
        print(f"Vie actuelle : {vie}")

        # Vérifie si tous les ennemis ont été éliminés
        if not verif_ennemis(laby):
            print("Félicitations ! Vous avez éliminé tous les ennemis du labyrinthe.")
            print(f"Jeu terminé après {niveaux_traverses} niveaux traversés.")
            break
        if vie <= 0:
            print(f"Jeu terminé ! Vous avez perdu après {niveaux_traverses} niveaux traversés.")
            break
        if position_joueur == arrivee:
            print("Bien joué ! Vous êtes arrivé jusqu'au bout !")
            break
        niveaux_traverses += 1
    if vie > 0 and verif_ennemis(laby):
        print(f"Félicitations ! Vous avez terminé le jeu avec {niveaux_traverses} niveaux traversés.")

main()
