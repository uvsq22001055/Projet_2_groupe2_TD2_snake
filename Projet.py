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
ROW, COL = (HEIGHT // COTE), (WIDTH // COTE)
COULEUR_FOND = '#3bbf3e'
COULEUR_MUR = '#9e6d36'
COULEUR_POMME = '#ad0017'
COULEUR_SERPENT = '#014386'
FOND = 0
MUR = -2
POMME = -1
DROITE = 5
GAUCHE = 6 
BAS = 7
HAUT = 8
vitesseTest = 2000

# Variables globales:

case = [[0 for row in range(ROW)] for col in range(COL)]
etat = [[FOND for row in range(ROW)] for col in range(COL)]
time = [[0 for row in range(ROW)] for col in range(COL)]
SPEED_GAME_SLOW = 2000
SPEED_GAME_MEDIUM = 1000
SPEED_GAME_FAST = 500
SPEED_GAME_CHOOSE = 0
END = 1
score = []
compteur = []
c = "vitesse : non-défini"
vitesse = 0
racine1 = 0
tete = 3
transfo = -tete
vitesse_entree = 2
Avance = HAUT
echec = False

#Defintions des fonctions :

def Generate_Pomme():
    """Génération de la pomme"""
    y = rd.randint(1, ROW-1)
    x = rd.randint(1, COL-1)
    if etat[y][x] == FOND:
        etat[y][x] = POMME
    else:
        Generate_Pomme()


def MangerPomme():
    global tete
    for x in range(1, ROW-1):
        for y in range(1, COL-1):
            if etat[x][y] == transfo:  
                if Avance == DROITE and etat[x+1][y] == POMME:
                    tete += 1
                    Generate_Pomme()
                elif Avance == GAUCHE and etat[x-1][y] == POMME:
                    tete += 1
                    Generate_Pomme()
                elif Avance == BAS and etat[x][y+1] == POMME:
                    tete += 1
                    Generate_Pomme()
                elif Avance == HAUT and etat[x][y-1] == POMME:
                    tete += 1
                    Generate_Pomme()



def Generate_Serpent():
    """Génération du serpent"""
    etat[15][15] = 3
    etat[15][14] = 2
    etat[15][13] = 1


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
                etat[y][x] = MUR
            elif x == 0:
                etat[y][x] = MUR
            elif y == (ROW - 1):
                etat[y][x] = MUR
            elif x == (COL - 1):
                etat[y][x] = MUR
    
    
def draw():
    for y in range(ROW):
        for x in range(COL):
            if etat[x][y] == transfo:
                coul = COULEUR_SERPENT
                canvas.itemconfig(case[y][x], fill=coul)
                etat[x][y] = tete
            elif etat[x][y] > 0:
                coul = COULEUR_SERPENT
                canvas.itemconfig(case[y][x], fill=coul)
            elif etat[x][y] == POMME:
                canvas.create_image(x*20+10, y*20+10,image= image_pomme)
            elif etat[y][x] == FOND:
                coul = COULEUR_FOND
                canvas.itemconfig(case[y][x], fill=coul)
            elif etat[y][x] == MUR:
                coul = COULEUR_MUR
                canvas.create_image(x*20+10, y*20+10, image=image_mur)           


def Avance_Serpent():
    global echec
    for x in range(1, ROW-1):
        for y in range(1, COL-1):
            if etat[x][y] == tete:  
                if Avance == DROITE:
                        etat[x+1][y] = transfo
                elif Avance == GAUCHE:
                        etat[x-1][y] = transfo
                elif Avance == BAS:
                        etat[x][y+1] = transfo
                elif Avance == HAUT:
                        etat[x][y-1] = transfo
            if etat[x][y] > 0:
                etat[x][y] -= 1
    for x in range(1, ROW-1):
        for y in range(1, COL-1):
            if Avance == DROITE:
                if etat[x][y] == transfo and etat[x+1][y] == MUR:
                    echec = True
            if Avance == GAUCHE:
                if etat[x][y] == transfo and etat[x-1][y] == MUR :
                    echec = True
            if Avance == BAS:
                if etat[x][y] == transfo and etat[x][y+1] == MUR :
                    echec = True
            if Avance == HAUT:
                if etat[x][y] == transfo and etat[x][y-1] == MUR :
                    echec = True
    print(etat)
    


def Echec():
    global echec, vitesse
    id_time = canvas.after(vitesse, Echec)
    Avance = HAUT
    if echec == False:
        print(Avance)
        print(echec)
        Avance_Serpent()
        MangerPomme()
        draw()
    elif echec == True:
        canvas.after_cancel(id_time)
        print("ok")


def Start(event):
    Echec()


def Fast():
    """Creation d'un bouton permettant de changer la vitesse en rapide"""
    global SPEED_GAME_FAST, c, vitesse
    c = "vitesse : rapide"
    vitesse = SPEED_GAME_FAST
    racine1.destroy()


def Slow():
    """Creation d'un bouton permettant de changer la vitesse en lente"""
    global SPEED_GAME_SLOW, c, vitesse
    c = "vitesse : lent"
    vitesse = SPEED_GAME_SLOW
    racine1.destroy()


def Medium():
    """Creation d'un bouton permettant de changer la vitesse en moyenne"""
    global SPEED_GAME_MEDIUM, c, vitesse
    c = "vitesse : moyen" 
    vitesse = SPEED_GAME_MEDIUM
    racine1.destroy()


def Vitesse():
    """Creation d'un bouton permettant au joueur d'entrer une vitesse de son choix"""
    global SPEED_GAME_CHOOSE, c, vitesse
    SPEED_GAME_CHOOSE = int(vitesse_entree) * 1000
    c = "vitesse : " + str(vitesse_entree) + " s"
    vitesse = SPEED_GAME_CHOOSE
    racine1.destroy()


def Grandir_Serpent():
    """Quand le serpent mange une pomme il grandit d'une unité"""


def Pseudo():
    """A chaque début de partie le joueur doit rentrer un pseudo"""


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


def Avance_Droite(event):
    global Avance
    Avance = DROITE


def Avance_Haut(event):
    global Avance
    Avance = HAUT


def Avance_Bas(event):
    global Avance
    Avance = BAS 

def get_entry(event):
    global vitesse_entree
    vitesse_entree = var.get()
    Vitesse()


################################## Programme principal#############################

#1ere fenetre demande vitesse
racine1 = tk.Tk()
racine1.title("Choix vitesse")
racine1.geometry("320x130")

var = tk.StringVar()

info = tk.Label(racine1, text="Choix du mode de vitesse", font=('arial', '15'))
buttonl = tk.Button(racine1, text='lent', font=('arial', '10'), command= Slow)
buttonm = tk.Button(racine1, text='moyen', font=('arial', '10'), command= Medium)
buttonr = tk.Button(racine1, text='rapide', font=('arial', '10'), command= Fast)
info2 = tk.Label(racine1, text="Ou choix de la période en seconde", font=('arial', '15'))
e1 = tk.Entry(racine1, textvariable = var)
racine1.bind('<Return>', get_entry)


info.grid(row=0, column=0, columnspan=5)
buttonl.grid(row=2, column=0)
buttonm.grid(row=2, column=2)
buttonr.grid(row=2, column=4)
info2.grid(row=3, column=0, columnspan=5)
e1.grid(row=4, column=2)

racine1.mainloop()

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

racine.mainloop()
