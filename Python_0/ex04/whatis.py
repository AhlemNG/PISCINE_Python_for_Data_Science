import sys

args = sys.argv

try:
    if len(args) > 2:
        raise AssertionError("more than one argument is provided")
    if len(args) == 1:
        exit()
    nb = int(args[1])
    if nb % 2 ==  0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except ValueError:
    print("AssertionError: argument is not an integer")
    exit(1)
except AssertionError as e:
    print(f"AssertionError: {e}")