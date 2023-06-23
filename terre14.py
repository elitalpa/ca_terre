##### Terre - Trié ou pas #####
# Créez un programme qui détermine si une liste d’entiers est triée ou pas.

import sys

### Function ###
def is_the_list_sorted(number_list):
    index = 0
    stop_index = len(number_list) - 1

    for number in number_list:
        if index == stop_index:
            break

        if not int(number_list[index]) < int(number_list[index + 1]):
            return False
        
        index += 1

    return True

def handle_argument_errors():
    if len(sys.argv) <= 2:
        print("erreur: Vous devez entrer au moins 2 arguments.")
        exit()
    
    for argument in sys.argv[1:]:
        if not argument.strip('-').isdigit():
            print("erreur: Vous devez entrer seulement des nombres entiers.")
            exit()

### Error ###
handle_argument_errors()

### Parsing ###
number_list = sys.argv[1:]

### Problem Solving ###
is_the_list_sorted_result = "Triée !" if is_the_list_sorted(number_list) else "Pas triée !"

### Result ###
print(is_the_list_sorted_result)

