##### Terre - Pair ou impair #####
# Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair..
# Attention : gérez aussi les entiers négatifs.

import sys

### Function ###
def determine_even_or_odd(number_input):
    number_int = int(number_input)

    if number_int % 2 == 0:
        return "pair"
    else:
        return "impair"

def handle_argument_errors():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Tu ne me la mettras pas à l’envers.")
        exit()

### Error ###
handle_argument_errors()

### Parsing ###
number_input = sys.argv[1]

### Problem Solving ###
even_or_odd_result = determine_even_or_odd(number_input)

### Result ###
print(even_or_odd_result)
