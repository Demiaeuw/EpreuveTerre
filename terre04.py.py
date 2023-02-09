#Pair ou impair
#Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair..
#Attention : gérez aussi les entiers négatifs.


#demande de l'argument 
#savoir si c'est un entier pair ou impair
#afficher la reponse



import sys

val = sys.argv[1]

try:
    val = int(val)
    if val == 0:
        print("impossible")
    elif val % 2 == 0:
        print("pair")
    else:
        print("impair")  
except ValueError:
    print("tu ne me la mettra pas val l'envers")

"""
if type(val) is  int:
    if val == 0:
        print("impossible")
    elif val % 2 == 0:
        print("pair")
    else:
        print("impair")
else:
    print("tu ne me la mettra pas val l'envers")
"""