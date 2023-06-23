##### Terre - Divisions #####
# Créez un programme qui affiche le résultat et le reste d’une division entre deux nombres.

import sys

### Function ###
def calculate_division(dividend, divisor):
    dividend_int = int(dividend)
    divisor_int = int(divisor)

    quotient_result_str = "résultat: " + str(dividend_int // divisor_int)
    remainder_str = "reste: " + str(dividend_int % divisor_int)

    division_str = quotient_result_str + "\n" + remainder_str

    return division_str

def handle_argument_errors():
    if len(sys.argv) != 3:
        print("erreur: Veuillez entrer (seulement) 2 arguments: le dividende et le diviseur.")
        exit()
    if not sys.argv[1].strip('-').isdigit() or not sys.argv[2].strip('-').isdigit():
        print("erreur: Vous avez entré 1 ou 2 arguments qui ne sont pas des nombres entiers.")
        exit()
    if int(sys.argv[2]) == 0:
        print("erreur: Votre diviseur ne peut pas être 0.")
        exit()
    if int(sys.argv[1]) < int(sys.argv[2]):
        print("erreur: Le nombre que vous essayez de diviser (le dividende) est plus petit que le diviseur.")
        exit()

### Error ###
handle_argument_errors()

### Parsing ###
dividend_input = sys.argv[1]
divisor_input = sys.argv[2]

### Problem Solving ###
division_quotient_and_remainder_str = calculate_division(dividend_input, divisor_input)

### Result ###
print(division_quotient_and_remainder_str)
