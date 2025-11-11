import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


import numpy as np
import matplotlib.pyplot as plt

def to_gray(img: np.ndarray) ->np.array:
    """
    returns a grayscaled image based on a given image,
    """


    if img.ndim == 3:
        gray = img[:, :, 0] * 0.2989 + img[:, :, 1] * 0.5870 \
        + img[:, :, 2] * 0.1140
    else:
        gray = img
    return gray

def zoom_image(array: np.ndarray, y_start, y_end, x_start, x_end):
    """
    Zooms ap part of a given image using slicing methodand shows it with axes.
    """
    try:
        if array is None:
            raise ValueError("No image loaded.")
        zoomed = array[y_start:y_end, x_start:x_end]
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)
        plt.imshow(zoomed)
        plt.show()
    except Exception as e:
        print(f"Error while zooming: {e}")


def main():
    path = "animal.jpeg"
    img = to_gray(ft_load(path))

    if img is not None:
        h = img.shape[0]
        w = img.shape[1]
        zoom_image(img, h//4, h//4 + 400, w//4, w//4 + 400)

if __name__ == "__main__":
    main()
