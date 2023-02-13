#Trié ou pas
#Créez un programme qui détermine si une liste d’entiers est triée ou pas.



#recuperer la liste d'argument 
#definir si c'est un nombre premier
#savoir si c'est une liste en ordre
#gerer les erreurs 



import sys


def list_arguments(*args):                                                                              #recuperer la liste d'argument 
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




try:

    if nombre_premier(listeDarguments) and listeDarguments == listeDarguments.sort():                   #savoir si c'est une liste en ordre
        print("Triée !")
    elif nombre_premier(listeDarguments) and listeDarguments != listeDarguments.sort():
        print("Pas triée !")
    else:
        print("erreur")
except ValueError:                                                                                      #gerer les erreurs 
    print("Entré une liste de nombre premier separé par des espaces")