##### Terre - Pair ou impair #####
# Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair..
# Attention : gérez aussi les entiers négatifs.

import sys

### Function ###
def is_even(number_input):
    number_int = int(number_input)

    if number_int % 2 == 0:
        return True
    else:
        return False

def handle_argument_errors():
    if len(sys.argv) != 2 or not sys.argv[1].strip('-').isdigit():
        print("Tu ne me la mettras pas à l’envers.")
        exit()

### Error ###
handle_argument_errors()

### Parsing ###
number_input = sys.argv[1]

### Problem Solving ###
even_or_odd_result = "pair" if is_even(number_input) else "impair"

### Result ###
print(even_or_odd_result)
