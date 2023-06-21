##### Terre - Divisions #####
# Créez un programme qui affiche le résultat et le reste d’une division entre deux nombres.

import sys

### Function ###
def get_quotient_of_division(dividend, divisor):
    dividend_int = int(dividend)
    divisor_int = int(divisor)

    division_result_str = "résultat: " + str(dividend_int // divisor_int)
    return division_result_str

def get_remainder_of_division(dividend, divisor):
    dividend_int = int(dividend)
    divisor_int = int(divisor)

    remainder_result = "reste: " + str(dividend_int % divisor_int)
    return remainder_result

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
quotient_result_str = get_quotient_of_division(dividend_input, divisor_input)
remainder_result_str = get_remainder_of_division(dividend_input, divisor_input)

### Result ###
print(quotient_result_str)
print(remainder_result_str)
