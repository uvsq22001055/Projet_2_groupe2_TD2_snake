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

#Definitions des contantes :

WIDTH, HEIGHT = 500, 500
COULEUR_FOND = '#3bbf3e'

#Defintions des fonctions :

def Generate_Pomme() :
    """Génération de la pomme"""
    pass


def Generate_Serpent():
    """Génération du serpent"""
    pass


def Generate_Decor() :
    """génération mur"""
    pass


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


def Entre_Pseudo() :
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

canvas = tk.Canvas(width = WIDTH, height = HEIGHT, bg = COULEUR_FOND)

canvas.grid(column = 0, row = 0)

racine.mainloop()