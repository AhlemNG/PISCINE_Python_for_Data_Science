import sys


def isValidArg(string):
    """
    string: a string to validate
    return: True if all characters in the string are alphanumeric or spaces,
            False otherwise
    """
    for char in string:
        if not (char.isalnum() or char.isspace()):
            return False
    return True


def toMorse(string):
    """
    string: a string to convert to Morse code
    return: a string representing the Morse code translation of the input,
            with letters separated by spaces and words separated by '/'
    """
    NESTED_MORSE = {" ": "/ ",
                    "A": ".- ", "B": "-... ", "C": "-.-. ",
                    "D": "-.. ", "E": ". ",
                    "F": "..-. ", "G": "--. ", "H": ".... ",
                    "I": ".. ", "J": ".--- ", "K": "-.- ",
                    "L": ".-.. ", "M": "-- ", "N": "-. ",
                    "O": "--- ", "P": ".--. ", "Q": "--.- ",
                    "R": ".-. ", "S": "... ", "T": "- ",
                    "U": "..- ", "V": "...- ", "W": ".-- ",
                    "X": "-..- ", "Y": "-.-- ", "Z": "--.. ",
                    "1": ".---- ", "2": "..--- ", "3": "...-- ",
                    "4": "....- ", "5": "..... ", "6": "-.... ",
                    "7": "--... ", "8": "---.. ", "9": "----. ",
                    "0": "----- "}

    result = []
    for char in string.upper():
        if char in NESTED_MORSE:
            result.append(NESTED_MORSE[char])
    return ''.join(result)


def main():
    """
    args: command line arguments
    return: prints the Morse code translation of the input argument if valid,
            otherwise prints an error message
    """
    args = sys.argv
    if len(args) != 2 or not isValidArg(args[1]):
        print("AssertionError: the arguments are bad")
        return
    print(toMorse(args[1]))


if __name__ == "__main__":
    main()
