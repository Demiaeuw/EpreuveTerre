#Nom du programme
#Créez un programme qui affiche son nom de fichier.

def affiche_nom_fichier():
    print(__file__.split('\\')[-1])   #sous windows utilisation de "\\" au lieux de "/"

affiche_nom_fichier()
