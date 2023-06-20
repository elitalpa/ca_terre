##### Terre - Divisions #####
# Créez un programme qui affiche le résultat et le reste d’une division entre deux nombres.

import sys

### Function ###
def get_result_of_division(first_number, second_number):
    first_number_int = int(first_number)
    second_number_int = int(second_number)

    division_result = "résultat: " + str(first_number_int // second_number_int)
    return division_result

def get_remainder_of_division(first_number, second_number):
    first_number_int = int(first_number)
    second_number_int = int(second_number)

    remainder_result = "reste: " + str(first_number_int % second_number_int)
    return remainder_result

def display_error_message_and_exit():
    print("erreur.")
    exit()

def handle_argument_errors():
    if len(sys.argv) != 3:
        display_error_message_and_exit()
    if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
        display_error_message_and_exit()
    if int(sys.argv[1]) <= 0 or int(sys.argv[2]) <= 0:
        display_error_message_and_exit()
    if int(sys.argv[1]) < int(sys.argv[2]):
        display_error_message_and_exit()

### Error ###
handle_argument_errors()

### Parsing ###
first_number_input = sys.argv[1]
second_number_input = sys.argv[2]

### Problem Solving ###
division_result_str = get_result_of_division(first_number_input, second_number_input)
remainder_result_str = get_remainder_of_division(first_number_input, second_number_input)

### Result ###
print(division_result_str)
print(remainder_result_str)
