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

# Import des librairies :
from PIL import Image, ImageTk
import tkinter as tk
import random as rd

# Definitions des contantes :


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

# Variables globales:

case = [[0 for row in range(ROW)] for col in range(COL)]
etat = [[FOND for row in range(ROW)] for col in range(COL)]
time = [[0 for row in range(ROW)] for col in range(COL)]
SPEED_GAME_SLOW = 2000
SPEED_GAME_MEDIUM = 1000
SPEED_GAME_FAST = 500
SPEED_GAME_CHOOSE = 0
END = 1
score = [0]
compteur = [0]
c = "vitesse : non-défini"
vitesse = 0
racine1 = 0
tete = 3
transfo = -tete
vitesse_entree = 2
Avance = HAUT
echec = False
PseudoJoueur = 0
Pseudo = 'pseudo non défini'

# Defintions des fonctions :


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
                    score[0] += 1
                elif Avance == GAUCHE and etat[x-1][y] == POMME:
                    tete += 1
                    Generate_Pomme()
                    score[0] += 1
                elif Avance == BAS and etat[x][y+1] == POMME:
                    etat[x][y+1] = FOND
                    tete += 1
                    Generate_Pomme()
                    score[0] += 1
                elif Avance == HAUT and etat[x][y-1] == POMME:
                    etat[x][y-1] = FOND
                    tete += 1
                    Generate_Pomme()
                    score[0] += 1


def Generate_Serpent():
    """Génération du serpent"""
    etat[15][15] = 1
    etat[15][14] = 2
    etat[15][13] = 3


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
                canvas.create_image(x*20+10, y*20+10, image=image_pomme)
            elif etat[y][x] == FOND:
                coul = COULEUR_FOND
                canvas.itemconfig(case[y][x], fill=coul)
            elif etat[y][x] == MUR:
                coul = COULEUR_MUR
                canvas.create_image(x*20+10, y*20+10, image=image_mur)
            Score_modifie()


def Avance_Serpent():
    global echec, tete
    for x in range(1, ROW-1):
        for y in range(1, COL-1):
            if etat[x][y] == tete:
                if Avance == DROITE:
                    if etat[x+1][y] != POMME:
                        etat[x+1][y] = transfo
                    else:
                        tete += 1
                        Generate_Pomme()
                        score[0] += 1
                        etat[x+1][y] = transfo
                elif Avance == GAUCHE:
                    if etat[x-1][y] != POMME:
                        etat[x-1][y] = transfo
                    else:
                        tete += 1
                        Generate_Pomme()
                        score[0] += 1
                        etat[x-1][y] = transfo
                elif Avance == BAS:
                    if etat[x][y+1] != POMME:
                        etat[x][y+1] = transfo
                    else:
                        tete += 1
                        Generate_Pomme()
                        score[0] += 1
                        etat[x][y+1] = transfo
                elif Avance == HAUT:
                    if etat[x][y-1] != POMME:
                        etat[x][y-1] = transfo
                    else:
                        tete += 1
                        Generate_Pomme()
                        score[0] += 1
                        etat[x][y-1] = transfo
            if etat[x][y] > 0:
                etat[x][y] -= 1
    Generate_Decor()
    for x in range(1, ROW-1):
        for y in range(1, COL-1):
            if Avance == DROITE:
                if etat[x][y] == (tete -1) and etat[x+1][y] == MUR or etat[x][y] == transfo and etat[x+1][y] > 0 :
                    echec = True
            if Avance == GAUCHE:
                if etat[x][y] == (tete -1) and etat[x-1][y] == MUR or etat[x][y] == transfo and etat[x-1][y] > 0 :
                    echec = True
            if Avance == BAS:
                if etat[x][y] == (tete -1) and etat[x][y+1] == MUR or etat[x][y] == transfo and etat[x][y+1] > 0 :
                    echec = True
            if Avance == HAUT:
                if etat[x][y] == (tete -1) and etat[x][y-1] == MUR or etat[x][y] == transfo and etat[x][y-1] > 0 :
                    echec = True


def Echec():
    global echec, vitesse
    id_time = canvas.after(vitesse, Echec)
    if echec == False:
        Avance_Serpent()
        """MangerPomme()"""
        draw()
    else:
        canvas.after_cancel(id_time)
        Pseudo()


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
    """Change la vitesse par celle choisit"""
    global SPEED_GAME_CHOOSE, c, vitesse
    SPEED_GAME_CHOOSE = float(vitesse_entree) * 1000
    c = "vitesse : " + str(vitesse_entree) + " s"
    vitesse = int(SPEED_GAME_CHOOSE)
    racine1.destroy()


def Pseudo():
    """A chaque début de partie le joueur doit rentrer un pseudo"""
    global Pseudo
    racine2 = tk.Tk()
    racine2.title("Choix du pseudo")
    racine2.geometry("320x70")

    Pseudo = tk.StringVar()

    question = tk.Label(racine2, text = "Entrer un pseudo", font = ('arial', '15'))
    info3 = tk.Entry(racine2, textvariable = Pseudo)

    question.grid(row = 0, column = 0)
    info3.grid(row = 1, column = 0)
    racine2.bind('<Return>', Entree_Joueur)

    racine2.mainloop()


def Score():
    """le score est affiché sur une partie de l'écran"""
    if score[0] != compteur[0]:
        canvas.itemconfig(message_score, text=score[0])
        score[0] = compteur[0]


def Score_texte():
    """le score est enregistré dans un fichier .txt"""
    global f, PseudoJoueur
    inwrite = str(PseudoJoueur) + " score = " + str(score[0])
    f = open('score.txt', 'a')
    f.write(inwrite)
    f.close()


def Score_modifie():
    b = "score : ", str(score[0])
    message_score.configure(text=b)


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


def Entree_Joueur(event):
    global PseudoJoueur, Pseudo
    PseudoJoueur = Pseudo.get()
    Score_texte()


# Programme principal:

# 1ere fenetre demande vitesse

racine1 = tk.Tk()
racine1.title("Choix vitesse")
racine1.geometry("320x130")

var = tk.StringVar()

info = tk.Label(racine1, text="Choix du mode de vitesse", font=('arial', '15'))
buttonl = tk.Button(racine1,
                    text='lent', font=('arial', '10'), command=Slow)
buttonm = tk.Button(racine1,
                    text='moyen', font=('arial', '10'), command=Medium)
buttonr = tk.Button(racine1,
                    text='rapide', font=('arial', '10'), command=Fast)
info2 = tk.Label(racine1,
                 text="Ou choix de la période en seconde",
                 font=('arial', '15'))
e1 = tk.Entry(racine1, textvariable=var)
racine1.bind('<Return>', get_entry)


info.grid(row=0, column=0, columnspan=5)
buttonl.grid(row=2, column=0)
buttonm.grid(row=2, column=2)
buttonr.grid(row=2, column=4)
info2.grid(row=3, column=0, columnspan=5)
e1.grid(row=4, column=2)

racine1.mainloop()

# 2eme fenetre, fenetre principale

racine = tk.Tk()
racine.title("snake")


canvas = tk.Canvas(width=WIDTH, height=HEIGHT)

message_score = tk.Label(racine, text="score : 0")
message_vitesse = tk.Label(racine, text=c)

canvas.grid(column=0, row=1, columnspan=2)
message_score.grid(column=0, row=0)
message_vitesse.grid(column=1, row=0)

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
