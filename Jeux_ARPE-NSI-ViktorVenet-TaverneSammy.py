#On ajoute les "import"
from math import *
from random import *
from colorama import *
#On met en place des couleurs ou changements de texte pour rendre plus lisible

#print(f"This is {Fore.GREEN} JOHN CENA {Style.RESET_ALL} !!!") Méthode qui sera utilisée dans le code
class color:                                                   
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   SOULIGNE = '\033[4m'
   ITALIQUE = '\033[3m'
 #test
#On présente un peu le jeu en mettant dans le contexte le joueur

hour =int(input("Ici seigneur. Je suis là. Mon seigneur, vous m'entendez ?! SEIGNEUR !!! Dîtes moi combien d'heures pensez-vous avoir dormi ?"))
print("Bienvenue, mon seigneur, vous venez en rélaité de vous réveiller d'un sommeil de ...")
print(hour * 9,"heures.")
user = input("Rassurez moi, vous n'êtes pas sonné, vous rappelez vous au moins de votre prénom. Dîtes-le moi.")
print("Merci Bon Dieu !Bienvenue à vous, Seigneur ", user,".")
start = input("Maintenant que vous êtes prêt, nous allons régler les problèmes de votre peuple. Etes-vous prêt ?")
if start == 'oui' :
    print("Allons-y !")
elif start == 'non' :
    print("Vous avez été mis à éxécution par votre peuple...\n C'est dommage de se rendormir seulement après s'être réveillé.")
else :
    print("Répondez-moi par oui ou par non, mon Seigneur, redîtes-moi tout !")
    break
    

#On crée les variables pour les objets et autres


tour = 0
objet = 0
armee = 50
religion = 50
peuple = 50
economie = 50
armee2 = armee / 5
religion2 = religion / 5
peuple2 = peuple / 5
economie2 = economie / 5
vie = 1
#Variables dédiées à l'un des systèmes de combat
j1pvmax = 100 * tour
j1lv = 5 * tour
j1attack = 50 * tour
j1def = 30 * tour
j2pvmax = 100 * hour
j2lv = 5 * hour
j2attack = 60 * hour
j2def = 50 * hour


#On crée les def pour raccourcir un peu le code

def combatmonstre() :
    j1pvmax = 100 * tour
    j1lv = 5 * tour
    j1attack = 50 * tour
    j1def = 30 * tour
    j2pvmax = 100 * hour
    j2lv = 5 * hour
    j2attack = 60 * hour
    j2def = 50 * hour
    while j1pvmax > 0 or j2pvmax > 0 : 
        print("PV de Seigneur", user,": ", j1pvmax)
        print("PV du Monstre: ", j2pvmax)
        print()
 
        print("Seigneur", user," attaque le Monstre !")
        print()
        print("Le Monstre perd", (((j1lv*0.4+2)*j1attack)/j2def*50)/10, "PV !")
    
        j2pvmax = j2pvmax - ((((j1lv*0.4+2)*j1attack)/j2def*50)/10)
        
        print("PV de Seigneur", user,": ", j1pvmax)
        print("PV du Monstre: ", j2pvmax)
        print()
 
        print("Seigneur", user," attaque le Monstre !")
        print()
        print("Seigneur", user," perd", (((j2lv*0.4+2)*j2attack)/j1def*50)/10, "PV !")
    
        j2pvmax = j2pvmax - (((j2lv*0.4+2)*j2attack)/j1def*50)/10
    
        if j1pvmax <= 0 :
            print("Le Seigneur fut vaincu...")
            vie = vie - 1
            break
        elif j2pvmax <= 0 :
            print("Le Seigneur a vaincu ce monstre !")
            break
            
            
def combatgeneral() :
    j1pvmax = 100 * tour
    j1lv = 5 * tour
    j1attack = 50 * tour
    j1def = 30 * tour
    j2pvmax = 100 * hour
    j2lv = 5 * hour
    j2attack = 50 * hour
    j2def = 30 * hour
    while j1pvmax > 0 or j2pvmax > 0 : 
        print("PV de Seigneur", user,": ", j1pvmax)
        print("PV du Général Legrand: ", j2pvmax)
        print()
 
        print("Seigneur", user," attaque le Général Legrand !")
        print()
        print("Le Général Legrand perd", (((j1lv*0.4+2)*j1attack)/j2def*50)/10, "PV !")
    
        j2pvmax = j2pvmax - ((((j1lv*0.4+2)*j1attack)/j2def*50)/10)
        
        print("PV de Seigneur", user,": ", j1pvmax)
        print("PV du Général Legrand: ", j2pvmax)
        print()
 
        print("Seigneur", user," attaque le Général Legrand !")
        print()
        print("Seigneur", user," perd", (((j2lv*0.4+2)*j2attack)/j1def*50)/10, "PV !")
    
        j2pvmax = j2pvmax - (((j2lv*0.4+2)*j2attack)/j1def*50)/10
    
        if j1pvmax <= 0 :
            print("Le Seigneur", user,"a gagné cet entraînement !")
            break
            
        elif j2pvmax <= 0 :
            print("Le Général Legrand a gagné cet entraînement !")
            break
            



#On crée les conditions de fin de partie


while (armee != 0 or 100) or (religion != 0 or 100) or (peuple != 0 or 100) or (economie != 0 or 100) or (vie != 0) :
    if armee <= 0 :
        print("Vous n'avez plus aucun soldat et les autres royaumes se disputent le vôtre.")
        print("FIN DE LA PARTIE \n \n Vous avez survécu",tour,"tours et vous avez trouvé", objet," objets.")
        print("\n Statistiques de la partie :\n Armée :", armee,"\n Religion :", religion,"\n Peuple :", peuple,"\n Economie :", economie,"\n")
        break
    elif armee >= 100 :
        print("L'armée vous chasse et prend votre place.")
        print("FIN DE LA PARTIE \n \n Vous avez survécu",tour,"tours et vous avez trouvé", objet," objets.")
        print("\n Statistiques de la partie :\n Armée :", armee,"\n Religion :", religion,"\n Peuple :", peuple,"\n Economie :", economie,"\n")
        break
    elif religion <= 0 :
        print("Votre peuple ne croit plus en rien.")
        print("FIN DE LA PARTIE \n \n Vous avez survécu",tour,"tours et vous avez trouvé", objet," objets.")
        print("\n Statistiques de la partie :\n Armée :", armee,"\n Religion :", religion,"\n Peuple :", peuple,"\n Economie :", economie,"\n")
        break
    elif religion >= 100 :
        print("L'évêque Antoine Malbonne vous chasse du pouvoir et prend votre place.")
        print("FIN DE LA PARTIE \n \n Vous avez survécu",tour,"tours et vous avez trouvé", objet," objets.")
        print("\n Statistiques de la partie :\n Armée :", armee,"\n Religion :", religion,"\n Peuple :", peuple,"\n Economie :", economie,"\n")
        break
    elif peuple <= 0 :
        print("Vous n'avez plus aucun habitant, vous perdez votre pouvoir.")
        print("FIN DE LA PARTIE \n \n Vous avez survécu",tour,"tours et vous avez trouvé", objet," objets.")
        print("\n Statistiques de la partie :\n Armée :", armee,"\n Religion :", religion,"\n Peuple :", peuple,"\n Economie :", economie,"\n")
        break
    elif peuple >= 100 :
        print("Le peuple décide d'une révolte et vous chasse.")
        print("FIN DE LA PARTIE \n \n Vous avez survécu",tour,"tours et vous avez trouvé", objet," objets.")
        print("\n Statistiques de la partie :\n Armée :", armee,"\n Religion :", religion,"\n Peuple :", peuple,"\n Economie :", economie,"\n")
        break
    elif economie <= 0 :
        print("Le peuple prend le pouvoir suite à une Révolution.")
        print("FIN DE LA PARTIE \n \n Vous avez survécu",tour,"tours et vous avez trouvé", objet," objets.")
        print("\n Statistiques de la partie :\n Armée :", armee,"\n Religion :", religion,"\n Peuple :", peuple,"\n Economie :", economie,"\n")
        break
    elif economie >= 100 :
        print("Vous mourrez étouffé suite à un buffet organisé.")
        print("FIN DE LA PARTIE \n \n Vous avez survécu",tour,"tours et vous avez trouvé", objet," objets.")
        print("\n Statistiques de la partie :\n Armée :", armee,"\n Religion :", religion,"\n Peuple :", peuple,"\n Economie :", economie,"\n")
        break
    elif vie <= 0 :
        print("Vous mourrez, fin de la partie !")
        print("FIN DE LA PARTIE \n \n Vous avez survécu",tour,"tours et vous avez trouvé", objet," objets.")
        print("\n Statistiques de la partie :\n Armée :", armee,"\n Religion :", religion,"\n Peuple :", peuple,"\n Economie :", economie,"\n")
        break
    event = randint(1,54)
    tour = tour + 1

#On écrit tous les évènements pour qui forment le jeu   


    if event == 1:
        print(f"Le chambellan {Fore.YELLOW} Salur Maloth {Style.RESET_ALL} vous informe qu'un monstre effraye votre village.")
        choix1 = input("Voulez-vous y aller ?")
        if choix1 == 'oui':
            print(f" {Fore.RED} 20 000 {Style.RESET_ALL} de vos habitants se transforme en armée. Malheurseusement, {Fore.RED} 30 000 {Style.RESET_ALL} de votre armée tombe dans un ravin.")
            peuple = peuple - 20
            armee = armee + 20
            armee = 30
        elif choix1 == 'non' :
            print(f"Votre armée se démotive et vous perdez {Fore.RED} 5000 {Style.RESET_ALL} soldats.")
            armee = armee - 5


    if event == 2 :
        print(f"Le barde {Fore.YELLOW} Guillaume Apologie {Style.RESET_ALL} vous signale que votre armée souhaite avoir un hymne.")
        choix2 = input("Voulez-vous créer un hymne ?")
        if choix2 == 'oui' :
            print(f"Votre armée est contente, vous gagnez {Fore.GREEN} 5000 {Style.RESET_ALL} soldats.")
            armee = armee + 5
            print(f"L'Eglise trouve cet hymne blasphématoire, vous perdez {Fore.RED} 5000 {Style.RESET_ALL} en religion.")
            religion = religion - 5
            print(f"Votre peuple aime l'hymne, vous gagnez {Fore.GREEN} 5000 {Style.RESET_ALL} habitants.")
            peuple = peuple + 5
            print(f"Vous payez le barde, vous le payez {Fore.RED} 5000 {Style.RESET_ALL} francs.")
            economie = economie + 5
        elif choix2 == 'non' :
            print(f"Votre armée est déçue, vous perdez {Fore.RED} 5000 {Style.RESET_ALL} soldats.")
        
        
    if event == 3 :
 
        COUP = ("Scorpio", "Pisces", "Capricorn","Taurus","Gemini")
  
        print("\n-------------------------")
        print("Les batailles du Zodiaque")
        print("-------------------------\n")
 
        a = int(input("Choisissez un membre du Zodiaque:\n0: Scorpio\n1: Pisces\n2: Capricorn\n3: Taurus\n4: Gemini\n->"))
        b = choice(range(5))
 
        print("\n{} VS {}".format(COUP[a], COUP[b]))
        if a == b:
            print("Égalité\n")
        elif (a>b and b+1==a) or (a<b and a+b==2):
            print("Vous gagnez contre les dieux !")
        else:
            vie = vie - vie


    if event == 4 :
        choix4 = input(f"Votre fou {Fore.YELLOW} Cicéron Languependu {Style.RESET_ALL} vous propose de faire une petite partie de dés, histoire de s'amuser.\n Voulez vous jouer ?")
        if choix4 == 'oui':
            print(f"Le but est simple : vous devez obtenir 2 dés pairs pour remporter une petite somme. \n A l'inverse, vous me devrez quelque chose.")
            de1 = randint(1,6)
            de2 = randint(1,6)
            print(f"Dés lancés :",de1," et ",de2)
            if de1 % 2 == 0 and de2 % 2 == 0 :
                print(f"Vous gagnez {Fore.GREEN} 15 000 {Style.RESET_ALL} francs.")
                economie = economie + 15
            else :
                print(f"Vous donnez {Fore.RED} 15 000 {Style.RESET_ALL} francs à votre fou.")
                economie = economie - 15
        elif choix4 == 'non':
            print(f"Votre fou ne vous en veut pas, il est même déjà reparti au Lac.")
            
            
    if event == 5:
        print(f"L'agriculteur {Fore.YELLOW} Benjamin Bylton {Style.RESET_ALL}: On a laissé périmer du lait et ça nous a donné du lait solide. Ça sent mauvais mais ça a bon goût. Pouvons-nous en vendre ?")
        choix5 = input(f"\n Acceptez-vous que les agriculteurs en vendent ?")
        if choix5 == 'oui':
            print(f"Félicitations, vous avez créé le fromage. Votre peuple l'adore. {Fore.GREEN} 5000 {Style.RESET_ALL} habitants ont rejoint votre royaume pour cette découverte.")
            print(f"Votre armée bénéficie du fromage dans leur ration et ils sont contents. {Fore.GREEN} 5000 {Style.RESET_ALL} soldats intègrent votre armée.")
            armee = armee + 5
            peuple = peuple + 5
        elif choix5 == 'non' :
            print(f"Les agriculteurs sont déçus de ne pas vendre le lait périmé.{Fore.RED} 5000 {Style.RESET_ALL} agriculteurs font grêve. Votre économie en prend un coup puisque le lait entre en pénurie sur le marché :{Fore.RED}10 000{Style.RESET_ALL} francs en moins !")
            peuple = peuple - 5
            economie = economie - 10
            
            
    if event == 6:
        print(f"L'agriculteur {Fore.YELLOW} Benjamin Bylton {Style.RESET_ALL} : La récolte a été mauvaise cette année, Seigneur", user,"...")
        choix6 = input(f"Que voulez-vous faire ?\n 1 : Doubler le prix du pain \n 2 : Adapter le prix du pain justement \n")
        if choix6 == 'doubler':
            print(f"Vous avez doublé le prix du pain. Votre peuple est mécontent : {Fore.RED} 10 000 {Style.RESET_ALL} mais vous engendrez pas mal de profil :{Fore.GREEN}10 000{Style.RESET_ALL} francs en tout.")
            peuple = peuple - 10
            economie = economie + 10
        elif choix6 == 'adapter' :
            print(f"Vous avez choisi d'adapter le prix du pain mais votre peuple est mécontent :{Fore.RED}5 000{Style.RESET_ALL}.")
            peuple = peuple - 5
            
            
    if event == 7:
        print(f"L'agriculteur {Fore.YELLOW} Benjamin Bylton {Style.RESET_ALL} : Les pays d'Orient ont inventé une technique d'agriculture plus rentable.")
        choix7 = input("Pouvons-nous l'utiliser ?")
        if choix7 == 'oui':
            print(f"Grâce aux nouvelles méthodes d'agriculture, le rendement a été amélioré. Votre économie se porte mieux grâce à elle : {Fore.GREEN}15 000{Style.RESET_ALL}. Les agriculteurs ont moins de travail et vous remercie. {Fore.GREEN}5000{Style.RESET_ALL} agriculteurs arrivent dans votre royaume. Cependant, cette nouvelle technique vous a demandé un financement qui équivaut à {Fore.RED}5 000{Style.RESET_ALL} francs.")
            economie = economie + 15
            economie = economie - 5
            peuple = peuple + 5
        elif choix7 == 'non' :
            print(f"Vos agriculteurs sont déçus de vos choix traditionels : {Fore.RED} 5000 {Style.RESET_ALL} agriculteurs font grève.")
            peuple = peuple - 5
            
            
    if event == 8 :
        print(f"L'agriculteur {Fore.YELLOW} Benjamin Bylton {Style.RESET_ALL} : la récolte est excellente cette année, Seigneur", user,"!")
        choix8 = input("Voulez-vous augmenter le prix du pain ?")
        if choix8 == 'oui':
            print(f"Votre peuple ne pourra pas manger autant de pain : {Fore.RED} 5000 {Style.RESET_ALL} habitants sont mécontents.")
            peuple = peuple - 5
        elif choix8 == 'non' :
            print(f"Votre peuple est content. Ils pourront manger du pain. Vous gagnez {Fore.GREEN} 5000 {Style.RESET_ALL} habitants.")
            peuple = peuple + 5
            
            
    if event == 9:
        print(f"Le Général {Fore.YELLOW} Baldur Legrand {Style.RESET_ALL} : Votre armée est faible ! Qu'allez vous faire ?")
        choix9 = input(f"Voulez vous enrôler le peuple ?\n 1 : Oui \n 2 : Non \n")
        if choix9 == 'oui':
            print(f"Vous avez décidé d'enrôler votre peuple qui est réduit de {Fore.RED} 10 000 {Style.RESET_ALL} habitants, devenant désormais vos soldats.")
            peuple = peuple - 10
            armee = armee + 10
        elif choix9 == 'non' :
            print(f"Vous ne recrutez aucun soldat, votre armée est surpassée par les évènements : {Fore.RED} -5 000 {Style.RESET_ALL} .")
            armee = armee - 5
            
            
    if event == 10:
        print(f"L'évêque {Fore.YELLOW} Antoine Malbonne {Style.RESET_ALL} : La basilique Saint Pierre menace de s'effondrer. Aidez-nous à la reconstruire Seigneur",user," !")
        choix10 = input(f"Voulez-vous aider à sa restitution ?")
        if choix10 == 'oui':
            print(f"Vous aidez à la restitution de la basilique Saint Pierre. L'Eglise vous remercie : {Fore.GREEN} 10 000 {Style.RESET_ALL} . Votre peuple est content de cet édifice reconstitué :{Fore.GREEN}5 000{Style.RESET_ALL}. Mais ça vous a coûté {Fore.RED} 10 000 {Style.RESET_ALL} francs.")
            peuple = peuple + 5
            economie = economie - 10
            religion = religion + 10
        elif choix10 == 'non' :
           print(f"Vous n'aidez pas à restituer la basilique Saint-Pierre.L'Eglise est déçue : {Fore.RED} 15 000 {Style.RESET_ALL} .")
           religion = religion - 15
           
           
    if event == 11:
        print(f"La bonne soeur {Fore.YELLOW} Marie Delfriche {Style.RESET_ALL} : Seigneur",user,", un incendie est en train de ravager votre château !")
        choix11 = input(f"Voulez-vous sauver votre armée ou votre argent ?")
        if choix11 == 'armée':
            print(f"Vous perdez {Fore.RED} 10 000 {Style.RESET_ALL} francs. Vous perdez aussi {Fore.RED} 5000 {Style.RESET_ALL} habitants, mais l'Eglise organise une cérémonie est amène {Fore.GREEN} 10 000 {Style.RESET_ALL} religieux.")
            economie = economie - 10
            peuple = peuple - 5
            religion = religion + 10
        elif choix11 == 'argent' :
            print(f"Votre peuple est mécontent et vous perdez {Fore.RED} 10 000 {Style.RESET_ALL} habitants. Votre armée subit des perte à cause des flammes. En tout, {Fore.RED} 5000 {Style.RESET_ALL} soldats trépassent. Cependant l'Eglise organise une cérémonie est amène {Fore.GREEN} 10 000 {Style.RESET_ALL} religieux.")
            peuple = peuple - 10
            armee = armee - 5
            religion = religion + 10
            
            
    if event == 12:
        print(f"Le bourreau {Fore.YELLOW} Bourg Palette {Style.RESET_ALL} : Les prisonniers se sont échappés !")
        choix12 = input(f"Organiser une battue ?")
        if choix12 == 'oui':
            print(f"Vous organisez une battue, votre armée est contente de participer : {Fore.GREEN} 5 000 {Style.RESET_ALL} . Mais votre peuple a peur {Fore.RED} -5 000 {Style.RESET_ALL} .")
            peuple = peuple - 5
            armee = armee + 5
        elif choix12 == 'non' :
            print(f"Vous n'organisez pas de battue. Le peuple a très peur des prisonniers : {Fore.RED}10 000{Style.RESET_ALL}. De plus, votre armée s'ennuie :{Fore.RED}-5 000{Style.RESET_ALL}. Mais vous n'avez pas à payer l'armée :{Fore.GREEN}5 000{Style.RESET_ALL} francs.")
            armee = armee - 5
            peuple = peuple - 10
            economie = economie + 5


    if event == 13:
        print(f"Le bourreau {Fore.YELLOW} Bourg Palette {Style.RESET_ALL} : nous pourrions créer un musée de l'humain avec tous les prisonniers exécutés, je pourrais m'en occuper les jours fériés !")
        choix13 = input(f"Voulez vous créer un musée sur les corps et organes des éxécutés ?")
        if choix13 == 'oui':
            print(f"Votre peuple est dégoûté mais aime l'initiative {Fore.GREEN} 5000 {Style.RESET_ALL} . Votre économie se porte bien puisque vous faîtes payez les places au prix fort: {Fore.GREEN} 10 000 {Style.RESET_ALL} francs en plus ! Cependant, l'Eglise n'approuve pas se choix : {Fore.RED} 5000 {Style.RESET_ALL} religieux parte pour l'Italie.")
            economie = economie + 10
            peuple = peuple - 5
            religion = religion - 5
        elif choix13 == 'non' :
            print(f"Votre bourreau est déçu. L'armée et l'Eglise approuvent votre choix : {Fore.GREEN} 5000 {Style.RESET_ALL} religieux et soldats vous rejoignent.")
            armee = armee - 5
            religion = religion + 5
            
            
    if event == 14:
        print(f"Le bourreau {Fore.YELLOW} Bourg Palette {Style.RESET_ALL} : il y a trop de condamnations à mort. J'ai besoin de l'aide de l'armée.")
        choix14 = input(f"Voulez-vous impliquer votre armée pour les condamnations à mort ?")
        if choix14 == 'oui':
            print(f"Les condamnations à mort se portent plus fluidement mais cela réduit l'effectif de votre armée de {Fore.RED} 5000 {Style.RESET_ALL} soldats. De plus, la religion n'aime pas que l'on change les tendances par rapport au condamnations à mort : {Fore.RED} -5000 {Fore.RESET_ALL} .")
            armee = armee - 5
            religion = religion - 5
        elif choix14 == 'non' :
            print(f"Votre armée vous remercie de ne pas devoir faire tâche ingrate : {Fore.GREEN} +5000 {Style.RESET_ALL} . Mais le peuple a peur des criminels qui ne sont pas punis en temps et en heure : {Fore.RED} -5000 {Style.RESET_ALL} .")
            armee = armee + 5
            peuple = peuple - 5
        
    
    if event == 15:
        print(f"Le chambellan {Fore.YELLOW} Salur Maloth {Style.RESET_ALL} : vous devriez éduquer le peuple, ça améliorera le commerce et les capacités de votre peuple.")
        choix15 = input(f"Voulez-vous éduquez le peuple ?")
        if choix15 == 'oui':
            print(f"Vous avez choisi d'éduquer le peuple et cela vous coûte cher mais ils deviennent plus compétents et les marchands arrivent à vendre d'avantage de marchandises à l'étranger : {Fore.RED} 5000 {Style.RESET_ALL} franc en moins. Cependant L'Eglise n'aime pas votre choix car ils ont plus du mal à contrôler les pensées du peuple : {Fore.RED}5000{Style.RESET_ALL} . Votre peuple vous remercie grandement pour cette éducation, {Fore.GREEN} 5000 {Style.RESET_ALL} habitants viennent dans votre royaume.")
            peuple = peuple + 5
            religion = religion - 5
            economie = economie - 5
        elif choix15 == 'non' :
            print(f"Vous n'investissez pas dans l'éducation et l'Eglise vous en remercie : {Fore.GREEN} 10 000 {Style.RESET_ALL} . Mais votre peuple est déçu de votre choix : {Fore.RED} 5 000 {Style.RESET_ALL} .")
            peuple = peuple - 5
            religion = religion + 10
        
        
    if event == 16:
        print(f"Le chambellan {Fore.YELLOW} Salur Maloth {Style.RESET_ALL} : votre peuple se plaint des puanteurs de votre royaume.")
        choix16 = input(f"Voulez-vous construire un réseau d'égoût ?")
        if choix16 == 'oui':
            print(f"Vous construisez un réseau d'égoût, votre peuple vous remercie : {Fore.GREEN} +10 000 {Style.RESET_ALL} . Mais le réseau vous a coûté {Fore.RED} 10 000 {Style.RESET_ALL} francs.")
            peuple = peuple + 10
            economie = economie - 10
        elif choix16 == 'non' :
            print(f"Vous ne construisez pas de réseau d'égoût, votre peuple est mécontent : {Fore.RED} -10 000 {Style.RESET_ALL} et votre armée doit gérer les révoltes : {Fore.RED} -5 000 {Style.RESET_ALL} .")
            armee = armee - 5
            peuple = peuple - 10
        
        
    if event == 17:
        print(f" Le chambellan {Fore.YELLOW} Salur Maloth {Style.RESET_ALL} : La princesse du Nord souhaite vous épouser.")
        choix17 = input(f"Voulez-vous faire ?\n 1 : Epouser la princesse du Nord \n 2 : Ne pas épouser la princesse du Nord \n")
        if choix17 == 1 :
            print(f"Vous épousez la princesse du Nord. Tous les instituts aiment ce choix, que ce soit la religion, le peuple, l'économie ou encore l'armée : {Fore.GREEN} +5 000 {Style.RESET_ALL} .")
            peuple = peuple + 5
            religion = religion + 5
            armee = armee + 5
            economie = economie + 5
        elif choix17 == 2 :
            print(f"Vous refusez d'épouser la princesse du Nord. Tous les instituts détestent ce choix, que ce soit la religion, le peuple, l'économie ou encore l'armée : {Fore.GREEN} +5 000 {Style.RESET_ALL} .")
            peuple = peuple - 5
            religion = religion - 5
            armee = armee - 5
            economie = economie - 5
        
        
    if event == 18:
        print(f"Le chambellan {Fore.YELLOW} Salur Maloth {Style.RESET_ALL} : une femme a lancée une rumeur sur le fait qu'elle est la mère de votre enfant. Si vous le reconnaisez, vous devriez lui verser une pension.")
        choix18 = input(f"Que voulez-vous faire ?\n 1 : Exécutez là ! \n 2 : Laissez cette folle ! \n")
        if choix18 == 1:
            print(f"Vous avez décidé d'exécuter la femme qui a lancé la rumeur. Elle est exécutée discrètement et personne ne remarque de changements.")
        elif choix18 == 2 :
            print(f"Vous laissez crier la femme et le peuple en a marre du bruit : {Fore.RED} -5 000 {Style.RESET_ALL} .")
            peuple = peuple - 5
        
        
    if event == 19:
        print(f"Le chambellan {Fore.YELLOW} Salur Maloth {Style.RESET_ALL} : nous devrions suivre la route de la soie. Cela améliorerait nos commerces extérieurs. Cependant, vous devrez payer une taxe au royaume de l'Est.")
        choix19 = input(f"Voulez-vous rejoindre la route de la soie ?")
        if choix19 == 'oui':
            print(f"Vous construisez la route de la soie et malgré la taxe, les affaires ne se sont jamais aussi bien portées : {Fore.GREEN} 15 000 {Style.RESET_ALL} francs gagnés.")
            economie = economie + 15
        elif choix19 == 'non' :
            print(f"Vous ne construisez pas votre partie de la route de la soie, votre commerce est ralenti puisque les autre pays ont fait le choix de la construire : {Fore.RED} 10 000 {Style.RESET_ALL} francs en moins.")
            economie = economie - 10
        
        
    if event == 20:
        print(f"Le chambellan {Fore.YELLOW} Salur Maloth {Style.RESET_ALL} : le royaume du Nord est en guerre, leur peuple entre dans nos frontières en ce moment même. Que devons-nous faire ?")
        choix20 = input(f"Voulez-vous accepter ou refuser les immigrés du royaume du Nord ?")
        if choix20 == 'accepter' :
            print(f"Vous avez accepté les immigrés du royaume dans votre royaume et ils vous en remercient en vous payant une taxe de {Fore.GREEN} 5000 {Style.RESET_ALL} francs et votre peuple est heureux de vos décisions diplomatiques : {Fore.GREEN} +5000 {Style.RESET_ALL} .")
            peuple = peuple + 5
            economie = economie + 5
        elif choix20 == 'refuser' :
            print(f"Vous avez refusé les immigrés du royaume du Nord et ils entrent en tension avec vous. De plus, votre peuple est mécontent : {Fore.RED} 5000 {Style.RESET_ALL} .")
            peuple = peuple - 5
        
        
    if event == 21:
        print(f"Le chambellan {Fore.YELLOW} Salur Maloth {Style.RESET_ALL} : un tremblement de terre a touché votre royaume. Votre trésorerie sera sans garde si vous aidez le peuple.")
        choix21 = input(f"Voulez-vous sauver votre argent ou le peuple ?")
        if choix21 == 'argent':
            print(f"Vous sauvez votre trésorerie, votre peuple est en danger : {Fore.RED} -10 000 {Style.RESET_ALL} . Votre armée subit des pertes en protégeant votre trésor : {Fore.RED} -5000 {Style.RESET_ALL} soldats sont bléssés. Quant à elle , l'Eglise en subit les conséquences avec vous : {Fore.RED} 5 000 {Style.RESET_ALL} .")
            peuple = peuple - 10
            armee = armee - 5
            religion = religion -5
        elif choix21 == 'peuple' :
            print(f"Votre peuple est sauvé malgré de lourdes pertes : {Fore.RED} -5000 {Style.RESET_ALL} . Votre trésor se fait piller, vous perdez {Fore.RED} 10 000 {Style.RESET_ALL} francs. L'Eglise apprécie que le peuple passe avant votre argent : {Fore.GREEN} +5000 {Style.RESET_ALL} .")
            peuple = peuple - 5
            religion = religion + 5
            economie = economie + 10
        
        
    if event == 22:
        print(f"Le chambellan {Fore.YELLOW} Salur Maloth {Style.RESET_ALL} : des habitants de notre royaume incitent des enfants à cracher sur vos hommes, Seigneur", user,". Devrions-nous intervenir pour l'exemple ?")
        choix22 = input(f"Voulez-vous que l'armée intervienne  ?")
        if choix22 == 'oui':
            print(f"Vous faîtes intervenir l'armée. L'Eglise approuve votre choix : {Fore.GREEN} +5 000 {Style.RESET_ALL} mais le peuple trouve cela offensant : {Fore.RED} -5 000 {Style.RESET_ALL} .")
            religion = religion + 5
            peuple = peuple - 5
        elif choix22 == 'non' :
            print(f"Vous ne faîtes pas intervenir l'armée. Le peuple approuve votre calme {Fore.GREEN} +5 000 {Style.RESET_ALL} .")
            peuple + peuple + 5
        
        
    if event == 23:
        print(f"Le scientifique {Fore.YELLOW} Elon Monka {Style.RESET_ALL} : j'ai créé un système qui diffusera ce que vous voudrez dans votre royaume entier ! .")
        choix23 = input(f"Voulez-vous installez des hauts-parleurs dans votre royaume ?")
        if choix23 == 'oui':
            print(f"Vous avez installé des hauts-parleurs dans tout votre royaume, le peuple est content : {Fore.GREEN} +5 000 {Style.RESET_ALL} mais les religieux ont de mauvais présentiments :{Fore.RED} -10 000 {Style.RESET_ALL}.")
            peuple = peuple + 5
            religion = religion - 10
        elif choix23 == 'non' :
            print(f"Vous n'installez pas le système de hauts-parleurs, les religieux approuvent votre choix : {Fore.GREEN} +10 000 {Style.RESET_ALL} .")
            religion = religion + 10
        
        
    if event == 24:
        print(f"L'évêque {Fore.YELLOW} Antoine Malbonne {Style.RESET_ALL} : nous voulons construire une nouvelle église dans la capitale.")
        choix24 = input("Voulez-vous construire une nouvelle église dans la capitale ?")
        if choix24 == 'oui':
            print(f"Vous construisez une nouvelle église et cette église vous coûte {Fore.RED} 10 000 {Style.RESET_ALL} francs, mais le pouvoir de l'Eglise augmente de {Fore.GREEN} 10 000 {Style.RESET_ALL} religieux. Votre peuple est plus heureux que jamais : {Fore.GREEN} +5000 {Style.RESET_ALL} .")
            economie = economie - 10
            peuple = peuple + 5
            religion = religion + 10
        elif choix24 == 'non' :
            print(f"Vous ne construisez pas une nouvelle église donc l'évêque est mécontent : {Fore.RED} -5000 {Style.RESET_ALL} . Aussi, votre peuple est mécontent, l'Eglise les manipule pour vous faire passer pour un horrible seigneur : {Fore.RED} -5000 {Style.RESET_ALL} .")
            religion = religion - 5
            peuple = peuple - 5
        
        
    if event == 25:
        print(f"L'évêque {Fore.YELLOW} Antoine Malbonne {Style.RESET_ALL} : nous devrions créer un pèlerinage jusqu'à la tombe du Saint Viktor.")
        choix25 = input("Acceptez-vous le pèlerinage ?")
        if choix25 == 'oui':
            print(f"Vous acceptez le pèlerinage jusqu'à la tombe du Saint Viktor, L'Eglise vous remercie : {Fore.GREEN} +5 000 {Style.RESET_ALL} et le peuple approuve votre choix : {Fore.RED} +5000 {Style.RESET_ALL} mais vous financez le projet à hauteur de {Fore.RED} 5 000 {Style.RESET_ALL} francs.")
            religion = religion + 5
            economie = economie - 5
            peuple = peuple + 5
        elif choix25 == 'non' :
            print(f"Vous refusez le pèlerinage jusqu'à la tombe du Saint Viktor. L'Eglise vous en veut de votre choix : {Fore.RED} -5 000 {Style.RESET_ALL} et votre peuple en pense de même : {Fore.RED} -5 000 {Style.RESET_ALL} . L'armée approuve vos choix : {Fore.GREEN} +5 000 {Style.RESET_ALL} .")
            religion = religion -5
            peuple = peuple - 5
            armee = armee + 5
        
        
    if event == 26:
        print(f"L'évêque {Fore.YELLOW} Antoine Malbonne {Style.RESET_ALL} : donnez-nous assez de pouvoir pour faire respecter les lois du très haut. Le Pape est prêt à payer le prix !")
        choix26 = input(f"Voulez-vous augmenter le pouvoir de l'Eglise ?")
        if choix26 == 'oui':
            print(f" {Fore.GREEN} 10 000 {Style.RESET_ALL} religieux vous rejoignent car vous accordez assez de puissance a l'Eglise pour qu'elle fasse respecter ses lois. De plus, le Pape vous paye une taxe pour ce service de {Fore.GREEN}10 000{Style.RESET_ALL} francs.")
            religion = religion + 10
            economie = economie + 10
        elif choix26 == 'non' :
            print(f" {Fore.RED} 10 000 {Style.RESET_ALL} relgieux partent dans d'autres royaumes car vous refusez d'accorder du pouvoir à l'Eglise, elle est très mécontente.")
            religion = religion - 10
        
        
    if event == 27:
        print(f"L'évêque {Fore.YELLOW} Antoine Malbonne {Style.RESET_ALL} : nous aimerions faire une messe en l'honneur de votre père.")
        choix27 = input(f"Voulez-vous organiser la messe ?")
        if choix27 == 'oui':
            print(f"L'Eglise affirme sa position : {Fore.Green} 10 000 {Style.RESET_ALL}, et le peuple en est ravie : {Fore.GREEN} 5000 {Style.RESET_ALL} habitants font la fête, mais l'Eglise n'a pas précisé que la messe est organisée à vos frais : {Fore.RED} -5 000 {Style.RESET_ALL} ")
            economie = economie - 5
            peuple = peuple +5
            religion = religion + 10
        elif choix27 == 'non' :
            print(f"L'Eglise est déçue de ne pas pouvoir fêter cette messe : {Fore.RED} -10 000 {Style.RESET_ALL} . Le peuple est déçu qu'une cérémonie au nom du père de leur illustre Seigneur n'ait pas lieu : {Fore.RED} 5 000 {Style.RESET_ALL} habitants déçus.")
            peuple = peuple - 5
            religion = religion - 10
        
        
    if event == 28:
        print(f"Le Général {Fore.YELLOW} Baldur Legrand {Style.RESET_ALL} : une de nos patrouille s'est  faite attaquée par le peuple de l'Est")
        choix28 = input(f"Que voulez vous faire ?\n 1 : Envoyez un diplomate \n 2 : Envoyez l'armée \n")
        if choix28 == 1 :
            print(f"Vous avez réussi à éviter une guerre. Votre peuple est heureux : {Fore.GREEN} +10 000 {Style.RESET_ALL} .")
        elif choix28 == 2 :
            print(f"Certains de vos soldats sont morts pendant l'attaque mais vous avez réussi à venger vos {Fore.RED} 15 000 {Style.RESET_ALL} soldats morts.")


    if event == 29:
        print(f"Le Général {Fore.YELLOW} Baldur Legrand {Style.RESET_ALL} : vos forteresses sont en ruine Seigneur", user,". Nous avons besoin d'en construire de nouvelles.")
        choix29 = input(f"Voulez-vous construire de nouvelles forteresses ?")
        if choix29 == 'oui':
            print(f"Vous décidez de construire une nouvelle forteresse, votre armée vous remercie : {Fore.GREEN} +10 000 {Style.RESET-ALL} . Cependant, ces protection vous ont coûté des millions de Yuan, soit près de {Fore.RED} 10 000 {Style.RESET_ALL} francs.")
            economie = economie - 10
            armee = armee + 10
        elif choix29 == 'non' :
            print(f"Vous ne construisez pas de nouvelles forteresses, vos soldats sont déçus : {Fore.GREEN} +5 000 {Style.RESET_ALL} .")
            armee = armee - 5
        
        
    if event == 30:
        print(f"Le Général {Fore.YELLOW} Baldur Legrand {Style.RESET_ALL} : cette année, il ne se passe rien, les soldats s'ennuient à mourrir.")
        choix30 = input(f"Voulez-vous ?\n 1 : Leur donner du pain et du vin \n 2 : A l'entraînement !\n")
        if choix30 == 1 :
            print(f"Vous nourrissez votre armée de pain et de vin, et ils vous remercient . Cependant, elle est plus faible que les autres, ce qui entraîne des pertes, {Fore.RED} 5 000 {Style.RESET_ALL} soldats exactement. Votre peuple a peur de la faiblesse de votre armée et préfère émigrer. Vous perdez {Fore.RED}5 000{Style.RESET_ALL} habitants. Votre économie en prend un coup puisque le vin coûte cher : {Fore.RED} 5000 {Style.RESET_ALL} francs en tout !")
            armee = armee - 5
            economie = economie - 5
            peuple = peuple - 5
        elif choix30 == 2 :
            print(f"Votre armée est contente de s'entraîner et devient plus forte qu'avant : {Fore.GREEN} +5 000 {Style.RESET_ALL} . Votre peuple se sent en sécurité : {Fore.GREEN} +5 000 {Style.RESET_ALL} .")
            armee = armee + 5
            peuple = peuple + 5
        
        
    if event == 31:
        print(f"Le Général {Fore.YELLOW} Baldur Legrand {Style.RESET_ALL} : vous devriez mettre un couvre-feu, les rues ne sont pas sûres la nuit, Seigneur", user,".")
        choix31 = input(f"Voulez-vous appliquer un couvre-feu ?")
        if choix31 == 'oui':
            print(f"Vous appliquer un couvre feu, votre peuple est rassuré : {Fore.GREEN} +5 000 {Style.RESET_ALL} . Cette manoeuvre facilite gradement les patrouilles des soldats : {Fore.GREEN} +5 000 {Style.RESET_ALL} .")
            peuple = peuple + 5
            armee = armee + 5
        elif choix31 == 'non' :
            print(f"Vous n'appliquez aucun couvre-feu. Votre peuple a peur : {Fore.RED} -5 000 {Style.RESET_ALL} . Votre armée est surpassée par les évènements : {Fore.RED} -5 000 {Style.RESET_ALL} .")
            armee = armee - 5
            peuple = peuple - 5
        
        
    if event == 32:
        print(f"Le fou {Fore.YELLOW} Cicéron Lenguepandu {Style.RESET_ALL} : Chaussssssuuuuureeeeeee !!!")
        choix32 = input(f"Comment voulez-vous réagir ?\n 1 : A mes pieds, fou ! \n 2 : *Un long soupir...* \n")
        if choix32 == 1:
            print(f"Votre fou vous obéit et vous regarde comme un chien et fait le beau.")
        elif choix32 == 2 :
            print(f"Vous soupirez longuement et votre fou s'en va en courant.")
        
        
    if event == 33:
        print(f"Une Femme au foyer {Fore.YELLOW} Louise trave {Style.RESET_ALL} : Je veux que les femmes soient mieux payées ! ")
        choix33 = input(f"Voulez-vous augmentee le salaire des femmes ?")
        if choix33 == 'oui':
            print(f"Vous payez une femme. Cela fait débat mais les femmes sont contentes : {Fore.GREEN} +5000 {Style.RESET_ALL} .")
            peuple = peuple + 5
        elif choix33 == 'non' :
            print(f"Votre choix fait débat, {Fore.RED}5 000{Style.RESET_ALL} femmes sont déçues. Mais votre armée est fière de vous voir refuser l'augmentation des femmes : {Fore.GREEN} +15 000 {Style.RESET_ALL} soldats sont fiers d'être dans votre armée.")
            armee = armee + 15
            peuple = peuple - 5
        
        
    if event == 34:
        print(f"Le chambellan {Fore.YELLOW} Malur Saloth {Style.RESET_ALL} il ne s'est rien passé cette année !")
        choix34 = input(f"Qu'en pensez-vous ?\n 1 : Euhhhh ... \n 2 : Bahhhh...")
        if choix34 == 1:
            print(f"Vraiment Rien !")
        elif choix34 == 2 :
            print(f"Vraiment rien !")
        
        
    if event == 35:
        print(f"Le fou {Fore.YELLOW} Cicéron Languependu {Style.RESET_ALL} : vous gouvernez comme un nul !")
        choix35 = input(f"Qu'en pensez-vous ?\n 1 : Euhhhh ... \n 2 : Bahhhh...")
        if choix35 == 1:
            print(f"Vous restez sans comprendre pendant qu'il court en rond devant vous.")
        elif choix35 == 2 :
            print(f"Vous restez sans comprendre pendant qu'il court en rond devant vous.")
        
        
    if event == 36:
        print(f"Le fou {Fore.YELLOW} Cicéron Languependu {Style.RESET_ALL} : Seigneur",user,", les éxécutions, elles sont à mourir d'ennui ! Vous devriez rajoutez des feux d'artifice ! et des jeux !")
        choix36 = input("Voulez-vous rendre les éxecutions plus 'amusantes'?")
        if choix36 == 'oui':
            print(f" {Fore.GREEN} 5000 {Style.RESET_ALL} habitants se questionnent sur votre choix mais adorent votre idée. Cette idée vous coûte énormement, {Fore.RED}5000{Style.RESET_ALL} francs en moins.")
            peuple = peuple + 5
            economie = economie - 5
        elif choix36 == 'non' :
            print(f"Aucun changement ne se fait ressentir. Votre fou n'est même pas déçu et rigole tout seul.")
        
        
    if event == 37:
        print(f"Le fou {Fore.YELLOW} Cicéron Languependu {Style.RESET_ALL} : vous savez qui est le monstre que tout le monde appelle Nestor ? ")
        choix37 = input(f"Le savez vous ? ?\n 1 : Euhhh non ...  \n 2 : Un dragon ?\n")
        if choix37 == 1:
            print(f"Le fou ne vous répond pas en s'en va en courant.")
        elif choix37 == 2 :
            print(f"Le fou ne vous répond pas en s'en va en courant.")
        
        
    if event == 38:
        print(f"Le messager {Fore.YELLOW} Alfred Postal {Style.RESET_ALL} : la reine du Nord m'envoie vous offrir 40 livres pour construire une bibliothèque.")
        choix38 = input(f"Voulez-vous fabriquer une bibliothèque à partir de ces 40 livres ?")
        if choix38 == 'oui' :
            print(f"Vous construisez une bibliothèque. Votre peuple est content de s'instruire : {Fore.GREEN} +5 000 {Style.RESET_ALL} .De plus, cela ne vous a rien coûté puisque la reine du Nord a financé le projet.")
            peuple = peuple + 5
        elif choix38 == 'non' :
            print(f"Vous ne construisez pas de bibliothèque, votre peuple est déçu {Fore.RED}5 000{Style.RESET_ALL}.")
            peuple = peuple - 5
        
        
    if event == 39:
        print(f"Le mineur {Fore.YELLOW} Steve Jaub {Style.RESET_ALL} : on en a marre de creuser un trou pour votre or ! Augmentez-nous !")
        choix39 = input(f"Voulez-vous augmenter le salaire des mineurs ? \n 1 : Augmenter leur salaire \n 2 : Ne pas augmenter leur salaire \n")
        if choix39 == 1:
            print(f"Vous augmentez un peu leur salaire, votre économie en prend un coup : {Fore.RED} -10 000 {Style.RESET_ALL} francs en tout mais les mineurs vous remercie : {Fore.GREEN} +5 000 {Style.RESET_ALL} .")
            peuple = peuple + 5
            economie = economie - 10
        elif choix39 == 2 :
            print(f"Vous n'augmentez pas le salaire des mineurs, votre économie en prend un coup à cause des grèves : {Fore.RED} -5 000 {Style.RESET_ALL} . Votre peuple est mécontent : {Fore.RED} -5 000 {Style.RESET_ALL} .")
            economie = economie -10 
            peuple = peuple - 5
        
        
    if event == 40:
        print(f"Le mineur {Fore.YELLOW} Steve Jaub {Style.RESET_ALL} : Seigneur", user," nous avons trouvé un gisement d'or !")
        choix40 = input(f"Que comptez-vous faire ?\n 1 : Partager l'or \n 2 : Garder l'or \n")
        if choix40 == 1 :
            print(f"Vous partagez l'or. Vous gagnez {Fore.GREEN} 10 000 {Style.RESET_ALL} francs grâce à l'or. De plus, vous augmentez le budget de votre armée : {Fore.GREEN} +5 000 {Style.RESET_ALL} et votre peuple est fier de vous : {Fore.GREEN} +5 000 {Style.RESET_ALL} .")
            economie = economie + 10
            peuple = peuple + 5
            armee = armee + 5
        elif choix40 == 2 :
            print(f"Vous gardez tout pour vous ! Votre économie augmente radicalement : {Fore.GREEN} +20 000 {Style.RESET_ALL} francs. Cependant, votre peuple est mécontent de vous voir vous enrichir toujours plus : {Fore.RED} -5 000 {Style.RESET_ALL} et votre armée attendait un budget supplémentaire : {Fore.RED} -5 000 {Style.RESET_ALL}.")
            economie = economie + 20
            peuple = peuple - 5
            armee = armee - 5
        
        
    if event == 41:
        print(f"Le chambellan {Fore.YELLOW} Salur Maloth {Style.RESET_ALL} : la rivière de l'Est est bloquée par les brigands.")
        choix41 = input(f"Que voulez-vous faire ?\n 1 : Soudoyer les brigands \n 2 : Envoyer l'armée \n")
        if choix41 == 1:
            print(f"Vous soudoyez les brigands, votre armée perd confiance en vous : {Fore.RED} -15 000 {Style.RESET_ALL} et vous payez les brigands une petit somme : {Fore.RED} 5 000 {Style.RESET_ALL} francs.")
            armee = armee - 15
            economie = economie - 5
        elif choix41 == 2 :
            print(f"Vous envoyez l'armée ! Lors de l'assaut, des soldats meurent sur le nombre de brigands : {Fore.RED} -5 000 {Style.RESET_ALL} .")
            armee = armee - 5        
        
    if event == 42:
        print(f"Le chambellan {Fore.YELLOW} Salur Maloth {Style.RESET_ALL} : le Seigneur du Sud souhaite former une alliance avec vous en construisant des murailles.")
        choix42 = input(f"Voulez-vous faire une alliance avec le Seigneur du Sud ?")
        if choix42 == 'oui':
            print(f"Vous acceptez de construire une murraille, vous facilitez le travail de votre armée et ils vous en remercient  : {Fore.GREEN} +10 000 {Style.RESET_ALL} . Cependant, les défenses ralentissent votre commerce extérieur : {Fore.RED} -5 000 {Style.RESET_ALL} .")
            armee = armee + 10
            economie = economie - 5
        elif choix42 == 'non' :
            print(f"Vous refusez de construire une muraille, vos relations diplomatiques avec le Sud se sont dégradées, votre commerce ralentit : {Fore.RED} -5 000 {Style.RESET_ALL} et votre peuple se sent en insécurité : {Fore.RED} -5 000 {Style.RESET_ALL} .")
            peuple = peuple - 5
            economie = economie - 5
        
        
    if event == 43:
        print(f"Le scientifique {Fore.YELLOW} Elon Monka {Style.RESET_ALL} : Seigneur", user,", j'ai trouvé comment transformer le plomb en or !")
        choix43 = input(f"Voulez-vous que je transforme votre plomb en or ?")
        if choix43 == 'oui':
            print(f"Votre scientifique a vraiment réussi à transformer le plomb en or mais les vapeurs de la transformation lui font vite oublier la manière dont il a réussi cette exploit. Cependant, votre économie en bénéficie : {Fore.GREEN} +15 000 {Style.RESET_ALL} francs grâce à l'or vendu.")
            economie = economie + 15
        elif choix43 == 'non' :
            print(f"Votre scientifique est déçu et oublie rapidement comment il a réussi son exploit ...")
        
        
    if event == 44:
        print(f"Le {Fore.YELLOW} Sir Rudolf {Style.RESET_ALL} : Seigneur", user,", d'autres pays ont commencé l'esclavagisme.")
        choix44 = input(f"Voulez-vous aussi commencer le commerce de l'esclave?")
        if choix44 == 'oui':
            print(f"Vous commencez le commerce de l'esclave. Votre économie explose : {Fore.GREEN} +25 000 {Style.RESET_ALL} francs et votre peuple devient lui aussi plus riche : {Fore.GREEN} +10 000 {Style.RESET_ALL} . Mais les religieux n'aiment pas ce choix : {Fore.RED} 10 000 {Style.RESET_ALL} .")
            economie = economie + 25
            religion = religion - 10
            peuple = peuple + 10
        elif choix44 == 'non' :
            print(f"Vous ne profitez pas du commerce de l'esclave. Votre économie est ralentie par les pays qui le font : {Fore.RED} -5 000 {Style.RESET_ALL} . Mais l'Eglise approuve votre choix : {Fore.GREEN} +10 000 {Style.RESET_ALL} .")
            economie = economie - 5
            religion = religion + 10
        
        
    if event == 45:
        print(f"Le {Fore.YELLOW} Sir Rudolf {Style.RESET_ALL} : vous devriez augmenter les impôts.")
        choix45 = input(f"Voulez-vous doubler ou tripler les impôts ?")
        if choix45 == 'doubler':
            print(f"Vous avez doublé les impôts, votre peuple est mécontent : {Fore.RED} -5 000 {Style.RESET_ALL} . Cependant, les impôts vous financent {Fore.GREEN} 10 000 {Style.RESET_ALL} francs.")
            peuple = peuple -5
            economie = economie + 10
        elif choix45 == 'tripler' :
            print(f"Vous avez triplé les impôts, votre peuple est mécontent : {Fore.RED} -10 000 {Style.RESET_ALL} . Cependant, les impôts vous financent {Fore.GREEN} 20 000 {Style.RESET_ALL} francs.")
            economie = economie + 20
            peuple = peuple -10
        
        
    if event == 46:
        print(f"Le général {Fore.YELLOW} Baldur Legrand {Style.RESET_ALL} : la paye des soldats est trop basse. Ils veulent être payés correctement et régulièrement.")
        choix46 = input(f"Voulez-vous augmenter le salaire de vos soldats ?")
        if choix46 == 'oui':
            print(f"{Fore.GREEN} 5000 {Style.RESET_ALL} soldats sont contents de s'être fait entendre. Cependant, votre économonie en prend un coup : {Fore.RED} 10 000 {Style.RESET_ALL} francs en moins.")
            armee = armee + 5
            economie = economie - 10
        elif choix46 == 'non' :
            print(f"Votre armée n'est pas contente, {Fore.RED} 5000 {Style.RESET_ALL} soldats font grêve.")
            armee = armee - 5
        
        
    if event == 47:
        print(f"Le tavernier {Fore.YELLOW} Sammy Taverne {Style.RESET_ALL} : Seigneur", user,", on a retrouvé votre femme accompagnée d'un homme ivre à notre taverne. Je crois qu'elle vous trompe ! ")
        choix47 = input(f"Qu'allez vous faire ? ?\n 1 : Exiler votre femme \n 2 : Quelle foutaise ! \n")
        if choix47 == 1:
            print(f"Vous avez choisi d'exiler votre femme. Votre peuple est mécontent de voir votre séparation : {Fore.RED} -5 000 {Style.RESET_ALL} . Cependant, votre armée est fière de votre choix autoritaire : {Fore.GREEN} +10 000 {Style.RESET_ALL} .")
            peuple = peuple - 5
            armee = armee + 10
        elif choix47 == 2 :
            print(f"Vous refusez le constat du tavernier! Votre armée se moque de vous : {Fore.RED} -5 000 {Style.RESET_ALL} .")
            armee = armee - 5
        
        
    if event == 48:
        print(f"Le chambellan {Fore.YELLOW} Salur Maloth {Style.RESET_ALL} : un voleur s'est introduit dans votre armurerie.")
        choix48 = input(f"\n 1 : D'accord... \n 2 : Ce n'est pas grave... \n")
        if choix48 == 1 :
            print(f"Vous perdez {Fore.RED} 5000 {Style.RESET_ALL} armes.")
            armee = armee - 5
        elif choix48 == 2 :
            print(f"Vous perdez {Fore.RED} 5000 {Style.RESET_ALL} armes.")
            armee = armee - 5
        
        
    if event == 49:
        print(f"Le chambellan {Fore.YELLOW} Salur Maloth {Style.RESET_ALL} : un voleur s'est introduit dans votre église.")
        choix49 = input(f"\n 1 : D'accord... \n 2 : Ce n'est pas grave... \n")
        if choix49 == 1 :
            print(f"Vous perdez {Fore.RED} 5000 {Style.RESET_ALL} adeptes.")
            religion = religion - 5
        elif choix49 == 2 :
            print(f"Vous perdez {Fore.RED} 5000 {Style.RESET_ALL} adeptes.")
            religion = religion - 5



    if event == 50:
        print(f"Le chambellan {Fore.YELLOW} Salur Maloth {Style.RESET_ALL} : un voleur s'est introduit dans les maisons de vos habitants.")
        choix50 = input(f"\n 1 : D'accord... \n 2 : Ce n'est pas grave... \n")
        if choix50 == 1 :
            print(f"Vous perdez {Fore.RED} 5000 {Style.RESET_ALL} habitants.")
            peuple = peuple - 5
        elif choix50 == 2 :
            print(f"Vous perdez {Fore.RED} 5000 {Style.RESET_ALL} habitants.")
            peuple = peuple - 5
        
        
    if event == 51:
        print(f"Le chambellan {Fore.YELLOW} Salur Maloth {Style.RESET_ALL} : un voleur s'est introduit dans votre trésorerie.")
        choix51 = input(f"\n 1 : D'accord... \n 2 : Ce n'est pas grave... \n")
        if choix51 == 1 :
            print(f"Vous perdez {Fore.RED} 5000 {Style.RESET_ALL} francs.")
            economie = economie - 5
        elif choix51 == 2 :
            print(f"Vous perdez {Fore.RED} 5000 {Style.RESET_ALL} francs.")
            economie = economie - 5



    if event == 52:
        print(f"Une personne nommée {Fore.YELLOW} John titor {Style.RESET_ALL} : je vous apporte le téléphone et un chargeur bis.\n")
        print(f"Le chambellan {Fore.YELLOW} Salur Maloth {Style.RESET_ALL} : qu'est-ce donc cette chose !?\n")
        print(f"L'évêque {Fore.YELLOW} Antoine Malbonne {Style.RESET_ALL} : jetons cette hérésie ! \n Le scientifique {Fore.YELLOW} Elon Monka {Style.RESET_ALL} : oh ! Un miroir lumineux ! J'aimerais l'étudier ...\n")
        choix52 = input(f"Que voulez-vous faire ?\n 1 : Le garder \n 2 : Le jeter au bûcher \n")
        if choix52 == 1 :
            print(f"Le scientifique va étudier cette objet de très près. Vous obtenez un {Fore.BLUE} téléphone {Style.RESET_ALL} ainsi qu'un {Fore.BLUE} chargeur {Style.RESET_ALL} .")
            objet = objet + 2
        elif choix52 == 2 :
            print(f"Vous jetez le miroir lumineux au bûcher.")
            
            
    if event == 53 :
        print(f"Le {Fore.YELLOW} Sir Rudolf {Style.RESET_ALL} : Vous devriez aller combattre le monstre !")
        choix53 = input(f"Voulez-vous aller combattre ce monstre ?")
        if choix53 == 'oui' :
            print(f"Le {Fore.YELLOW} Monstre {Style.RESET_ALL} : Grrrrh !")
            combatmonstre()
        elif choix == 'non' :
            print(f"Vous décidez de laissez ce monstre inconnu.")
        
        
        
    if event == 54 :
        print(f"Le {Fore.YELLOW} Baldur Legrand {Style.RESET_ALL} : Voulez-vous vous entraîner au combat ?")
        choix54 = input("Acceptez-vous de vous entraîner contre le Général ?")
        if choix54 == 'oui' :
            print(f"Le {Fore.YELLOW} Baldur Legrand {Style.RESET_ALL} : Allons-y. Et je ne vais pas retenir mes coups !")
            combatgeneral()
        elif choix54 == 'non' :
            print(f"Votre Général et votre armée sont déçues : {Fore.RED} -5 000 {Style.RESET_ALL} .")
          