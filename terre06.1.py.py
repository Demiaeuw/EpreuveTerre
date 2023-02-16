#Inverser une chaîne
#Créez un programme qui affiche l’inverse de la chaîne de caractères donnée en argument.

#avec une boucle for a la place du a[::-1]


import sys

argument = str(sys.argv[1])

reverse_String = ""
count = len(argument)

while count > 0:   
    reverse_String += argument[count - 1] 
    count = count - 1


try:
    if len(sys.argv) > 2:
        print("Merci de metre vos arguments entre guillemet ")
    elif len(sys.argv) == 1:
        print("Merci de fournir un argument")
    else:
        print(reverse_String)
except ValueError:
    print("Entrer un argument valide")
