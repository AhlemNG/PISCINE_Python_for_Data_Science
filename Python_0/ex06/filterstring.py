import sys
from ft_filter import ft_filter


def longerThen(n):
    """
    returns a lamda function that checks if a word is onger than n characters
    """
    return lambda word: len(word) >= n


def main():
    """
    write something here
    """
    args = sys.argv

    if len(args) != 3:
        print("AssertionError: the arguments are bad")
        return
    S = args[1]
    try:
        N = int(args[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return
    words = S.split()
    res = [word for word in ft_filter(longerThen(N), words)]
    print(res)


if __name__ == "__main__":
    main()
