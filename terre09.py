##### Terre - Racine carrée d’un nombre #####
# Créez un programme qui affiche la racine carrée d’un entier positif.
# Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.

import sys

### Function ###
def calculate_square_root(number):
    number_int = int(number)

    for num in range(number_int):
        if num * num == number_int:
            return num
            exit()
    
    display_error_message_and_exit()

def display_error_message_and_exit():
    print("erreur.")
    exit()

def handle_argument_errors():
    if len(sys.argv) != 2:
        display_error_message_and_exit()
    if not sys.argv[1].isdigit():
        display_error_message_and_exit()
    if int(sys.argv[1]) <= 0:
        display_error_message_and_exit()

### Error ###
handle_argument_errors()

### Parsing ###
number_input = sys.argv[1]

### Problem Solving ###
square_root_result = calculate_square_root(number_input)

### Result ###
print(square_root_result)
