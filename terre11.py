##### Terre - 24 to 12 #####
# Créez un programme qui transforme une heure affichée en format 24h en une heure affichée en format 12h
# Attention : midi et minuit.

import sys

### Function ###
def transform_24_to_12(time):
    hour_str = time[:2]
    hour = int(time[:2])
    minutes = time[3:5]

    if hour >= 0 and hour <= 11:
        return f"{hour_str}:{minutes}AM"

    if hour >= 12 and hour <= 21:
        return f"0{str(hour - 12)}:{minutes}PM"
    
    if hour == 22 or hour == 23:
        return f"{str(hour - 12)}:{minutes}PM"

def display_error_message_and_exit():
    print("erreur.")
    exit()

def handle_argument_errors():
    if len(sys.argv) != 2:
        display_error_message_and_exit()
    if len(sys.argv[1]) != 5:
        display_error_message_and_exit()

    sys.argv[1] = sys.argv[1]

    if sys.argv[1][2] != ":":
        display_error_message_and_exit()

    if not sys.argv[1][:2].isdigit() or not sys.argv[1][3:5].isdigit():
        display_error_message_and_exit()
    
    if int(sys.argv[1][:2]) < 0 or int(sys.argv[1][:2]) > 23:
        display_error_message_and_exit()
    if int(sys.argv[1][3:5]) > 60:
        display_error_message_and_exit()

### Error ###
handle_argument_errors()

### Parsing ###
time_input = sys.argv[1]

### Problem Solving ###
transform_24_to_12_result = transform_24_to_12(time_input)

### Result ###
print(transform_24_to_12_result)
