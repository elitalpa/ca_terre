##### Terre - Taille d’une chaîne #####
# Créez un programme qui affiche le nombre de caractères d’une chaîne de caractères passée en argument.

import sys

### Function ###
def number_of_chr_in_str(string):
    number_of_chr = 0
    
    for chr in string:
        number_of_chr += 1
    
    return number_of_chr

def display_error_message_and_exit():
    print("erreur.")
    exit()

def error():
    if len(sys.argv) != 2:
        display_error_message_and_exit()
    if sys.argv[1].isdigit():
        display_error_message_and_exit()

### Error ###
error()

### Parsing ###
string_input = sys.argv[1]

### Problem Solving ###
number_of_chr_in_str_result = number_of_chr_in_str(string_input)

### Result ###
print(number_of_chr_in_str_result)
