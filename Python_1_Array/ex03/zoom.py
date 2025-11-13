import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load

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
    except Exception as e:
        print(f"Error while zooming: {e}")

def zoom_image(array: np.ndarray):
    """
    Zooms ap part of a given image using slicing methodand shows it with axes.
    """
    try:
        if array is None:
            raise ValueError("No image loaded.")
        h = array.shape[0]
        w = array.shape[1]
        zoomed = array[h//4:h//4 + 400, w//4:w//4 + 400]
        print(f"New shape after slicing: {zoomed.shape}")
        return(zoomed)
    except Exception as e:
        print("an error occurred: ", e)


def main():
    path = "animal.jpeg"
    img = ft_load(path)
    if img is not None:
        print(img)
        gray = to_gray(img)
        zoomed = zoom_image(gray)
        print(zoomed)

        plt.imshow(zoomed, cmap='gray', vmin=0, vmax=255)
        plt.show()
        
if __name__ == "__main__":
    main()
