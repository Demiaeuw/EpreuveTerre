#12 to 24
#Créez un programme qui transforme une heure affichée en format 12h en une heure affichée au format 24h.

#Attention : midi et minuit.


import sys

monHeure = sys.argv[1]
partie = monHeure.split(":")
heures = partie[0]
minutes_et_jour = partie[1][:-2]
minutes = partie[1][:2]
jourNuit = partie[1][-2:]



import sys

monHeure = sys.argv[1]
parties = monHeure.split(":")
heures = int(parties[0])
minutes_et_jour = parties[1]
minutes = int(minutes_et_jour[:-2])
jour = minutes_et_jour[-2:]

if len(sys.argv) < 2:
    print("Entrer une heure au format hh:mm(am/pm)")
else:
    def changement(heures):
        if jour == "am":
            return str(heures) + ":" + str(minutes)
        else:
            return str(heures + 12) + ":" + str(minutes)
    heuresEU = changement(heures)
    print(heuresEU)

