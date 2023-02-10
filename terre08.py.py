#Puissance d’un nombre
#Créez un programme qui affiche le résultat d’une puissance.
#L’exposant ne pourra pas être négatif.




import sys

base = sys.argv[1]
exposant = sys.argv[2]
resultat = 1



"""
try:
    base = int(base)
    exposant = int(exposant)
    resultat = int(resultat)

    if exposant == 0:
        print("erreur")
    elif exposant < 0:
        print("erreur")
    else:
        for i in range(exposant):
            resultat *= base
        print(resultat)
except ValueError:
    print("tu ne me la mettra pas val l'envers")
"""




try:
    base = int(base)
    exposant = int(exposant)
    resultat = int(resultat)

    if exposant == 0:
        print("erreur")
    elif exposant < 0:
        print("erreur")
    else:
        def puissance(x):
            return pow(x, exposant)

        resultat = puissance(base)
        print(resultat)
except ValueError:
    print("tu ne me la mettra pas val l'envers")