##### Terre - Trouver la Suisse (lol) #####
# Créez un programme qui prend en paramètre trois entiers et affiche la valeur du milieu.

import sys

### Function ###
def find_Switzerland(first_number, second_number, third_number):
    num_1 = int(first_number)
    num_2 = int(second_number)
    num_3 = int(third_number)

    if num_2 > num_1 > num_3 or num_2 < num_1 < num_3:
        return num_1
    elif num_1 > num_2 > num_3 or num_1 < num_2 < num_3:
        return num_2
    elif num_2 > num_3 > num_1 or num_2 < num_3 < num_1:
        return num_3

def handle_argument_errors():
    if len(sys.argv) != 4:
        print("erreur: Vous devez entrer 3 arguments.")
        exit()
    if not sys.argv[1].strip('-').isdigit() or not sys.argv[2].strip('-').isdigit() or not sys.argv[3].strip('-').isdigit():
        print("erreur: Vous devez entrer 3 nombres entiers.")
        exit()
    if sys.argv[1] == sys.argv[2] == sys.argv[3] or sys.argv[1] == sys.argv[2] or sys.argv[1] == sys.argv[3] or sys.argv[2] == sys.argv[3]:
        print("erreur: Vos arguments ne peuvent pas être identiques.")
        exit()

### Error ###
handle_argument_errors()

### Parsing ###
first_number_input = sys.argv[1]
second_number_input = sys.argv[2]
third_number_input = sys.argv[3]

### Problem Solving ###
find_Switzerland_result = find_Switzerland(first_number_input, second_number_input, third_number_input )

### Result ###
print(find_Switzerland_result)

