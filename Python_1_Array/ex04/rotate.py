from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def to_gray(img: np.array) -> np.array:
    """
    returns a grayscaled image based on a given image,
    """
    return np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])


def ft_transpose(array: np.array) -> np.array:
    """
    returns an np.array after transpose of a given argument
    """
    if array.ndim == 3 and array.shape[2] == 1:
        array = array[:, :, 0]
    return array.T


def main():
    """
    loads the image "animal.jpeg", cuts a square part from
    it and grayscales it and transposes it.
    """
    image = ft_load("animal.jpeg")
    if image is None:
        return
    square_size = 400

    height = image.shape[0]
    width = image.shape[1]
    if height < square_size or width < square_size:
        raise ValueError("The image must be at least 400x400 pixels.")
    top = (height - square_size) // 2
    left = (width - square_size) // 2
    square = image[top:top + square_size, left:left + square_size]
    gray = to_gray(square)
    print(f"The shape of image is: {gray.shape}")
    print(gray[:, :, np.newaxis])

    transposed = ft_transpose(gray)
    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)

    plt.imshow(transposed, cmap="gray", vmin=0, vmax=255)
    plt.show()


if __name__ == "__main__":
    main()
