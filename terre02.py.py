#Afficheur d’arguments
#Créez un programme qui affiche les arguments qu’il reçoit ligne par ligne, peu importe le nombre d’arguments.

import sys

def display_arguments():
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])

if __name__ == '__main__':
    display_arguments()
