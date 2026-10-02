from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def check_array(array):
    """Check that the input is a valid RGB image."""
    if not isinstance(array, np.ndarray):
        raise TypeError("Input must be a numpy.ndarray")
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("Input must be an RGB image")
    if array.dtype != np.uint8:
        raise TypeError("Input must contain uint8 pixel values")


def ft_invert(array) -> np.ndarray:
    """Invert the colors of the image."""
    check_array(array)
    return 255 - array


def ft_red(array) -> np.ndarray:
    """Keep only the red channel."""
    check_array(array)
    result = array.copy()
    result[:, :, 1] = 0
    result[:, :, 2] = 0
    return result


def ft_green(array) -> np.ndarray:
    """Keep only the green channel."""
    check_array(array)
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 2] = 0
    return result


def ft_blue(array) -> np.ndarray:
    """Keep only the blue channel."""
    check_array(array)
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    return result


def ft_grey(array) -> np.ndarray:
    """Convert the image to grayscale."""
    check_array(array)
    grey = (
        0.299 * array[:, :, 0]
        + 0.587 * array[:, :, 1]
        + 0.114 * array[:, :, 2]
    )
    grey = grey.astype(array.dtype)
    return np.repeat(grey[:, :, np.newaxis], 3, axis=2)


if __name__ == "__main__":
    array = ft_load("landscape.jpg")

    inverted = ft_invert(array)

    print("Original shape:", array.shape)
    print("Inverted shape:", inverted.shape)

    plt.imshow(inverted)
    plt.title("Inverted Image")
    plt.show()


def ft_render(original, modified):
    """Render original and modified images side by side."""
    check_array(original)
    check_array(modified)

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(modified)
    plt.title("Modified")
    plt.axis("off")

    plt.show()
