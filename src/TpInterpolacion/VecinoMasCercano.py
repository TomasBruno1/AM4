import numpy as np
import matplotlib.pyplot as plt

# Leer una imagen
img = plt.imread("test_1.jpg")


# Interpolar valores desconocidos
def zoom_in_closest(img):
    # Obtener la dimensión de la imagen
    height, width, t = img.shape

    print(img.shape)

    # Tamaño nuevo
    new_width = width * 2
    new_height = height * 2

    # Creamos una imagen negra del doble de tamaño
    resized_image = np.zeros((new_height, new_width, t))

    # Interpola la imagen con los mas cercanos
    for i in range(new_width):
        for j in range(new_height):
            resized_image[i, j] = img[i // 2, j // 2]
            for k in range(3):
                if (resized_image[i, j][k] >= 1): resized_image[i, j][k] = 1
                if (resized_image[i, j][k] <= 0): resized_image[i, j][k] = 0

    # Guardamos la imagen en disco
    plt.imsave('test_bigger_closest.png', resized_image)

    # Mostramos la imagen en pantalla
    plt.imshow(resized_image, vmin=0, vmax=1)
    plt.show()
    return resized_image


zoom_in_closest(img)


def zoom_out_closest(img):
    # Obtener la dimensión de la imagen
    height, width, t = img.shape

    print(img.shape)

    # Tamaño nuevo
    new_width = width // 2
    new_height = height // 2

    # Creamos una imagen negra del doble de tamaño
    resized_image = np.zeros((new_height, new_width, t))

    # Interpola la imagen con los mas cercanos
    for i in range(new_width):
        for j in range(new_height):
            resized_image[i, j] = img[i * 2, j * 2]
            for k in range(3):
                if (resized_image[i, j][k] >= 1): resized_image[i, j][k] = 1
                if (resized_image[i, j][k] <= 0): resized_image[i, j][k] = 0

    # Guardamos la imagen en disco
    plt.imsave('test_smaller_closest.png', resized_image)

    # Mostramos la imagen en pantalla
    plt.imshow(resized_image, vmin=0, vmax=1)
    plt.show()
    return resized_image


img = zoom_out_closest(img)
