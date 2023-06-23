##### Terre - Afficheur d’arguments #####
# Créez un programme qui affiche les arguments qu’il reçoit ligne par ligne, peu importe le nombre d’arguments.

import sys

### Function ###
def get_arguments_in_lines(arguments):
    arguments_in_lines = ""

    for each_argument in arguments:
        arguments_in_lines += f"{each_argument}\n"

    return arguments_in_lines

### Error ###

### Parsing ###
arguments_input = sys.argv[1:]

### Problem Solving ###
arguments_in_lines_result = get_arguments_in_lines(arguments_input)

### Result ###
print(arguments_in_lines_result, end="")
