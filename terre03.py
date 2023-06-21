##### Terre - L’alphabet à partir de #####
# Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne.
# Attention : votre programme devra utiliser une boucle.

import sys

### Function ###
def get_alphabet_from(starting_letter):
    z_letter = 122
    alphabet_result = ""

    for chr_number in range(starting_letter, z_letter + 1):
        alphabet_result += chr(chr_number)

    return alphabet_result

def handle_argument_errors():
    if len(sys.argv) != 2:
        print("erreur: Veuillez entrer un (seul) argument.")
        exit()
    if ord(sys.argv[1]) not in range(97, 122 + 1):
        print("erreur: Seules les lettres minuscules (faisant partie de l'alphabet ASCII) sont acceptées.")
        exit()

### Error ###
handle_argument_errors()

### Parsing ###
starting_letter_input = ord(sys.argv[1])

### Problem Solving ###
alphabet_from = get_alphabet_from(starting_letter_input)

### Result ###
print(alphabet_from)
