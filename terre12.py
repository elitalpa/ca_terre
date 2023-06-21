##### Terre - 12 to 24 #####
# Créez un programme qui transforme une heure affichée en format 12h en une heure affichée au format 24h.
# Attention : midi et minuit.

import sys

### Function ###
def transform_24_to_12(time):
    time_result = ""
    hour_str = time[:2]
    hour_int = int(time[:2])
    minutes = time[3:5]
    time_indicator = time[-2:]

    if time_indicator == "AM" and hour_int >= 1 and hour_int <= 11:
        return f"{hour_str}:{minutes}"

    if time_indicator == "AM" and hour_int == 12:
        return f"00:{minutes}"

    if time_indicator == "PM" and hour_int >= 1 and hour_int <= 11:
        return f"{hour_int + 12}:{minutes}"

    if time_indicator == "PM" and hour_int == 12:
        return f"12:{minutes}"

def handle_argument_errors():
    if len(sys.argv) != 2:
        print("erreur: Veuillez n'entrer qu'un (seul) argument.")
        exit()
    if len(sys.argv[1]) != 7:
        print("erreur: Veuillez ne pas entrer plus ou moins de 7 caractères.")
        exit()

    if sys.argv[1][2] != ":":
        print("erreur: Veuillez entrer l'heure au format hh:mmXM (Exemple: 01:30PM). Il manque le signe ':' au milieu.")
        exit()

    if not sys.argv[1][:2].isdigit() or not sys.argv[1][3:5].isdigit():
        print("erreur: Veuillez entrer l'heure au format hh:mmXM (Exemple: 01:30PM). Les heures et les minutes doivent être des nombres.")
        exit()

    if int(sys.argv[1][:2]) < 1 or int(sys.argv[1][:2]) > 12:
        print("erreur: Veuillez entrer l'heure au format hh:mmXM (Exemple: 01:30PM). Le nombre d'heures ne peut être que de 01 à 12 compris.")
        exit()
    if int(sys.argv[1][3:5]) < 0 or int(sys.argv[1][3:5]) > 60:
        print("erreur: Veuillez entrer l'heure au format hh:mmXM (Exemple: 01:30PM). Le nombre de minutes ne peut être que de 00 à 60 compris.")
        exit()

    if sys.argv[1][5:7] != "AM" and sys.argv[1][5:7] != "PM":
        print("erreur: Veuillez entrer l'heure au format hh:mmXM (Exemple: 01:30PM). Vous n'avez pas correctement entré AM (signifie Ante Meridiem en latin) ou PM (signifie Post Meridiem en latin).")
        exit()

### Error ###
handle_argument_errors()

### Parsing ###
time_input = sys.argv[1]

### Problem Solving ###
transform_24_to_12_result = transform_24_to_12(time_input)

### Result ###
print(transform_24_to_12_result)
