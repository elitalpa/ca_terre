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

### Error ###

### Parsing ###
starting_letter = ord(sys.argv[1])

### Problem Solving ###
alphabet_from = get_alphabet_from(starting_letter)

### Result ###
print(alphabet_from)
