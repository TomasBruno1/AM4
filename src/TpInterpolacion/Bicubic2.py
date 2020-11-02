import math
import numpy as np
import matplotlib.pyplot as plt
import sys


# Bicubic operation
def bicubic(image, ratio, a):
    # Get image size
    H, W, C = image.shape

    zimg = np.zeros((H + 4, W + 4, C))
    zimg[2:H + 2, 2:W + 2, :C] = img
    # Pad the first/last two col and row
    zimg[2:H + 2, 0:2, :C] = img[:, 0:1, :C]
    zimg[H + 2:H + 4, 2:W + 2, :] = img[H - 1:H, :, :]
    zimg[2:H + 2, W + 2:W + 4, :] = img[:, W - 1:W, :]
    zimg[0:2, 2:W + 2, :C] = img[0:1, :, :C]
    # Pad the missing eight points
    zimg[0:2, 0:2, :C] = img[0, 0, :C]
    zimg[H + 2:H + 4, 0:2, :C] = img[H - 1, 0, :C]
    zimg[H + 2:H + 4, W + 2:W + 4, :C] = img[H - 1, W - 1, :C]
    zimg[0:2, W + 2:W + 4, :C] = img[0, W - 1, :C]

    image = zimg

    C = 3
    # Create new image
    dH = math.floor(H * ratio)
    dW = math.floor(W * ratio)
    dst = np.zeros((dH, dW, 3))

    h = 1 / ratio

    for c in range(C):
        for j in range(dH):
            for i in range(dW):
                x, y = i * h + 2, j * h + 2

                x1 = 1 + x - math.floor(x)
                x2 = x - math.floor(x)
                x3 = math.floor(x) + 1 - x
                x4 = math.floor(x) + 2 - x

                y1 = 1 + y - math.floor(y)
                y2 = y - math.floor(y)
                y3 = math.floor(y) + 1 - y
                y4 = math.floor(y) + 2 - y

                mat_l = np.matrix([[u(x1, a), u(x2, a), u(x3, a), u(x4, a)]])
                mat_m = np.matrix([[image[int(y - y1), int(x - x1), c], image[int(y - y2), int(x - x1), c],
                                    image[int(y + y3), int(x - x1), c], image[int(y + y4), int(x - x1), c]],
                                   [image[int(y - y1), int(x - x2), c], image[int(y - y2), int(x - x2), c],
                                    image[int(y + y3), int(x - x2), c], image[int(y + y4), int(x - x2), c]],
                                   [image[int(y - y1), int(x + x3), c], image[int(y - y2), int(x + x3), c],
                                    image[int(y + y3), int(x + x3), c], image[int(y + y4), int(x + x3), c]],
                                   [image[int(y - y1), int(x + x4), c], image[int(y - y2), int(x + x4), c],
                                    image[int(y + y3), int(x + x4), c], image[int(y + y4), int(x + x4), c]]])
                mat_r = np.matrix([[u(y1, a)], [u(y2, a)], [u(y3, a)], [u(y4, a)]])
                pixel = np.dot(np.dot(mat_l, mat_m), mat_r)
                dst[j, i, c] = pixel
    return dst


# Paddnig
def padding(img, H, W, C):
    zimg = np.zeros((H + 4, W + 4, C))
    zimg[2:H + 2, 2:W + 2, :C] = img
    # Pad the first/last two col and row
    zimg[2:H + 2, 0:2, :C] = img[:, 0:1, :C]
    zimg[H + 2:H + 4, 2:W + 2, :] = img[H - 1:H, :, :]
    zimg[2:H + 2, W + 2:W + 4, :] = img[:, W - 1:W, :]
    zimg[0:2, 2:W + 2, :C] = img[0:1, :, :C]
    # Pad the missing eight points
    zimg[0:2, 0:2, :C] = img[0, 0, :C]
    zimg[H + 2:H + 4, 0:2, :C] = img[H - 1, 0, :C]
    zimg[H + 2:H + 4, W + 2:W + 4, :C] = img[H - 1, W - 1, :C]
    zimg[0:2, W + 2:W + 4, :C] = img[0, W - 1, :C]
    return zimg

def u(s, a):
    if (abs(s) >= 0) & (abs(s) <= 1):
        return (a + 2) * (abs(s) ** 3) - (a + 3) * (abs(s) ** 2) + 1
    elif (abs(s) > 1) & (abs(s) <= 2):
        return a * (abs(s) ** 3) - (5 * a) * (abs(s) ** 2) + (8 * a) * abs(s) - 4 * a
    return 0


def zoom_in_bicubic(image):
    return bicubic(image, 2, -0.5)


def zoom_out_bicubic(image):
    return bicubic(image, 0.5, -0.5)


# Leer una imagen
img = plt.imread("test_3.jpg")
bigger = zoom_in_bicubic(img)
smaller = zoom_out_bicubic(img)

# Mostramos la imagen en pantalla
plt.imshow(bigger, vmin=0, vmax=1)
plt.show()
plt.imshow(smaller, vmin=0, vmax=1)
plt.show()
