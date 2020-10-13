def Euler(f, x0, y0, b, n):
    h = (b - x0) / n
    for i in range(n):
        y1 = y0 + h * f(x0, y0)
        x0 = x0 + h
        y0 = y1
    return [x0, y0]


def funTo(x, y):
    return (y / x) ** 2 + y / x


# ---------------------------------------------------------------------------------------------------------------
# Ejercicio 1a
# ---------------------------------------------------------------------------------------------------------------

print('Ejercicio 1a: ' + str(Euler(funTo, 1, 1, 1.2, 2)))


def Taylor4(f1, f2, f3, f4, x0, y0, b, n):
    h = (b - x0) / n
    for i in range(n):
        f1Value = f1(x0, y0)
        f2Value = f2(x0, y0, f1Value)
        f3Value = f3(x0, y0, f1Value, f2Value)
        f4Value = f4(x0, y0, f1Value, f2Value, f3Value)
        y1 = y0 + h * f1Value + ((h ** 2) / 2) * f2Value + ((h ** 3) / 6) * f3Value + ((h ** 4) / 24) * f4Value
        x0 = x0 + h
        y0 = y1
    return [x0, y0]


# ---------------------------------------------------------------------------------------------------------------
# Ejercicio 5
# ---------------------------------------------------------------------------------------------------------------

def funTo1(x, y):
    return 1 + y ** 2 - x ** 3


def funTo2(x, y, y1):
    return 2 * y * y1 - 3 * x ** 2


def funTo3(x, y, y1, y2):
    return 2 * (y1 ** 2) + 2 * y * y2 - 6 * x


def funTo4(x, y, y1, y2, y3):
    return 6 * y1 * y2 + 2 * y * y3 - 6


print('Ejercicio 5: ' + str(Taylor4(funTo1, funTo2, funTo3, funTo4, 0, -1, 2, 200)))
