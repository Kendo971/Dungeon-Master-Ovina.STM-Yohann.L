import random

def generer_niveau():
    tab = []
    for i in range (0, 20):
        tab.append(random.randint(0,1))
    return tab

def traverse_niveau(niveau):
    vie = 1
    for i in niveau:
        if i == 1:
            dice = random.randint(1,6)
            if dice in [1, 2, 3]:
                vie = vie - 1
        if vie <= 0:
            return False
    return True

def main():
    niveaux_traverses = 0
    finished = False
    while not finished:
        niveau = generer_niveau()
        finished = traverse_niveau(niveau)
        niveaux_traverses += 1
        print(generer_niveau())
    print("Jeu terminé !", niveaux_traverses, "niveaux traversés avant de réussir !")
    
main()


