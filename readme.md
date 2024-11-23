## Dungeon Master Classic

Dans le cadre de notre projet Python, nous devions réaliser un mini-jeu où le joueur doit traverser des niveaux remplis de salles vides et d'ennemis. Le but est de réussir à traverser un niveau sans perdre toutes ses vies. A la fin le jeu affiche le nombre de niveaux qu'il a fallu traverser pour réussir.

Règles :
Chaque niveau contient 20 salles générées aléatoirement.
Le joueur commence chaque niveau avec 1 vie.
En rencontrant un ennemi, un dé est lancé :
- 1, 2, 3 : le joueur perd 1 vie.
- 4, 5, 6 : rien ne se passe.
Si la vie du joueur tombe à 0, la traversée échoue.
Le jeu continue jusqu'à ce qu'un niveau soit traversé avec succès.

## Dungeon Master Advanced

Ce mini-jeu est une version améliorée de "Dungeon Master Classic". Il y a 2 manières de gagner :
- Eliminer tous les ennemis sans perdre toutes ses vies.
- Accéder à la dernière salle située en bas à droite.
L'utilisateur a la possibilité de se déplacer en utilisant les touches suivantes :
- Z pour aller en haut.
- S pour aller en bas.
- Q pour aller à gauche.
- D pour aller à droite.

Les nouvelles règles sont :
- Le joueur commence la partie avec 3 vies.
- Lorsqu'on perd les niveaux ne se génèrent plus automatiquement contrairement à la version classique.
- Le joueur gagne soit en éliminant tous les ennemis, soit en atteignant la dernière salle en bas à droite ([1][19]).
En dehors de cela le système de dé reste inchangé.


## Auteurs

- [@Kendo971](https://www.github.com/Kendo971) Alias Yohann LACROIX
- [@QueenVon971](https://www.github.com/QueenVon971)  Alias Ovina SAINT-MARTIN


![Logo](https://sarcdprodstrapi.blob.core.windows.net/strapi-media/assets/logo_epsi_8b6f0271b8.png)

