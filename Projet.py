################
# Auteurs:
# LEFEBVRE Elora
# GAY Arnaud
# GIAMMONA Leandre
# Nicolas Mimaud
# REBATI Rayan
# PEREZ Martin
#
# Groupe 2
# MPCI TD2
# dépot Github:
# https://github.com/uvsq22001055/Projet_2_groupe2_TD2_snake.git
################

#Import des librairies :

import tkinter as tk
import random as rd

#Definitions des contantes :


WIDTH, HEIGHT = 600, 600
COTE = 20
ROW, COL = (HEIGHT // COTE), (WIDTH // COTE)
COULEUR_FOND = '#3bbf3e'
COULEUR_MUR = '#9e6d36'
COULEUR_POMME = '#ad0017'
FOND = 0
MUR = 1
POMME = 2
SERPENT = 3

# Variables globales:

case = [[0 for row in range(ROW)] for col in range(COL)]
etat = [[FOND for row in range(ROW)] for col in range(COL)]
score = []
compteur = []

#Defintions des fonctions :

def Generate_Pomme() :
    """Génération de la pomme"""
    y = rd.randint(1, ROW-1)
    x = rd.randint(1, COL-1)
    etat[y][x] = POMME


def Generate_Serpent():
    """Génération du serpent"""
    


def base():
    for y in range(ROW):
        for x in range(COL):
            case[y][x] = canvas.create_rectangle(
                (x * COTE, y * COTE, (x + 1) * COTE, (y + 1) * COTE),
                outline=COULEUR_FOND,
                fill=COULEUR_FOND)
            etat[y][x] = FOND
    Generate_Decor()
    Generate_Pomme()
    draw()
                

def Generate_Decor() :
    """génération mur"""
    for y in range(ROW):
        for x in range(COL):
            if y == 0:
                etat[y][x] = 1
            elif x == 0:
                etat[y][x] = 1
            elif y == (ROW - 1):
                etat[y][x] = 1
            elif x == (COL - 1):
                etat[y][x] = 1
    
    
def draw():
    for y in range(ROW):
        for x in range(COL):
            if etat[y][x] == FOND:
                coul = COULEUR_FOND
                canvas.itemconfig(case[y][x], fill=coul)
            elif etat[y][x] == MUR:
                coul = COULEUR_MUR
                canvas.itemconfig(case[y][x], fill=coul)
            if etat[y][x] == POMME:
                coul = COULEUR_POMME
                canvas.itemconfig(case[y][x], fill=coul)


def Avance_Serpent():
    score()


def Vitesse() :
    """Creation d'un bouton permettant de changer la vitesse en trois vitesses différentes"""
    pass


def Echec():
    """Si le serpent rentre dans un mur ou dans sa propre queue la partie est perdue"""
    pass


def Grandir_Serpent() :
    """Quand le serpent mange une pomme il grandit d'une unité"""
    pass


def Start() :
    """Appuyer sur un bouton ou une touche pour démarrer la simulation"""
    pass


def Pseudo() :
    """A chaque début de partie le joueur doit rentrer un pseudo"""
    pass

def Score() :
    """le score est affiché sur une partie de l'écran"""
    if score[0] != compteur[0]:
        canvas.itemconfig(message_score, text=score[0])
        score[0] = compteur[0]


def Score_texte() :
    """le score est enregistré dans un fichier .txt"""
    f = open('score.txt', 'w')
    f.write('Pseudo', score[0])
    f.close()


# Programme principal

racine = tk.Tk()
racine.title("snake")


canvas = tk.Canvas(width = WIDTH, height = HEIGHT)

message_score = tk.Label(racine, text = "score : 0")
message_vitesse = tk.Label(racine, text = "vitesse : lent")

canvas.grid(column = 0, row = 1, columnspan = 2)
message_score.grid(column = 0, row = 0)
message_vitesse.grid(column = 1, row = 0)

base()

racine.mainloop()