##### Terre - L’alphabet #####
# Créez un programme qui affiche l’alphabet en lettres minuscules suivi d’un retour à la ligne.
# Attention : votre programme devra utiliser une boucle.

### Function ###
def get_alphabet():
    a_letter = 97
    z_letter = 122
    alphabet_result = ""

    for ascii_value in range(a_letter, z_letter + 1):
        alphabet_result += chr(ascii_value)

    return alphabet_result

### Error ###

### Parsing ###

### Problem Solving ###
alphabet = get_alphabet()

### Result ###
print(alphabet)
