#Nombre premier
#Créez un programme qui affiche si un nombre est premier ou pas.

#Attention : 0 et 1 ne sont pas des nombres premiers. Gérez les erreurs d’arguments.



import sys

def nombre_premier(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

try:
    number = int(sys.argv[1])
    if nombre_premier(number):
        print("C'est un nombre premier")
    else:
        print("Ce n'est pas un nombre premier")
except ValueError:
    print("Veuillez entrer un entier valide")




