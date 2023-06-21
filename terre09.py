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
    
    print("erreur: Impossible d'avoir la racine carrée.")
    exit()

def handle_argument_errors():
    if len(sys.argv) != 2:
        print("erreur: Veuillez n'entrer qu'un (seul) argument.")
        exit()
    if not sys.argv[1].isdigit():
        print("erreur: Veuillez entrer un entier positif.")
        exit()
    if int(sys.argv[1]) <= 0:
        print("erreur: Veuillez entrer un entier positif.")
        exit()

### Error ###
handle_argument_errors()

### Parsing ###
number_input = sys.argv[1]

### Problem Solving ###
square_root_result = calculate_square_root(number_input)

### Result ###
print(square_root_result)
