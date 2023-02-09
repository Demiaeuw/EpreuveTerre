#Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne.

#je dois aller chercher la lettre de depart dans l'argument
#je dois utiliser cette lettre pour lancer ma fonction 
#je dois lancer cette fonction


import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"

def choix_de_lettre():
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])

lettre_de_depart = choix_de_lettre()

print(lettre_de_depart)