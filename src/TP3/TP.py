import numpy as np
import csv
import matplotlib.pyplot as plt
import math

#
# def dTdt(x, y, Tm):
#     return -0.25 * (y - Tm)
#
#
# def rungeKutta(x0, y0, x, h, Tm):
#     n = (int)((x - x0) / h)
#     y = y0
#     for i in range(1, n + 1):
#         k1 = h * dTdt(x0, y, ambientT)
#         k2 = h * dTdt(x0 + 0.5 * h, y + 0.5 * k1, ambientT)
#         k3 = h * dTdt(x0 + 0.5 * h, y + 0.5 * k2, ambientT)
#         k4 = h * dTdt(x0 + h, y + k3, ambientT)
#         y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
#         x0 = x0 + h
#     return y
#
#
# arrayArchivos = ["temperaturas_horno.csv", "tempEnT1.csv", "tempEnT2.csv", "tempEnT3.csv",
#                  "tempEnT4.csv", "tempEnT5.csv", "tempEnT6.csv", "tempEnT7.csv",
#                  "tempEnT8.csv", "tempEnT9.csv", "tempEnT10.csv"]
#
# for k in range(1, len(arrayArchivos)):
#
#     with open(arrayArchivos[k - 1], 'r') as file:
#         array = np.loadtxt(file, delimiter=",")
#
#         for i in range(1, len(array[0]) - 1):
#             for j in range(1, len(array[i]) - 1):
#                 ambientT = (array[i - 1][j - 1] + array[i - 1][j] + array[i - 1][j + 1] + array[i][j - 1] +
#                             array[i + 1][
#                                 j - 1] + array[i][j + 1] + array[i + 1][j] + array[i + 1][j + 1]) / 8
#                 array[i][j] = rungeKutta(0, array[i][j], 1, 0.01, ambientT)
#
#         with open(arrayArchivos[k], 'w') as file2:
#             csvWriter = csv.writer(file2, delimiter=',')
#             csvWriter.writerows(array)
#
# with open("tempEnT10.csv", 'r') as file:
#     array = np.loadtxt(file, delimiter=",")
#     plt.imshow(array, cmap='gist_heat')
#     plt.show()




def analitica(x, T, Tm):

    return constant(Tm,T) * math.exp(-0.25*x) + Tm


def constant (Tm, T):
    return T-Tm

with open("temperaturas_horno.csv", 'r') as file3:
    array = np.loadtxt(file3, delimiter=",")

    for i in range(1, len(array[0]) - 1):
        for j in range(1, len(array[i]) - 1):
            ambientT = (array[i - 1][j - 1] + array[i - 1][j] + array[i - 1][j + 1] + array[i][j - 1] +
                        array[i + 1][
                            j - 1] + array[i][j + 1] + array[i + 1][j] + array[i + 1][j + 1]) / 8
            array[i][j] = analitica(1, array[i][j],ambientT)

    with open("tempEnT1Analitica.csv", 'w') as file2:
        csvWriter = csv.writer(file2, delimiter=',')
        csvWriter.writerows(array)

with open("tempEnT1.csv", 'r') as file4:
    array = np.loadtxt(file4, delimiter=",")
    with open("tempEnT1Analitica.csv", 'r') as file5:
        array2 = np.loadtxt(file5, delimiter=",")
        error = array-array2
        with open("ErrorT1.csv", 'w') as file6:
            csvWriter = csv.writer(file6, delimiter=',')
            csvWriter.writerows(error)