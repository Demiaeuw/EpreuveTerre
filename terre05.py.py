#Divisions
#Créez un programme qui affiche le résultat et le reste d’une division entre deux nombres.

import sys

val1 = sys.argv[1]
val2 = sys.argv[2]

def division():
    z = val1 / val2
    y = val1 % val2
    print("resultat :", int(z), "\nreste :", int(y))


try:
    val1 = int(val1)
    val2 = int(val2)
    if val2 == 0:
        print("erreur")
    elif val2 > val1:
        print("erreur")
    else:
        division()
except ValueError:
    print("tu ne me la mettra pas val l'envers")