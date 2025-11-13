import numpy as np
import matplotlib.pyplot as mpl


def ft_load(path: str) -> np.array:
    """
    loads an image based on a given path
    prints its format and its content RGB
    returns an array of pixels
    """
    try:
        img = mpl.imread(path)
        print("The shape of image is: ", img.shape)
        return (img)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"Error while loading IMAGE: {e}")
    return None
