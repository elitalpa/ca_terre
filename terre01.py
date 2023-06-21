##### Terre - Nom du programme #####
# Créez un programme qui affiche son nom de fichier.

import sys

### Function ###
def get_filename():
    filename_argument = sys.argv[0]
    return filename_argument

### Error ###

### Parsing ###

### Problem Solving ###
filename = get_filename()

### Result ###
print(filename)
