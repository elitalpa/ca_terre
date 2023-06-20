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

    for power in range(exponent_int - 1):
        power_result *= number_int
    
    return power_result

def display_error_message_and_exit():
    print("erreur.")
    exit()

def error():
    if len(sys.argv) != 3:
        display_error_message_and_exit()
    if not sys.argv[1].strip('-').isdigit() or not sys.argv[2].isdigit():
        display_error_message_and_exit()
    if int(sys.argv[2]) <= 0:
        display_error_message_and_exit()

### Error ###
error()

### Parsing ###
number_input = sys.argv[1]
exponent_input = sys.argv[2]

### Problem Solving ###
number_to_the_power_of_exponent_result = number_to_the_power_of_exponent(number_input, exponent_input)

### Result ###
print(number_to_the_power_of_exponent_result)
