# On importe les librairies
from math import*
from random import*
from time import*
from colorama import*

# On crée les Variables du joueur durant sa partie
vie = 100
armee = 50
religion = 50
peuple = 50
economie = 50

# On crée les Variables des item du joueur
Clairvoyance = 0

# exemplue d'écriture


def hellow_world():
    print("Espace dev pour gérer les couleur de ARPE")

    print("\n")
    print(Fore.LIGHTBLUE_EX + "Cette couleur sera utiliser pour : Mettre en évidence les éléments important des phrase des PNJ " + Fore.RESET)
    print(Fore.BLUE + "Cette couleur sera utiliser pour : Afficher des TITRE " + Fore.RESET)
    print(Fore.CYAN + "Cette couleur sera utiliser pour : Mettre en évidence les choix que la joueur peut faire  " + Fore.RESET)

    print("\n")
    print(Fore.RED + "Cette couleur sera utiliser pour : Les Malus " + Fore.RESET)
    
    print("\n")
    print(Fore.LIGHTGREEN_EX + "Cette couleur sera utiliser pour : Afficher les donnée statistique du joueur " + Fore.RESET)
    print(Fore.GREEN + "Cette couleur sera utiliser pour : Les Bonus " + Fore.RESET)

    print("\n")
    print(Fore.LIGHTYELLOW_EX + "Cette couleur sera utiliser pour : Annoncer le rôle et le nom des PNJ : " + Fore.RESET)

    print("\n")
    print(Fore.LIGHTMAGENTA_EX + "Cette couleur sera utiliser pour : CIRCONSTANCE INDETERMINER " + Fore.RESET)
    print(Fore.MAGENTA + "Cette couleur sera utiliser pour : CIRCONSTANCE INDETERMINER " + Fore.RESET)

    print("\n")
    print(Fore.BLACK + "Cette couleur sera utiliser pour : écriture normal adapté au constraste du fond.  " + Fore.RESET)
    print(Fore.LIGHTBLACK_EX + "Cette couleur sera utiliser pour : écriture normal adapté au constraste du fond.   " + Fore.RESET)
    print(Fore.LIGHTWHITE_EX + "Cette couleur sera utiliser pour : écriture normal adapté au constraste du fond.  " + Fore.RESET)
    print(Fore.WHITE + "Cette couleur sera utiliser pour : écriture normal adapté au constraste du fond.  " + Fore.RESET)

    print("\n")

hellow_world()


# On crée les conditions de fin de partie lié au variable ci-dessus.
while (armee != 0 or 100) or (religion != 0 or 100) or (peuple != 0 or 100) or (economie != 0 or 100) or (vie != 0):
    if armee <= 0:
        print(Fore.LIGHTBLUE_EX + "Vous n'avez plus aucun soldat et les autres royaumes se disputent le vôtre." + Fore.RESET)
        print(Fore.RED + "FIN DE LA PARTIE" + Fore.RESET)
        print(Fore.YELLOW,"\n Statistiques de la partie :", Fore.RESET, Fore.LIGHTYELLOW_EX , "\n Armée :", armee, "\n Religion :",religion, "\n Peuple :", peuple, "\n Economie :", economie, "\n", Fore.RESET)
        break
    elif armee >= 100:
        print("L'armée vous chasse et prend votre place.")
        print("FIN DE LA PARTIE")
        print("\n Statistiques de la partie :\n Armée :", armee, "\n Religion :",
              religion, "\n Peuple :", peuple, "\n Economie :", economie, "\n")
        break
    elif religion <= 0:
        print("Votre peuple ne croit plus en rien.")
        print("FIN DE LA PARTIE")
        print("\n Statistiques de la partie :\n Armée :", armee, "\n Religion :",
              religion, "\n Peuple :", peuple, "\n Economie :", economie, "\n")
        break
    elif religion >= 100:
        print("L'évêque Antoine Malbonne vous chasse du pouvoir et prend votre place.")
        print("FIN DE LA PARTIE")
        print("\n Statistiques de la partie :\n Armée :", armee, "\n Religion :",
              religion, "\n Peuple :", peuple, "\n Economie :", economie, "\n")
        break
    elif peuple <= 0:
        print("Vous n'avez plus aucun habitant, vous perdez votre pouvoir.")
        print("FIN DE LA PARTIE")
        print("\n Statistiques de la partie :\n Armée :", armee, "\n Religion :",
              religion, "\n Peuple :", peuple, "\n Economie :", economie, "\n")
        break
    elif peuple >= 100:
        print("Le peuple décide d'une révolte et vous chasse.")
        print("FIN DE LA PARTIE")
        print("\n Statistiques de la partie :\n Armée :", armee, "\n Religion :",
              religion, "\n Peuple :", peuple, "\n Economie :", economie, "\n")
        break
    elif economie <= 0:
        print("Le peuple prend le pouvoir suite à une Révolution.")
        print("FIN DE LA PARTIE")
        print("\n Statistiques de la partie :\n Armée :", armee, "\n Religion :",
              religion, "\n Peuple :", peuple, "\n Economie :", economie, "\n")
        break
    elif economie >= 100:
        print("Vous mourrez étouffé suite à un buffet organisé.")
        print("FIN DE LA PARTIE")
        print("\n Statistiques de la partie :\n Armée :", armee, "\n Religion :",
              religion, "\n Peuple :", peuple, "\n Economie :", economie, "\n")
        break
    elif vie <= 0:
        print("Vous mourrez, fin de la partie !")
        print("FIN DE LA PARTIE")
        print("\n Statistiques de la partie :\n Armée :", armee, "\n Religion :",
              religion, "\n Peuple :", peuple, "\n Economie :", economie, "\n")
        break

# Combat sous forme de pierre feuille ciseaux


def Combat():
    regle_Combat = input(
        "Voulez vous connaitre les règles du jeu ? \n 1 : Connaitre les règle \n 2 : Ne pas connaitre les règle (c'est un peirre feuille ciseaux tu dois connaitre ahah) ")
    if regle_Combat == "1":
        print("\n")
        print("Voici les règle du jeu :")
        print("Le jeu se joue entre vous et votre ennemis.")
        print("Pour gagner il faut avoir un signe plus fort que celui de votre ennemis. ")
        print("La pierre bat le ciseaux.")
        print("La feuille bat la pierre.")
        print("Le ciseaux bat la feuille.")
        print("Si vous et votre ennemis ont le même signe, il y a égalité.")
        print("\n")
    pierre = 1
    feuille = 2
    ciseaux = 3
    choix = randint(1, 3)
    choix_joueur_C = int(input("Veuillez choisir entre \n 1 : La Pierre \n 2 : La Feuille \n 3 : Le Ciseaux \n"))
    if choix_joueur_C == 1:
        print("Vous avez choisi la pierre")
    elif choix_joueur_C == 2:
        print("Vous avez choisi la feuille")
    elif choix_joueur_C == 3:
        print("Vous avez choisi le ciseaux")
    if choix_joueur_C == choix:
        print("Egalité")
        print("Il n'y a aucune conséquence.")
    elif choix_joueur_C == 1 and choix == 2:
        print("Vous avez perdu")
    elif choix_joueur_C == 1 and choix == 3:
        print("Vous avez gagné")
    elif choix_joueur_C == 2 and choix == 1:
        print("Vous avez gagné")
    elif choix_joueur_C == 2 and choix == 3:
        print("Vous avez perdu")
    elif choix_joueur_C == 3 and choix == 1:
        print("Vous avez perdu")
    elif choix_joueur_C == 3 and choix == 2:
        print("Vous avez gagné")
    else:
        print("Vous n'avez pas respecter les règles. Veuillez recommencer")
        Combat()

# Jeu du Nain Rouge


def Nain_Rouge():
    regle_Nain_Rouge = input(
        "Voulez vous connaitre les règles du jeu ? \n 1 : Connaitre les règle \n 2: Ne pas connaitre les règle (Vous connaisez ? O_o) ")
    if regle_Nain_Rouge == "1":
        print("\n")
        print("Voici les règle du jeu :")
        print("Le jeu se joue entre vous et votre Fou.")
        print("Vous devez choisir entre pair ou impair.")
        print("On lance deux dé a six faces et on compare les deux dés.")
        print("Si vous avez choisir la bonne option, vous gagnez une récompense aléatoire.")
        print("\n")
    de1 = randint(1, 6)
    de2 = randint(1, 6)
    de_total = de1 + de2
    Pair = 1
    Impair = 2
    choix_joueur_N = input( "Veuillez choisir entre \n 1 : Pair \n 2 : Impair \n")
    if choix_joueur_N == "1":
        print("Vous avez choisi Pair")
    elif choix_joueur_N == "2":
        print("Vous avez choisi Impair")
    else:
        print("Vous n'avez pas respecter les règles. Veuillez recommencer")
        Nain_Rouge()
    if choix_joueur_N == "1" and de_total % 2 == 0:
        print("Vous avez gagné")
        Bonus_Nain_Rouge()
    elif choix_joueur_N == "2" and de_total % 2 != 0:
        print("Vous avez gagné")
        Bonus_Nain_Rouge()
    else:
        print("Vous avez perdu")
        Malus_Nain_Rouge()

# Récompense positive liée au nain rouge


def Bonus_Nain_Rouge():
    Récompense_aléatoire = randint(1, 7)
    if Récompense_aléatoire == 1:
        print("Le fou pour vous récompenser vous offre un pigeon mort.")
    elif Récompense_aléatoire == 2:
        print(
            "Le fou pour vous récompenser vous amène des clandestin a enrôler dans l'armée.")
        Armee = Armee + 10
    elif Récompense_aléatoire == 3:
        print("Le fou pour vous amène une troupe de comédien qui attire des habitants dans votre roayaume.")
        peuple = peuple + 10
    elif Récompense_aléatoire == 4:
        print("Le fou pour vous remercier a demander au Pape de former des fidèle en votre nom.")
        religion = religion + 10
    elif Récompense_aléatoire == 5:
        print("Le fou pour vous remercier vous offre un bâton de la mort.")
    elif Récompense_aléatoire == 6:
        print("Le fou commence a pleurer. Et s'enfuit avec un cri de dommage.")
    elif Récompense_aléatoire == 7:
        print("Le fou pour vous remercier vous offre un bout de diamant qu'il a trouver dans un trou.")
        economie = economie + 10

# Récompense négative liée au nain rouge


def Malus_Nain_Rouge():
    Malus_aléatoire = randint(1, 7)
    if Malus_aléatoire == 1:
        print("Le fou pour vous récompenser d'avoir perdu vous donne un pigeon mort.")
    elif Malus_aléatoire == 2:
        print("Le fou pour vous récompenser d'avoir perdu chasse des clandestin de votre royaume.")
        Armee = Armee - 10
    elif Malus_aléatoire == 3:
        print("Le fou pour vous récompenser d'avoir perdu vous donne une mauvaise troupe de comédien qui fous fuir les habitants du royaume.")
        peuple = peuple - 10
    elif Malus_aléatoire == 4:
        print("Le fou pour vous récompenser d'avoir perdu a demander au Pape de renvoyer des fidèle en votre nom.")
        religion = religion - 10
    elif Malus_aléatoire == 5:
        print("Le fou pour vous récompenser d'avoir perdu se moque de vous et s'enfuit avec votre tapis rouge.")
    elif Malus_aléatoire == 6:
        print("Le fou est pris d'une crise de joie et saute dans tout les sens.")
    elif Malus_aléatoire == 7:
        print("Le fou ayant gagner exige de vous que vous le payez.")
        economie = economie - 10


# On début le jeu !

#OBJECTIF DE LA PROCHAINE SESSION DE CODE :
# 1. Faire un système de récompense(Bonus/Malus) aléatoire pour le combat
# 2. Appliquer les bonne couleur a chaque partie du code + prendre l'habitude de ne pas les oublier.
# 3. Réfléchir a un système de sauvegarde pour le jeu. ( Reprendre a l'évènement près + garder les stats)
# 4. Mettre en place les premier évènement du jeu.
# 5. Toujours continuer a s'amuser a refaire se projet en mieux !

