##### Terre - Inverser une chaîne #####
# Créez un programme qui affiche l’inverse de la chaîne de caractères donnée en argument.
# Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.

import sys

### Function ###
def reverse_string(string):
    reversed_string = ""

    for chr_index in range(1, len(string) + 1):
        reversed_string += string[-chr_index]

    return reversed_string

def display_error_message_and_exit():
    print("erreur.")
    exit()

def error():
    if len(sys.argv) != 2:
        display_error_message_and_exit()
    if sys.argv[1].isdigit():
        display_error_message_and_exit()

### Error ###
error()

### Parsing ###
string_input = sys.argv[1]

### Problem Solving ###
reversed_string_result = reverse_string(string_input)

### Result ###
print(reversed_string_result)
