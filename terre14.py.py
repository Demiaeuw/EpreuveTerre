#Trié ou pas
#Créez un programme qui détermine si une liste d’entiers est triée ou pas.



#recuperer la liste d'argument 
#definir si c'est un nombre premier
#savoir si c'est une liste en ordre
#gerer les erreurs 



import sys

#mes fonctions 
"""def list_arguments(*args):                                                                              #recuperer la liste d'argument 
    return [str(arg) for arg in args]

def nombre_premier(n):                                                                                  #definir si c'est un nombre premier
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


args = [int(arg) for arg in sys.argv[1:]]
listeDarguments = list_arguments(*args)
listeNombrePremier = nombre_premier(listeDarguments)"""


#1ere version 
"""try:

    if nombre_premier(listeDarguments) and listeDarguments == listeDarguments.sort():                   #savoir si c'est une liste en ordre
        print("Triée !")
    elif nombre_premier(listeDarguments) and listeDarguments != listeDarguments.sort():
        print("Pas triée !")
    else:
        print("erreur")
except ValueError:                                                                                      #gerer les erreurs 
    print("Entré une liste de nombre premier separé par des espaces")"""


#2eme version
"""try:
    if all(listeNombrePremier[i] <= listeNombrePremier[i+1] for i in range(len(listeNombrePremier)-1)):
        print("Triée !")
    else:
        print("Pas triée !")
except ValueError:
    print("Erreur")"""


def nombre_premier(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

arguments = sys.argv[1:]
nombrePremier = []
nombrePasPremier = []


for argument in arguments:
    try:
        nombre = int(argument)
        if nombre_premier(nombre):
            nombrePremier.append(argument)
        else:
            nombrePasPremier.append(argument)
    except ValueError:
        nombrePasPremier.append(argument)

if nombrePasPremier:
    non_valides = ", ".join(nombrePasPremier)
    print(f"'{non_valides}', ne sont pas des entiers premiers !")
