import numpy as np
import PIL.Image as Image


def ft_load(path: str) -> list:
    """
    loads an image based on a given path
    prints its format and its content RGB
    returns an array of pixels
    """
    img = Image.open(path)
    img.show()
    img_arr = np.array(img)
    print("The shape of image is: ", img_arr.shape)
    pixels = np.array(img.getdata())
    return (pixels)
