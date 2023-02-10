#Racine carrée d’un nombre
#Créez un programme qui affiche la racine carrée d’un entier positif.



import sys

val1 = sys.argv[1]

try:
    val1 = int(val1)
    if val1 == 0:
        print("erreur")
    elif val1 < 0:
        print("erreur")
    else:
        resultat = val1**0.5
        print(resultat)
except ValueError:
    print("erreur")
