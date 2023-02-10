#Taille d’une chaîne
#Créez un programme qui affiche le nombre de caractères d’une chaîne de caractères passée en argument.

#il ne doit y avoir qu'un argument (chemin fonction + 1 argument = 2)
#ce doit forcement etre une chaine de caractere (str) si pas de chaine ou autre chose erreur


import sys



def main():
    if len(sys.argv) != 2:
        print("Erreur")
        return
    argument = sys.argv[1]
    if not isinstance(argument, str):
        print("Erreur")
        return
    print(len(argument))

main()