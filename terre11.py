##### Terre - 24 to 12 #####
# Créez un programme qui transforme une heure affichée en format 24h en une heure affichée en format 12h
# Attention : midi et minuit.

import sys

### Function ###
def transform_24_to_12(time):
    hour_str = time[:2]
    hour_int = int(time[:2])
    minutes = time[3:5]

    if hour_int >= 0 and hour_int <= 11:
        return f"{hour_str}:{minutes}AM"

    if hour_int >= 12 and hour_int <= 21:
        return f"0{str(hour_int - 12)}:{minutes}PM"
    
    if hour_int == 22 or hour_int == 23:
        return f"{str(hour_int - 12)}:{minutes}PM"

def handle_argument_errors():
    if len(sys.argv) != 2:
        print("erreur: Veuillez n'entrer qu'un (seul) argument.")
        exit()
    if len(sys.argv[1]) != 5:
        print("erreur: Veuillez ne pas entrer plus ou moins de 5 caractères.")
        exit()

    sys.argv[1] = sys.argv[1]

    if sys.argv[1][2] != ":":
        print("erreur: Veuillez entrer l'heure au format hh:mm (Exemple: 13:30). Il manque le signe ':' au milieu.")
        exit()

    if not sys.argv[1][:2].isdigit() or not sys.argv[1][3:5].isdigit():
        print("erreur: Veuillez entrer l'heure au format hh:mm (Exemple: 13:30). Les heures et les minutes doivent être des nombres.")
        exit()
    
    if int(sys.argv[1][:2]) < 0 or int(sys.argv[1][:2]) > 23:
        print("erreur: Veuillez entrer l'heure au format hh:mm (Exemple: 13:30). Le nombre d'heures ne peut être que de 00 à 23 compris.")
        exit()
    if int(sys.argv[1][3:5]) < 0 or int(sys.argv[1][3:5]) > 60:
        print("erreur: Veuillez entrer l'heure au format hh:mm (Exemple: 13:30). Le nombre de minutes ne peut être que de 00 à 60 compris.")
        exit()

### Error ###
handle_argument_errors()

### Parsing ###
time_input = sys.argv[1]

### Problem Solving ###
transform_24_to_12_result = transform_24_to_12(time_input)

### Result ###
print(transform_24_to_12_result)
