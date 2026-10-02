import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    prints the shape of a given 2D array and truncates it
    based on given start and end.
    returns a truncated array
    """
    try:
        if not isinstance(family, list):
            raise TypeError("Argument must be a list")
        if not family:
            raise IndexError("Argument must not be empty")
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("Argument must be an int")
        length = len(family[0])
        for lst in family:
            if not isinstance(lst, list):
                raise TypeError("list elements must be of type list")
            if len(lst) != length:
                raise IndexError("lists must have same length")
            for ls in lst:
                if not isinstance(ls, int | float):
                    raise TypeError("list elements must be of type int")
    except (TypeError, IndexError) as e:
        print(e)
        return
    arr = np.array(family)
    print("My shape is : ", arr.shape)
    new_f = arr[start:end]
    print("My new shape is : ", new_f.shape)
    return new_f.tolist()


if __name__ == "__main__":
    print(slice_me([[1, 2, 3], [4, 5, 6]], 0, 1))
    print(slice_me([], 0, 1))
