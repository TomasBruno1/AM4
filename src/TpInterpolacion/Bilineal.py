import numpy as np
import matplotlib.pyplot as plt

# Leer una imagen
img = plt.imread("test_1.jpg")


# Interpolar valores desconocidos
def zoom_in_bilineal(array_in):
    # Obtener la dimensión de la imagen
    height_in, width_in, t = img.shape
    t = 3

    # Tamaño nuevo
    width_out = width_in * 2
    height_out = height_in * 2

    # Creamos una imagen negra del doble de tamaño
    array_out = np.zeros((height_out, width_out, t))

    for i in range(height_out):
        for j in range(width_out):
            # Relative coordinates of the pixel in output space
            x_out = j / width_out
            y_out = i / height_out

            # Corresponding absolute coordinates of the pixel in input space
            x_in = (x_out * width_in)
            y_in = (y_out * height_in)

            # Nearest neighbours coordinates in input space
            x_prev = int(np.floor(x_in))
            x_next = x_prev + 1
            y_prev = int(np.floor(y_in))
            y_next = y_prev + 1

            # Sanitize bounds - no need to check for < 0
            x_prev = min(x_prev, width_in - 1)
            x_next = min(x_next, width_in - 1)
            y_prev = min(y_prev, height_in - 1)
            y_next = min(y_next, height_in - 1)

            # Distances between neighbour nodes in input space
            Dy_next = y_next - y_in
            Dy_prev = 1. - Dy_next  # because next - prev = 1
            Dx_next = x_next - x_in
            Dx_prev = 1. - Dx_next  # because next - prev = 1

            # Interpolate over 3 RGB layers
            for c in range(3):
                array_out[i][j][c] = Dy_prev * (
                        array_in[y_next][x_prev][c] * Dx_next + array_in[y_next][x_next][c] * Dx_prev) \
                                     + Dy_next * (array_in[y_prev][x_prev][c] * Dx_next + array_in[y_prev][x_next][c]
                                                  * Dx_prev)

    # Guardamos la imagen en disco
    plt.imsave('test_bigger.png', array_out)

    # Mostramos la imagen en pantalla
    plt.imshow(array_out, vmin=0, vmax=1)
    plt.show()


zoom_in_bilineal(img)


def zoom_out_bilineal(array_in):
    # Obtener la dimensión de la imagen
    height_in, width_in, t = img.shape
    t = 3

    # Tamaño nuevo
    width_out = width_in // 2
    height_out = height_in // 2

    # Creamos una imagen negra del doble de tamaño
    array_out = np.zeros((height_out, width_out, t))

    for i in range(height_out):
        for j in range(width_out):
            # Relative coordinates of the pixel in output space
            x_out = j / width_out
            y_out = i / height_out

            # Corresponding absolute coordinates of the pixel in input space
            x_in = (x_out * width_in)
            y_in = (y_out * height_in)

            # Nearest neighbours coordinates in input space
            x_prev = int(np.floor(x_in))
            x_next = x_prev + 1
            y_prev = int(np.floor(y_in))
            y_next = y_prev + 1

            # Sanitize bounds - no need to check for < 0
            x_prev = min(x_prev, width_in - 1)
            x_next = min(x_next, width_in - 1)
            y_prev = min(y_prev, height_in - 1)
            y_next = min(y_next, height_in - 1)

            # Distances between neighbour nodes in input space
            Dy_next = y_next - y_in
            Dy_prev = 1. - Dy_next  # because next - prev = 1
            Dx_next = x_next - x_in
            Dx_prev = 1. - Dx_next  # because next - prev = 1

            # Interpolate over 3 RGB layers
            for c in range(3):
                array_out[i][j][c] = Dy_prev * (
                        array_in[y_next][x_prev][c] * Dx_next + array_in[y_next][x_next][c] * Dx_prev) \
                                     + Dy_next * (array_in[y_prev][x_prev][c] * Dx_next + array_in[y_prev][x_next][c]
                                                  * Dx_prev)

    # Guardamos la imagen en disco
    plt.imsave('test_bigger.png', array_out)

    # Mostramos la imagen en pantalla
    plt.imshow(array_out, vmin=0, vmax=1)
    plt.show()


zoom_out_bilineal(img)
