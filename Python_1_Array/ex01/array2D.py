import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    prints the shape of a given 2D array and truncates it
    based on given start and end.
    returns a truncated array
    """
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Argument must be an int")
    if not isinstance(family, list):
        raise TypeError("Argument must be a list")
    length = len(family[0])
    for lst in family:
        if not isinstance(lst, list):
            raise TypeError("list elements must be of type list")
        if len(lst) != length:
            raise IndexError("lists must have same length")
        for ls in lst:
            if not isinstance(ls, int | float):
                raise TypeError("list elements must be of type int")
    print("My shape is : ", (len(family), len(family[0])))
    arr = np.array(family)
    new_f = arr[start:end]
    return new_f.tolist()
