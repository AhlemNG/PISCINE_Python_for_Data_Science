import sys


def Chars_Sum(string):
    """calculate sum of different character types in a string"""
    upper = lower = punct = digits = spaces = 0
    for character in string:
        if character.isupper():
            upper += 1
        elif character.islower():
            lower += 1
        elif character.isdigit():
            digits += 1
        elif character.isspace():
            spaces += 1
        else:
            punct += 1
    print(f"The text contains {len(string)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """Entry point of the program.
    Reads the command-line argument and passes it to `Chars_Sum`
    for character counting analysis."""
    args = sys.argv
    try:
        if len(args) == 1:
            print("What is the text to count?")
            text = sys.stdin.readline()
            Chars_Sum(text)
        elif len(args) == 2:
            Chars_Sum(args[1])
        else:
            raise AssertionError("more than one argument are provided")
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
