#Pair ou impair
#Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair..
#Attention : gérez aussi les entiers négatifs.


#demande de l'argument 
#savoir si c'est un entier pair ou impair
#afficher la reponse



import sys

a = int(sys.argv[1])



if type(a) is  int:
    if a == 0:
        print("impossible")
    elif a % 2 == 0:
        print("pair")
    else:
        print("impair")
else:
    print("tu ne me la mettra pas a l'envers")