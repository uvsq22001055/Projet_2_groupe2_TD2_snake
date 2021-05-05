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
from PIL import Image, ImageTk
import tkinter as tk
import random as rd

#Definitions des contantes :


WIDTH, HEIGHT = 600, 600
COTE = 20
ROW, cOL = (HEIGHT // COTE), (WIDTH // COTE)
COULEUR_FOND = '#3bbf3e'
COULEUR_MUR = '#9e6d36'
COULEUR_POMME = '#ad0017'
COULEUR_SERPENT = '#014386'
FOND = 0
MUR = 1
POMME = 2
SERPENT = 3
Avance = 4
DROITE = 5
GAUCHE = 6 
BAS = 7
HAUT = 8
TETE = 9
vitesseTest = 2000

# Variables globales:

case = [[0 for row in range(ROW)] for col in range(COL)]
etat = [[FOND for row in range(ROW)] for col in range(COL)]
SPEED_GAME_SLOW = 2000
SPEED_GAME_MEDIUM = 1000
SPEED_GAME_FAST = 500
SPEED_GAME_CHOOSE = 0
END = 1
score = []
compteur = []
c = "vitesse : non-défini"
vitesse = 0


#Defintions des fonctions :

def Generate_Pomme():
    """Génération de la pomme"""
    y = rd.randint(1, ROW-1)
    x = rd.randint(1, cOL-1)
    if etat[y][x] != SERPENT and etat[y][x] != MUR:
        etat[y][x] = POMME
        canvas.create_image(x*20+10, y*20+10,image=image_pomme)
    else:
        Generate_Pomme()


def Generate_Serpent():
    """Génération du serpent"""
    etat[15][15] = TETE
    



def base():
    for y in range(ROW):
        for x in range(COL):
            case[y][x] = canvas.create_rectangle(
                (x * COTE, y * COTE, (x + 1) * COTE, (y + 1) * COTE),
                outline=COULEUR_FOND,
                fill=COULEUR_FOND)
            etat[y][x] = FOND
    Generate_Decor()
    Generate_Serpent()
    Generate_Pomme()
    draw()
                

def Generate_Decor():
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
                canvas.create_image(x*20+10, y*20+10, image=image_mur)
            elif etat[x][y] == SERPENT:
                coul = COULEUR_SERPENT
                canvas.itemconfig(case[y][x], fill=coul)
            elif etat[x][y] == TETE:
                coul = COULEUR_SERPENT
                canvas.itemconfig(case[y][x], fill=coul)


def Avance_Serpent(): 
    while Echec == False :
        for x in range(1, len(etat)-1):
            for y in range(1, len(etat)-1):
                if Avance == DROITE :
                    if etat[x][y] == TETE :
                        etat[x+1][y] = TETE

                if Avance == GAUCHE :
                    if etat[x][y] == TETE :
                        etat[x-1][y] = TETE

                if Avance == BAS :
                    if etat[x][y] == TETE :
                        etat[x][y+1] = TETE

                if Avance == HAUT :
                    if etat[x][y] == TETE :
                        etat[x][y-1] = TETE
            draw()
    print(etat)
    id_Avance_Serpent = canvas.after(vitesse, Avance_Serpent)
    if Echec == True :
        canvas.after_cancel(id_Avance_Serpent)
    pass


def Fast():
    """Creation d'un bouton permettant de changer la vitesse en rapide"""
    global SPEED_GAME_FAST, c, vitesse
    c = "vitesse : rapide"
    vitesse = SPEED_GAME_FAST


def Slow():
    """Creation d'un bouton permettant de changer la vitesse en lente"""
    global SPEED_GAME_SLOW, c, vitesse
    c = "vitesse : lente"
    vitesse = SPEED_GAME_SLOW


def Medium():
    """Creation d'un bouton permettant de changer la vitesse en moyenne"""
    global SPEED_GAME_MEDIUM, c vitesse
    c = "vitesse : moyenne"
    vitesse = SPEED_GAME_MEDIUM


def Vitesse():
    """Creation d'un bouton permettant au joueur d'entrer une vitesse de son choix"""
    global SPEED_GAME_CHOOSE, c vitesse
    SPEED_GAME_CHOOSE = e1 * 1000
    c = "vitesse : choisie"
    vitesse = SPEED_GAME_CHOOSE

def Echec():
    """Si le serpent rentre dans un mur ou dans sa propre queue la partie est perdue"""
    global Echec
    Echec = False

    for x in range(1, len(etat)):
        for y in range(1, len(etat)):
            if Avance == DROITE :
                if etat[x+1][y] == MUR :
                    Echec = True
            if Avance == GAUCHE :
                if etat[x-1][y] == MUR :
                    Echec = True
            if Avance == BAS :
                if etat[x][y+1] == MUR :
                    Echec = True
            if Avance == HAUT :
                if etat[x][y-1] == MUR :
                    Echec = True
    canvas.after(vitesseTest, Echec)
    pass


def Grandir_Serpent():
    """Quand le serpent mange une pomme il grandit d'une unité"""
    pass


def Start():
    """Appuyer sur un bouton ou une touche pour démarrer la simulation"""
    global END, SPEED_GAME_FAST, SPEED_GAME_MEDIUM, SPEED_GAME_SLOW, SPEED_GAME_CHOOSE
    Avance_Serpent()
    id_Game = canvas.after(SPEED_GAME_SLOW or SPEED_GAME_FAST or SPEED_GAME_MEDIUM or SPEED_GAME_CHOOSE, Start)
    if END == 0:
        canvas.after_cancel(id_Game)


def Pseudo():
    """A chaque début de partie le joueur doit rentrer un pseudo"""
    pass


def Score():
    """le score est affiché sur une partie de l'écran"""
    if score[0] != compteur[0]:
        canvas.itemconfig(message_score, text=score[0])
        score[0] = compteur[0]


def Score_texte():
    """le score est enregistré dans un fichier .txt"""
    pseudo = input("Rentrez votre pseudo:" "\n")
    f = open('score.txt', 'w')
    f.write(Pseudo, score[0])
    f.close()

def Avance_Gauche(event):
    global Avance 
    Avance = GAUCHE
    pass


def Avance_Droite(event):
    global Avance
    Avance = DROITE
    pass


def Avance_Haut(event):
    global Avance
    Avance = HAUT
    pass


def Avance_Bas(event):
    global Avance
    Avance = BAS 
    pass


def Speed():
    racine1 = tk.Tk()
    racine1.title("Choix vitesse")
    racine1.geometry("320x130")
    info = tk.Label(racine1, text="Choix du mode de vitesse", font=('arial', '15'))
    buttonl = tk.Button(racine1, text='lent', font=('arial', '10'), command = Slow)
    buttonm = tk.Button(racine1, text='moyen', font=('arial', '10'), command = Medium)
    buttonr = tk.Button(racine1, text='rapide', font=('arial', '10'), command = Fast)
    info2 = tk.Label(racine1, text="Ou choix de la période en seconde", font=('arial', '15'))
    e1 = tk.Entry(racine1)


    info.grid(row=0, column=0, columnspan=5)
    buttonl.grid(row=2, column=0)
    buttonm.grid(row=2, column=2)
    buttonr.grid(row=2, column=4)
    info2.grid(row=3, column=0, columnspan=5)
    e1.grid(row=4, column=2)

    racine1.mainloop()

################################## Programme principal#############################

#1ere fenetre demande vitesse
Speed()


#2eme fenetre, fenetre principale
racine = tk.Tk()
racine.title("snake")


canvas = tk.Canvas(width = WIDTH, height = HEIGHT)

message_score = tk.Label(racine, text = "score : 0")
message_vitesse = tk.Label(racine, text = c)

canvas.grid(column = 0, row = 1, columnspan = 2)
message_score.grid(column = 0, row = 0)
message_vitesse.grid(column = 1, row = 0)

canvas.bind_all('<KeyPress-d>', Fast)
canvas.bind_all('<KeyPress-q>', Slow)
canvas.bind_all('<KeyPress-s>', Medium)
canvas.bind_all('<Return>', Start)
canvas.bind_all('<KeyPress-v>', Vitesse)
canvas.bind_all('<Right>', Avance_Droite)
canvas.bind_all('<Left>', Avance_Gauche)
canvas.bind_all('<Down>', Avance_Bas)
canvas.bind_all('<Up>', Avance_Haut)

photo_pomme = Image.open("apple.png")
image_pomme = ImageTk.PhotoImage(photo_pomme)

photo_mur = Image.open("mur.png")
image_mur = ImageTk.PhotoImage(photo_mur)

base()
Avance_Serpent()

racine.mainloop()