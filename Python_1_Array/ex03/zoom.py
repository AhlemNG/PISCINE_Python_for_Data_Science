import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load

def zoom_image(array: np.ndarray, y_start, y_end, x_start, x_end):
    """
    Zoom sur une zone de l'image (slicing) et affichage avec axes.
    """
    try:
        if array is None:
            raise ValueError("No image loaded.")

        # Découpage (slicing)
        zoomed = array[y_start:y_end, x_start:x_end]

        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)  # affichage du contenu du zoom

        # Affichage avec axes
        plt.imshow(zoomed)
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()

    except Exception as e:
        print(f"Error while zooming: {e}")


def main():
    path = "animal.jpeg"
    img = ft_load(path)
    if img is not None:
        # Exemple de zoom au centre (ajuste selon ton image)
        h, w = img.shape[:2]
        zoom_image(img, h//4, h//4 + 400, w//4, w//4 + 400)


if __name__ == "__main__":
    main()
