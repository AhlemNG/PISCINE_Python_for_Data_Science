import numpy as np
from PIL import Image

def ft_load(path: str) -> np.ndarray:
    """
    loads an image based on a given path
    prints its format and its content RGB
    returns an array of pixels
    """
    try:
        img = Image.open(path)
        img_arr = np.array(img) #ici image to array

        print(f"The shape of image is: {img_arr.shape}")
        # print(img_arr)
        pixels = np.array(img.getdata()) #image data to array
        print(pixels)
        # return (pixels)
        return img_arr
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"Error while loading IMAGE: {e}")
    return None
