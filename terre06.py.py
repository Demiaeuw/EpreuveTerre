#Inverser une chaîne
#Créez un programme qui affiche l’inverse de la chaîne de caractères donnée en argument.


#recuperer la chaine de caractere
#fonction pour retourner le texte
#afficher le texte

import sys

def chaine_de_char():
    resultat = ""
    for i in range(1, len(sys.argv)):
        resultat += sys.argv[i] + " "
    return resultat

def inverse(a):
    return a[::-1]

text = chaine_de_char()
textInverse = inverse(text)
print(textInverse)