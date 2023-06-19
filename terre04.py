##### Terre - Pair ou impair #####
# Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair..
# Attention : gérez aussi les entiers négatifs.

import sys

### Function ###
def even_or_odd(number):
    number_int = int(number)

    if number_int % 2 == 0:
        return "pair"
    else:
        return "impair"

def error():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Tu ne me la mettras pas à l’envers.")
        exit()

### Error ###
error()

### Parsing ###
number = sys.argv[1]

### Problem Solving ###
even_or_odd_result = even_or_odd(number)

### Result ###
print(even_or_odd_result)
