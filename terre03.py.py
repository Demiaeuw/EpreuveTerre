#L’alphabet à partir de
#Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne.

#je dois aller chercher la lettre de depart dans l'argument
#je dois utiliser cette lettre pour lancer ma fonction 
#je dois lancer cette fonction


import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"

def choisir_lettre():
    for i in range(1, len(sys.argv)):
        return sys.argv[i]

def afficher_alphabet(lettreDepart):
    index = alphabet.index(lettreDepart)
    print(alphabet[index:])

if __name__ == '__main__':
    lettre_choisie = choisir_lettre()
    afficher_alphabet(lettre_choisie)
