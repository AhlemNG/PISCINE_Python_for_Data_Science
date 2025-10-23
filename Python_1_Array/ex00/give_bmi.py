import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculates the list of BMI(s) based on two gives lists
    - height
    - weight
    returns a list of floats"""
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("arguments must be lists")
    if len(height) != len(weight):
        raise ValueError("arguments must have same length")
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("arguments must contain only ints or floats")
        if h <= 0:
            raise ValueError("height must be bigger then zero")
    height_array = np.array(height, dtype=float)
    weight_array = np.array(weight, dtype=float)
    bmi = weight_array / (height_array ** 2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    checks if a list of givem BIM(s) are above or under a gigen limit
    returns a list of booleans(true if above the limit)
    """
    if not isinstance(bmi, list):
        raise TypeError("argument must be a list")
    if not isinstance(limit, int):
        raise TypeError("argument must be an int")
    for b in bmi:
        if not isinstance(b, (int, float)):
            raise TypeError("values in the list must be ints or floats")
    bmi_array = np.array(bmi, dtype=float)
    result = bmi_array > limit

    return result.tolist()


# def main():
#     h = [1.80, 1.60, 1.75]
#     w = [75, 50, 100]
#     bmi_list = give_bmi(h, w)
#     print("BMI:", bmi_list)
#     print("Au-dessus de 25 ?", apply_limit(bmi_list, 25))

# if __name__ == "__main__":
#     main()
