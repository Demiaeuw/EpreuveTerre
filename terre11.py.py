#24 to 12
#Créez un programme qui transforme une heure affichée en format 24h en une heure affichée en format 12h.

#Attention : midi et minuit.

"""

le format 24 = 13:45
le format 12 = 01:45 PM
minuit  = 12:00 AM
midi    = 12: PM

"""


"""

import sys

# Vérification du nombre d'arguments
if len(sys.argv) < 2:
    print("Veuillez fournir une heure au format hh:mm.")
else:
    # Récupération de l'heure à partir de sys.argv
    heure = sys.argv[1]

    # Décomposition de l'heure en heures et minutes
    parties = heure.split(":")

    # Conversion des parties en entiers
    heures = int(parties[0])
    minutes = int(parties[1])

    # Affichage du résultat
    print("Heures :", heures)
    print("Minutes :", minutes)

"""
import sys

monHeure = sys.argv[1]
partie = monHeure.split(":")
heures = int(partie[0])
minutes = int(partie[1])


if len(sys.argv) < 2:
    print("Entrer une heure au format hh:mm")
else:
    def changement(heures):
        if heures == 00:
            return str(heures) + ":" + str(minutes) + "AM"
        elif heures < 12:
            return str(heures) + ":" + str(minutes) +"AM"
        elif heures == 12:
            return str(heures) + ":" + str(minutes) + "PM"
        else:
            return str(heures - 12) + ":" + str(minutes) + "PM"
    heuresUS = changement(heures)
    print(heuresUS)

