##### Terre - Nombre premier #####
# Créez un programme qui affiche si un nombre est premier ou pas.
# Attention : 0 et 1 ne sont pas des nombres premiers. Gérez les erreurs d’arguments.
# nombre premier = qui ne peut être divisé que par lui-même et par 1

import sys

### Function ###
def is_prime_number_or_not(number):
    number_int = int(number)
    response_message = ""

    for i in range(2, number_int - 1):
        #print(i)
        if number_int % i == 0 :
            response_message = "Non, " + str(number_int) + " n’est pas un nombre premier."
            return response_message

    response_message = "Oui, " + str(number_int) + " est un nombre premier."
    return response_message

def display_error_message_and_exit():
    print("erreur.")
    exit()

def handle_argument_errors():
    if len(sys.argv) != 2:
        display_error_message_and_exit()
    if not sys.argv[1].isdigit():
        display_error_message_and_exit()
    if int(sys.argv[1]) <= 1:
        display_error_message_and_exit()

### Error ###
handle_argument_errors()

### Parsing ###
number_input = sys.argv[1]

### Problem Solving ###
is_prime_number_or_not_result = is_prime_number_or_not(number_input)

### Result ###
print(is_prime_number_or_not_result)
