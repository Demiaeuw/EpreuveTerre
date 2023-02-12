#Trouver la Suisse (lol)
#Créez un programme qui prend en paramètre trois entiers et affiche la valeur du milieu.


import sys 

val1 = sys.argv[1]
val2 = sys.argv[2]
val3 = sys.argv[3]

liste = [val1, val2, val3]
liste.sort()

print(liste[1])

