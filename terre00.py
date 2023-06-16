##### Terre - L’alphabet #####
# Créez un programme qui affiche l’alphabet en lettres minuscules suivi d’un retour à la ligne.
# Attention : votre programme devra utiliser une boucle.

### Function ###
def get_alphabet():
    a_letter = 97
    z_letter = 122
    alphabet_result = ""

    for chr_number in range(a_letter, z_letter + 1):
        alphabet_result += chr(chr_number)

    return alphabet_result

### Error ###

### Parsing ###

### Problem Solving ###
alphabet = get_alphabet()

### Result ###
print(alphabet)
