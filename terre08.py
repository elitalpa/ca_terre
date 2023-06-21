##### Terre - Puissance d’un nombre #####
# Créez un programme qui affiche le résultat d’une puissance.
# L’exposant ne pourra pas être négatif.
# Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.

import sys

### Function ###
def number_to_the_power_of_exponent(number, exponent):
    number_int = int(number)
    exponent_int = int(exponent)
    power_result = number_int

    if exponent_int == 0:
        power_result = 1
    else:
        for power in range(exponent_int - 1):
            power_result *= number_int

    return power_result

def handle_argument_errors():
    if len(sys.argv) != 3:
        print("erreur: Veuillez entrer (seulement) 2 arguments: la base et l'exposant.")
        exit()
    if not sys.argv[1].strip('-').isdigit() or not sys.argv[2].strip('-').isdigit():
        print("erreur: Vous avez entré 1 ou 2 arguments qui ne sont pas des nombres entiers.")
        exit()
    if int(sys.argv[2]) < 0:
        print("erreur: L'exposant ne peut pas être négatif.")
        exit()

### Error ###
handle_argument_errors()

### Parsing ###
number_input = sys.argv[1]
exponent_input = sys.argv[2]

### Problem Solving ###
number_to_the_power_of_exponent_result = number_to_the_power_of_exponent(number_input, exponent_input)

### Result ###
print(number_to_the_power_of_exponent_result)
