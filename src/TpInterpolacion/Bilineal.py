import numpy as np
import matplotlib.pyplot as plt

# Leer una imagen
img = plt.imread("test_1.jpg")


# Interpolar valores desconocidos
def zoom_in_bilineal(array_in):
    # Obtener la dimensión de la imagen
    height, width, t = img.shape
    t = 3

    # Tamaño nuevo
    new_width = width * 2
    new_height = height * 2

    # Creamos una imagen negra del doble de tamaño
    resized_image = np.zeros((new_height, new_width, t))

    for i in range(new_height):
        for j in range(new_width):
            # Obtenemos la posicion relativa en la nueva imagen
            new_x = j / new_width
            new_y = i / new_height

            # Buscamos las coordenadas reales en la imagen
            x = (new_x * width)
            y = (new_y * height)

            # Obtenemos los 2x2 más cercanos
            x1 = int(np.floor(x))
            x2 = x1 + 1
            y1 = int(np.floor(y))
            y2 = y1 + 1

            # Corregimos en caso de que se pase
            x1 = min(x1, width - 1)
            x2 = min(x2, width - 1)
            y1 = min(y1, height - 1)
            y2 = min(y2, height - 1)

            # Interpola la imagen con los 2x2 mas cercanos
            for k in range(3):
                resized_image[i][j][k] = (1. - (y2 - y)) * (
                        array_in[y2][x1][k] * (x2 - x) + array_in[y2][x2][k] * (1. - (x2 - x))) \
                                         + (y2 - y) * (array_in[y1][x1][k] * (x2 - x) + array_in[y1][x2][k]
                                                       * (1. - (x2 - x)))

    # Guardamos la imagen en disco
    plt.imsave('test_bigger_bilineal.png', resized_image)

    # Mostramos la imagen en pantalla
    print('Zoom in bilineal')
    plt.imshow(resized_image, vmin=0, vmax=1)
    plt.show()


zoom_in_bilineal(img)


def zoom_out_bilineal(array_in):
    # Obtener la dimensión de la imagen
    height, width, t = img.shape
    t = 3

    # Tamaño nuevo
    new_width = width // 2
    new_height = height // 2

    # Creamos una imagen negra de la mitad del tamaño
    resized_image = np.zeros((new_height, new_width, t))

    for i in range(new_height):
        for j in range(new_width):
            # Obtenemos la posicion relativa en la nueva imagen
            new_x = j / new_width
            new_y = i / new_height

            # Buscamos las coordenadas reales en la imagen
            x = (new_x * width)
            y = (new_y * height)

            # Obtenemos los 2x2 más cercanos
            x1 = int(np.floor(x))
            x2 = x1 + 1
            y1 = int(np.floor(y))
            y2 = y1 + 1

            # Corregimos en caso de que se pase
            x1 = min(x1, width - 1)
            x2 = min(x2, width - 1)
            y1 = min(y1, height - 1)
            y2 = min(y2, height - 1)

            # Interpola la imagen con los 2x2 mas cercanos
            for k in range(3):
                resized_image[i][j][k] = (1. - (y2 - y)) * (
                        array_in[y2][x1][k] * (x2 - x) + array_in[y2][x2][k] * (1. - (x2 - x))) \
                                         + (y2 - y) * (array_in[y1][x1][k] * (x2 - x) + array_in[y1][x2][k]
                                                       * (1. - (x2 - x)))

    # Guardamos la imagen en disco
    plt.imsave('test_smaller_bilineal.png', resized_image)

    # Mostramos la imagen en pantalla
    print('Zoom out bilineal')
    plt.imshow(resized_image, vmin=0, vmax=1)
    plt.show()


zoom_out_bilineal(img)
