##### Terre - 12 to 24 #####
# Créez un programme qui transforme une heure affichée en format 12h en une heure affichée au format 24h.
# Attention : midi et minuit.

import sys

### Function ###
def transform_24_to_12(time):
    time_result = ""
    hour_str = time[:2]
    hour = int(time[:2])
    minutes = time[3:5]
    time_indicator = time[-2:]

    if time_indicator == "AM" and hour >= 1 and hour <= 11:
        return f"{hour_str}:{minutes}"

    if time_indicator == "AM" and hour == 12:
        return f"00:{minutes}"

    if time_indicator == "PM" and hour >= 1 and hour <= 11:
        return f"{hour + 12}:{minutes}"

    if time_indicator == "PM" and hour == 12:
        return f"12:{minutes}"

def display_error_message_and_exit():
    print("erreur.")
    exit()

def handle_argument_errors():
    if len(sys.argv) != 2:
        display_error_message_and_exit()
    if len(sys.argv[1]) != 7:
        display_error_message_and_exit()

    if sys.argv[1][2] != ":":
        display_error_message_and_exit()

    if not sys.argv[1][:2].isdigit() or not sys.argv[1][3:5].isdigit():
        display_error_message_and_exit()

    if int(sys.argv[1][:2]) < 1 or int(sys.argv[1][:2]) > 12:
        display_error_message_and_exit()
    if int(sys.argv[1][3:5]) > 60:
        display_error_message_and_exit()

    if sys.argv[1][5:7] != "AM" and sys.argv[1][5:7] != "PM":
        display_error_message_and_exit()

### Error ###
handle_argument_errors()

### Parsing ###
time_input = sys.argv[1]

### Problem Solving ###
transform_24_to_12_result = transform_24_to_12(time_input)

### Result ###
print(transform_24_to_12_result)
