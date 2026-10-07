import PIL.Image as Image
import numpy as np


def ft_load(path: str) -> np.array:
    """
    loads an image based on a given path
    prints its format and its content RGB
    returns an array of pixels
    """
    try:
        img = Image.open(path)
        img_arr = np.array(img)
        print(f"The shape of image is: {img_arr.shape}")
        return (img_arr)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"Error while loading IMAGE: {e}")
    return None


def main():
    print(ft_load("landscape.jpg"))
    print(ft_load("non_existent_image.jpg"))


if __name__ == "__main__":
    main()
