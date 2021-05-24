# Projet_2_groupe2_TD2_snake
Lorsqu'on lance le programme, une première fenêtre apparait, 
celle-ci permet de choisir la vitesse entre plusieurs vitesses différentes :
Rapide, Moyen ou lent; mais on peut également taper au clavier une vitesse en secondes.
Elle permet également de choisir entre deux terrains différents, et il existe notamment un bouton pour choisir aléatoirement entre les 2 terrains.

Lorsqu'on à finalement choisi sa vitesse la seconde fenêtre s'ouvre et lorsqu'on appuie sur la touche "ENTREE" le serpent se met à avancer.
Afin de contrôler le serpent, il faut utiliser les différentes flèches du clavier haut, bas, gauche, droite afin de se déplacer dans les directions correspondantes.

Lorsque le serpent touche une pomme, le score du joueur augmente de 1 et une nouvelle pomme apparait sur une position aléatoire dans le terrain.

Lorsque la partie se termine une fenêtre apparait pour rentrer le pseudo du joueur, ce pseudo sera enregistré avec le score correspondant dans un fichier nommé score.txt.
Ces scores seront alors repris pour créer un autre fichier, top10.txt, celui-ci classe dans l'ordre les 10 meilleurs score avec les pseudos correspondant.

Pour lire le programme, il faut bien s'assurer de posséder la bibliothèque "PIL", une bibliothèque annexe de Tkinter.