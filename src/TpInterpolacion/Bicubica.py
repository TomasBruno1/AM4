import numpy as np
import matplotlib.pyplot as plt

# Leer una imagen
img = plt.imread("test_1.jpg")


def S(x):
    x = np.abs(x)
    if 0 <= x < 1:
        return 1 - 2 * x * x + x * x * x
    if 1 <= x < 2:
        return 4 - 8 * x + 5 * x * x - x * x * x
    else:
        return 0


def zoom_in_bicubic(img):
    height, width, channels = img.shape
    m = height * 2
    n = width * 2
    array_out = np.zeros((m, n, 3))
    sh = m / height
    sw = n / width
    for i in range(m):
        for j in range(n):
            x = i / sh
            y = j / sw
            p = (i + 0.0) / sh - x
            q = (j + 0.0) / sw - y
            x = int(x) - 2
            y = int(y) - 2
            A = np.array([
                [S(1 + p), S(p), S(1 - p), S(2 - p)]
            ])
            if x >= m - 3:
                m - 1
            if y >= n - 3:
                n - 1
            if 1 <= x <= (m - 3) and 1 <= y <= (n - 3):
                B = np.array([
                    [img[x - 1, y - 1], img[x - 1, y],
                     img[x - 1, y + 1],
                     img[x - 1, y + 1]],
                    [img[x, y - 1], img[x, y],
                     img[x, y + 1], img[x, y + 2]],
                    [img[x + 1, y - 1], img[x + 1, y],
                     img[x + 1, y + 1], img[x + 1, y + 2]],
                    [img[x + 2, y - 1], img[x + 2, y],
                     img[x + 2, y + 1], img[x + 2, y + 1]],

                ])
                C = np.array([
                    [S(1 + q)],
                    [S(q)],
                    [S(1 - q)],
                    [S(2 - q)]
                ])
                blue = np.dot(np.dot(A, B[:, :, 0]), C)[0, 0]
                green = np.dot(np.dot(A, B[:, :, 1]), C)[0, 0]
                red = np.dot(np.dot(A, B[:, :, 2]), C)[0, 0]

                array_out[i, j] = [blue, green, red]
    # Guardamos la imagen en disco
    plt.imsave('test_bigger_bicubic.png', array_out)

    # Mostramos la imagen en pantalla
    plt.imshow(array_out, vmin=0, vmax=1)
    plt.show()


zoom_in_bicubic(img)


def zoom_out_bicubic(img):
    height, width, channels = img.shape
    m = height // 2
    n = width // 2
    array_out = np.zeros((m, n, 3))
    sh = m / height
    sw = n / width
    for i in range(m):
        for j in range(n):
            x = i / sh
            y = j / sw
            p = (i + 0.0) / sh - x
            q = (j + 0.0) / sw - y
            x = int(x) - 2
            y = int(y) - 2
            A = np.array([
                [S(1 + p), S(p), S(1 - p), S(2 - p)]
            ])
            if x >= m - 3:
                m - 1
            if y >= n - 3:
                n - 1
            if 1 <= x <= (m - 3) and 1 <= y <= (n - 3):
                B = np.array([
                    [img[x - 1, y - 1], img[x - 1, y],
                     img[x - 1, y + 1],
                     img[x - 1, y + 1]],
                    [img[x, y - 1], img[x, y],
                     img[x, y + 1], img[x, y + 2]],
                    [img[x + 1, y - 1], img[x + 1, y],
                     img[x + 1, y + 1], img[x + 1, y + 2]],
                    [img[x + 2, y - 1], img[x + 2, y],
                     img[x + 2, y + 1], img[x + 2, y + 1]],

                ])
                C = np.array([
                    [S(1 + q)],
                    [S(q)],
                    [S(1 - q)],
                    [S(2 - q)]
                ])
                blue = np.dot(np.dot(A, B[:, :, 0]), C)
                green = np.dot(np.dot(A, B[:, :, 1]), C)
                red = np.dot(np.dot(A, B[:, :, 2]), C)

                array_out[i, j] = [blue, green, red]
    # Guardamos la imagen en disco
    plt.imsave('test_smaller_bicubic.png', array_out)

    # Mostramos la imagen en pantalla
    plt.imshow(array_out, vmin=0, vmax=1)
    plt.show()


zoom_out_bicubic(img)
