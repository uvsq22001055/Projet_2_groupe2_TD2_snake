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


WIDTH, HEIGHT = 800, 800
COTE = 20
ROW, COL = (HEIGHT // COTE), (WIDTH // COTE)
COULEUR_FOND = '#3bbf3e'
COULEUR_MUR = '#9e6d36'
MUR = 1
POMME = 2
SERPENT = 3

# Variables globales:

case = [[0 for row in range(ROW)] for col in range(COL)]


#Defintions des fonctions :

def Generate_Pomme() :
    """Génération de la pomme"""
    pass


def Generate_Serpent():
    """Génération du serpent"""
    pass


def base():
    for y in range(ROW):
        for x in range(COL):
            case[x][y] = canvas.create_rectangle(
                (x * COTE, y * COTE, (x + 1) * COTE, (y + 1) * COTE),
                outline=COULEUR_FOND,
                fill=COULEUR_FOND)

def Generate_Decor() :
    """génération mur"""
    for y in range(ROW):
        for x in range(COL):
            if y == 0:
                case[y][x] = 1
            elif x == 0:
                case[y][x] = 1
            elif x == (COL - 1):
                case[y][x] = 1
            else:
                case[y][x] = 0
    
    
def draw():
    for y in range(HEIGHT // COTE):
        for x in range(WIDTH // COTE):
            if case[x][y] == MUR:
                coul = COULEUR_MUR
                canvas.itemconfig(case[x][y], fill=coul)

def Avance_Serpent():
    pass


def Position_Pomme() :
    """Génération de la première pomme et quand celle ci est mangée une autre apparait à une position aléatoire"""
    pass


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
    pass


def Score_texte() :
    """le score est enregistré dans un fichier .txt"""
    pass


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
Generate_Decor()
draw()
racine.mainloop()