#24 to 12
#Créez un programme qui transforme une heure affichée en format 24h en une heure affichée en format 12h.

#Attention : midi et minuit.


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

