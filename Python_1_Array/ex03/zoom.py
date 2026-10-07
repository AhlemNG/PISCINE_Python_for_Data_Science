import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
from load_image import ft_load

def to_gray(img: np.array) -> np.array:
    """
    returns a grayscaled image based on a given image,
    """
    return np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])


def zoom_image(array: np.array):
    """
    Zooms a part of a given image using slicing methodand shows it with axes.
    """
    try:
        if array is None:
            raise ValueError("No image loaded.")
        h = array.shape[0]
        w = array.shape[1]
        zoomed = array[h//4:h//4 + 400, w//4:w//4 + 400]
        print(f"New shape after slicing: {zoomed.shape}")
        return (zoomed)
    except Exception as e:
        print("an error occurred: ", e)


def main():
    path = "animal.jpeg"
    img = ft_load(path)
    if img is not None:
        print(f"The shape of image is: {img.shape}")
        print(img)
        gray = to_gray(img)
        zoomed = zoom_image(gray)
        print(zoomed)

        plt.imshow(zoomed, cmap=plt.get_cmap('gray'))
        plt.show()


if __name__ == "__main__":
    main()
