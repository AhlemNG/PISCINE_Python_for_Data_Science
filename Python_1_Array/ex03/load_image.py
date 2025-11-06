from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """
    Charge une image et affiche ses infos.
    Retourne l'image sous forme de tableau numpy.
    """
    try:
        img = Image.open(path)
        array = np.array(img)

        print(f"The shape of image is: {array.shape}")
        print(array)  # affichage du contenu (partiel si trop grand)

        return array
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"Error while loading image: {e}")

    return None
