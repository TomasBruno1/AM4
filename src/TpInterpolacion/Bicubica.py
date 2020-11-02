import numpy as np
import matplotlib.pyplot as plt
import math

# Leer una imagen
img = plt.imread("test_1.jpg")


# Usando el algoritmo de convulación bicúbica obtenemos el peso de la siguiente forma
def weight(x):
    x = abs(x)
    if 0 <= x <= 1:
        return (-0.5 + 2) * (x ** 3) - (-0.5 + 3) * (x ** 2) + 1
    elif 1 < x <= 2:
        return -0.5 * (x ** 3) - (5 * -0.5) * (x ** 2) + (8 * -0.5) * x - 4 * -0.5
    return 0


def zoom_in_bicubic(img):
    # Obtener la dimensión de la imagen
    height, width, t = img.shape

    # Agrandamos la imagen y copiamos el borde para que no haya problemas en los bordes al hacer la interpolación
    temp_image = np.zeros((height + 4, width + 4, t))
    temp_image[2:height + 2, 2:width + 2, :t] = img
    temp_image[2:height + 2, 0:2, :t] = img[:, 0:1, :t]
    temp_image[height + 2:height + 4, 2:width + 2, :] = img[height - 1:height, :, :]
    temp_image[2:height + 2, width + 2:width + 4, :] = img[:, width - 1:width, :]
    temp_image[0:2, 2:width + 2, :t] = img[0:1, :, :t]
    temp_image[0:2, 0:2, :t] = img[0, 0, :t]
    temp_image[height + 2:height + 4, 0:2, :t] = img[height - 1, 0, :t]
    temp_image[height + 2:height + 4, width + 2:width + 4, :t] = img[height - 1, width - 1, :t]
    temp_image[0:2, width + 2:width + 4, :t] = img[0, width - 1, :t]

    # Tamaño nuevo
    new_height = math.floor(height * 2)
    new_width = math.floor(width * 2)
    t = 3

    # Creamos una imagen negra del doble de tamaño
    resized_image = np.zeros((new_height, new_width, 3))

    for c in range(t):
        for j in range(new_height):
            for i in range(new_width):
                # Buscamos las coordenadas en la imagen
                x = i / 2 + 2
                y = j / 2 + 2

                # Obtenemos los 4 de arriba y los 4 de abajo más cercanos
                x1 = 1 + x - math.floor(x)
                x2 = x - math.floor(x)
                x3 = math.floor(x) + 1 - x
                x4 = math.floor(x) + 2 - x
                y1 = 1 + y - math.floor(y)
                y2 = y - math.floor(y)
                y3 = math.floor(y) + 1 - y
                y4 = math.floor(y) + 2 - y

                # Obtenemos el peso de los 4x4 más cercanos para hacer la ponderación
                weight_left = np.asarray([[weight(x1), weight(x2), weight(x3), weight(x4)]])
                weight_right = np.asarray([[weight(y1)], [weight(y2)], [weight(y3)], [weight(y4)]])

                # Obtenemos los 4x4 más cercanos para hacer la ponderación
                matrix_closest = np.asarray(
                    [[temp_image[int(y - y1), int(x - x1), c], temp_image[int(y - y2), int(x - x1), c],
                      temp_image[int(y + y3), int(x - x1), c], temp_image[int(y + y4), int(x - x1), c]],
                     [temp_image[int(y - y1), int(x - x2), c], temp_image[int(y - y2), int(x - x2), c],
                      temp_image[int(y + y3), int(x - x2), c], temp_image[int(y + y4), int(x - x2), c]],
                     [temp_image[int(y - y1), int(x + x3), c], temp_image[int(y - y2), int(x + x3), c],
                      temp_image[int(y + y3), int(x + x3), c], temp_image[int(y + y4), int(x + x3), c]],
                     [temp_image[int(y - y1), int(x + x4), c], temp_image[int(y - y2), int(x + x4), c],
                      temp_image[int(y + y3), int(x + x4), c], temp_image[int(y + y4), int(x + x4), c]]])

                # Interpola la imagen con los 4x4 más cercanos
                pixel = np.dot(np.dot(weight_left, matrix_closest), weight_right)

                # Asignamos el valor al pixel
                resized_image[j, i, c] = pixel

    # Mostramos la imagen en pantalla
    plt.imshow(resized_image, vmin=0, vmax=1)
    plt.show()


zoom_in_bicubic(img)


def zoom_out_bicubic(img):
    # Obtener la dimensión de la imagen
    height, width, t = img.shape

    # Agrandamos la imagen y copiamos el borde para que no haya problemas en los bordes al hacer la interpolación
    temp_img = np.zeros((height + 4, width + 4, t))
    temp_img[2:height + 2, 2:width + 2, :t] = img
    temp_img[2:height + 2, 0:2, :t] = img[:, 0:1, :t]
    temp_img[height + 2:height + 4, 2:width + 2, :] = img[height - 1:height, :, :]
    temp_img[2:height + 2, width + 2:width + 4, :] = img[:, width - 1:width, :]
    temp_img[0:2, 2:width + 2, :t] = img[0:1, :, :t]
    temp_img[0:2, 0:2, :t] = img[0, 0, :t]
    temp_img[height + 2:height + 4, 0:2, :t] = img[height - 1, 0, :t]
    temp_img[height + 2:height + 4, width + 2:width + 4, :t] = img[height - 1, width - 1, :t]
    temp_img[0:2, width + 2:width + 4, :t] = img[0, width - 1, :t]

    # Tamaño nuevo
    new_height = math.floor(height // 2)
    new_width = math.floor(width // 2)
    t = 3

    # Creamos una imagen negra de la mitad del tamaño
    resized_image = np.zeros((new_height, new_width, 3))

    for c in range(t):
        for j in range(new_height):
            for i in range(new_width):
                # Buscamos las coordenadas en la imagen
                x = i * 2 + 2
                y = j * 2 + 2

                x1 = 1 + x - math.floor(x)
                x2 = x - math.floor(x)
                x3 = math.floor(x) + 1 - x
                x4 = math.floor(x) + 2 - x
                y1 = 1 + y - math.floor(y)
                y2 = y - math.floor(y)
                y3 = math.floor(y) + 1 - y
                y4 = math.floor(y) + 2 - y

                # Obtenemos el peso de los 4x4 más cercanos para hacer la ponderación
                weight_left = np.asarray([[weight(x1), weight(x2), weight(x3), weight(x4)]])
                weight_right = np.asarray([[weight(y1)], [weight(y2)], [weight(y3)], [weight(y4)]])

                # Obtenemos los 4x4 más cercanos para hacer la ponderación
                matrix_closest = np.asarray(
                    [[temp_img[int(y - y1), int(x - x1), c], temp_img[int(y - y2), int(x - x1), c],
                      temp_img[int(y + y3), int(x - x1), c], temp_img[int(y + y4), int(x - x1), c]],
                     [temp_img[int(y - y1), int(x - x2), c], temp_img[int(y - y2), int(x - x2), c],
                      temp_img[int(y + y3), int(x - x2), c], temp_img[int(y + y4), int(x - x2), c]],
                     [temp_img[int(y - y1), int(x + x3), c], temp_img[int(y - y2), int(x + x3), c],
                      temp_img[int(y + y3), int(x + x3), c], temp_img[int(y + y4), int(x + x3), c]],
                     [temp_img[int(y - y1), int(x + x4), c], temp_img[int(y - y2), int(x + x4), c],
                      temp_img[int(y + y3), int(x + x4), c], temp_img[int(y + y4), int(x + x4), c]]])

                # Interpola la imagen con los 4x4 más cercanos
                pixel = np.dot(np.dot(weight_left, matrix_closest), weight_right)

                # Asignamos el valor al pixel
                resized_image[j, i, c] = pixel

    # Mostramos la imagen en pantalla
    plt.imshow(resized_image, vmin=0, vmax=1)
    plt.show()


zoom_out_bicubic(img)
