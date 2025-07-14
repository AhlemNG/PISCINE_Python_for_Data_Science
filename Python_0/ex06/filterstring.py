import sys


def main():
    """
    __doc_
    write something here"""
    args = sys.argv
    try:
        S = args[1]
        N = int(args[2])
    except AssertionError("he arguments are bad"):
        print("problem")
if __name__ == "__main__":
    main()