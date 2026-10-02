from load_image import ft_load
import numpy as np


def to_gray(image: np.ndarray) -> np.ndarray:
    """Convert an RGB image to grayscale."""
    if image.ndim == 2:
        return image
    if image.ndim == 3 and image.shape[2] == 1:
        return image[:, :, 0]
    if image.ndim == 3 and image.shape[2] >= 3:
        return np.dot(image[:, :, :3], [0.299, 0.587, 0.114]).astype(np.uint8)
    raise ValueError("Expected a grayscale or RGB image.")


def ft_transpose(array: np.array) -> np.array:
    """
    returns an np.array after transpose of a given argument
    """
    if array.ndim == 3 and array.shape[2] == 1:
        array = array[:, :, 0]
    return array.T


def main():
    import matplotlib.pyplot as plt

    image = ft_load("animal.jpeg")
    if image is None:
        return

    gray = to_gray(image)
    height, width = gray.shape
    square_size = 400
    if height < square_size or width < square_size:
        raise ValueError("The image must be at least 400x400 pixels.")

    top = (height - square_size) // 2
    left = (width - square_size) // 2
    square = gray[top:top + square_size, left:left + square_size]
    print(f"New shape after crop: {square.shape}")
    print(square[:, :, np.newaxis])

    transposed = ft_transpose(square)
    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)

    plt.imshow(transposed, cmap="gray", vmin=0, vmax=255)
    plt.show()


if __name__ == "__main__":
    main()
