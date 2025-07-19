import sys
from ft_filter import ft_filter


def longerThen(n):
    """
    returns a lamda function that checks if a word is onger than n characters
    """
    return lambda word: len(word) > n


def main():
    """
    write something here
    """
    args = sys.argv

    try:
        assert len(args) == 3
        S = args[1]
        N = int(args[2])
    except Exception:
        raise AssertionError("the arguments are bad")
    words = S.split()
    res = [word for word in ft_filter(longerThen(N), words)]
    print(res)


if __name__ == "__main__":
    main()
