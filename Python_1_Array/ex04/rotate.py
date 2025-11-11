from load_image import ft_load
import numpy as np

def ft_transpose(array: np.array) -> np.array:
    """
    returns an np.array after transpose of a given argument
    """
    # tab = [[0, 1, 2, 3], 
    #        [4, 5, 6, 7], 
    #        [8, 9, 10, 11]]

    # tab-transp = [[0, 4, 8], [1, 5, 9], [2, 6, 10], [3, 7, 11]]

    y = array.shape[0]
    x = array.shape[1]
    



def main():
    print("this is main")
    ft_load("animal.jpeg")

if __name__ == "__main__":
    main()