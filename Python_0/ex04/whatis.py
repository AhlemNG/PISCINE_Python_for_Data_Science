# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number", type=int)
# args = parser.parse_args()
# if len(args.args) > 2:
#     parser.error("more than one argument is provided")
# print(args.square**2)

import argparse

# Créer le parser
parser = argparse.ArgumentParser(description="Script qui accepte un seul argument maximum.")

# Accepter des arguments positionnels (liste)
parser.add_argument('args', nargs='*', help='Arguments à traiter')

# Parse les arguments
args = parser.parse_args()

# Vérifier le nombre d'arguments et lever une AssertionError
assert type(args.args[0]) == int, "AssertionError: argument is not an integer"

assert len(args.args) <= 1, "AssertionError: more than one argument is provided"

print(f"Argument(s) reçu(s) : {args.args}")
