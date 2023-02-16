#Trié ou pas
#Créez un programme qui détermine si une liste d’entiers est triée ou pas.

#pas de chiffre premier


import sys




arguments = sys.argv[1:]
liste = []


for argument in arguments:
    try:
        nombre = int(argument)
        liste.append(argument)
    except ValueError:
        print("Entré une suite de nombre entier")

if len(arguments) <= 1:
    print("Ce n'est pas une liste !")
elif all(liste[i] <= liste[i+1] for i in range(len(liste)-1)):
    print("Triée !")
else:
    print("Pas triée !")