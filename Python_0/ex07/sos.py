import sys



def isValidArg(string):
    "checks if an argument is a string that contains only alpahnumeric carachters and spaces???"
    for letter in string:
        if letter.isdigit():
            return True
        if letter.isupper():
            return True
        if letter.islower():
            return True
        if letter.isspace():
            return True
        return False


def toMorse(string):
    "convertit un string en morse code"
    MORSE = {" ":  "/ ",
                    "A": ".- ", "B": "-...", "C": "-.-.",
                    "D": "-..", "E": ".",
                    "F": "..-.", "G": "--.", "H": "....",
                    "I": "..", "J": ".---", "K": "-.-",
                    "L": ".-..", "M": "--", "N": "-.",
                    "O": "---", "P": ".--.", "Q": "--.-",
                    "R": ".-.", "S": "...", "T": "-",
                    "U": "..-", "V": "...-", "W": ".--",
                    "X": "-..-", "Y": "-.--", "Z": "--..",
                    "1": ".----", "2": "..---", "3": "...--",
                    "4": "....-", "5": ".....", "6": "-....",
                    "7": "--...", "8": "---..", "9": "----.",
                    "0": "-----"}


    for s in string.upper():
        print(MORSE[s])


def main():
    """
    write something here
    """
    args = sys.argv
    if len(args) != 2:
        print("AssertionError: the arguments are bad")
        return
    print(args)
    try:
        if isValidArg(args[1][0]) == False:
            print("AssertionError: the arguments are bad**not valid")
            return
        toMorse(args[1])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return



if __name__ == "__main__":
    main()
