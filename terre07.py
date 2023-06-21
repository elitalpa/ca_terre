##### Terre - Taille d’une chaîne #####
# Créez un programme qui affiche le nombre de caractères d’une chaîne de caractères passée en argument.

import sys

### Function ###
def number_of_chr_in_str(string):
    number_of_chr = 0
    
    for chr in string:
        number_of_chr += 1
    
    return number_of_chr

def handle_argument_errors():
    if len(sys.argv) != 2 or sys.argv[1].isdigit():
        print("erreur: Veuillez entrer une (seule) chaîne de caractères comme argument.")
        exit()

### Error ###
handle_argument_errors()

### Parsing ###
string_input = sys.argv[1]

### Problem Solving ###
number_of_chr_in_str_result = number_of_chr_in_str(string_input)

### Result ###
print(number_of_chr_in_str_result)
