#Trié ou pas
#Créez un programme qui détermine si une liste d’entiers est triée ou pas.



#recuperer la liste d'argument 
#definir si c'est un nombre premier
#savoir si c'est une liste en ordre
#gerer les erreurs 



import sys



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
if len(arguments) <= 1:
    print("Ce n'est pas une liste !")
elif nombrePasPremier:
    non_valides = ", ".join(nombrePasPremier)
    print(f"'{non_valides}', ne sont pas des entiers premiers !")
elif nombrePremier:
    try:
        if all(nombrePremier[i] <= nombrePremier[i+1] for i in range(len(nombrePremier)-1)):
            print("Triée !")
        else:
            print("Pas triée !")
    except ValueError:
        print("Erreur")
