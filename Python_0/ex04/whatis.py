import sys

args = sys.argv

assert len(args) <=2, "AssertionError: more than one argument is provided"

if len(args) == 0:
    # sys.exit()
    exit()

try:
    nb = int(args[1])
    if nb % 2 ==  0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except ValueError:
    raise AssertionError("AssertionError: argument is not an integer")
