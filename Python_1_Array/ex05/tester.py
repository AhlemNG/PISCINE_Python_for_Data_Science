from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey
from matplotlib import pyplot as plt
# array = ft_load("landscape.jpg")
# ft_invert(array)
# ft_red(array)
# ft_green(array)
# ft_blue(array)
# ft_grey(array)
# print(ft_invert.__doc__)

if __name__ == "__main__":
    array = ft_load("landscape.jpg")

    operations = [
        ("Original", lambda x: x),
        ("Invert", ft_invert),
        ("Red", ft_red),
        ("Green", ft_green),
        ("Blue", ft_blue),
        ("Grey", ft_grey),
    ]

    plt.figure(figsize=(15, 10))

    for i, (name, operation) in enumerate(operations, 1):
        result = operation(array)

        print(f"{name}: shape = {result.shape}")

        plt.subplot(2, 3, i)
        plt.imshow(result)
        plt.title(name)
        plt.axis("off")

    plt.tight_layout()
    plt.show()
