#Trié ou pas
#Créez un programme qui détermine si une liste d’entiers est triée ou pas.

import sys



def list_arguments(*args):
    return [str(arg) for arg in args]

args = [int(arg) for arg in sys.argv[1:]]
listeDarguments = list_arguments(*args)

def nombre_premier(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


try:
    listeDarguments = int(listeDarguments)
    if nombre_premier(listeDarguments) and listeDarguments == listeDarguments.sort():
        print("Triée !")
    elif nombre_premier(listeDarguments) and listeDarguments != listeDarguments.sort():
        print("Pas triée !")
    else:
        print("erreur")
except ValueError:
    print("Entré une liste de nombre premier separé par des espaces")