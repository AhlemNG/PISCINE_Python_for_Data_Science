import numpy as np
import PIL.Image as Image


def ft_load(path: str) -> np.array:
    """
    loads an image based on a given path
    prints its format and its content RGB
    returns an array of pixels
    """
    try:
        img = Image.open(path)
        img.show()
        img_arr = np.array(img)
        print("The shape of image is: ", img_arr.shape)
        pixels = np.array(img.getdata()) #image data to array
        return (pixels)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"Error while loading IMAGE: {e}")
    return None