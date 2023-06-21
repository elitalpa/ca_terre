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

def handle_argument_errors():
    if len(sys.argv) != 2 or sys.argv[1].isdigit():
        print("erreur: Veuillez entrer une (seule) chaîne de caractères comme argument.")
        exit()

### Error ###
handle_argument_errors()

### Parsing ###
string_input = sys.argv[1]

### Problem Solving ###
reversed_string_result = reverse_string(string_input)

### Result ###
print(reversed_string_result)
