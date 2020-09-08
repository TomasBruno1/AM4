from math import sqrt, factorial, pi
from decimal import Decimal

# TP1
# a)
print('a)')
print(pi)
# pi = 3.141592653589793
# b)
print('b)')
a = 1.0
b = 1 / sqrt(2)
t = 1 / 4
p = 1.0
while a - b > 0.000000000000001:
    x = (a + b) / 2
    y = sqrt(a * b)
    t = t - p * (a - x) ** 2
    a = x
    b = y
    p = 2 * p
    pi = ((a + b) ** 2) / (4 * t)
    print(pi)
# pi = 3.141592653589794
# c) Decimal using default precision 28.
print('c)')

a = Decimal(1)
b = Decimal(1 / sqrt(2))
t = Decimal(1 / 4)
p = Decimal(1)
while a - b > Decimal(0.000000000000000000000000001):
    x = Decimal((a + b) / 2)
    y = Decimal(sqrt(a * b))
    t = Decimal(t - p * pow((a - x), Decimal(2)))
    a = Decimal(x)
    b = Decimal(y)
    p = Decimal(2 * p)
    pi = Decimal(((a + b) ** 2) / (4 * t))
    print(Decimal(pi))
# pi = 3.141592653589793127002456641
# d)
print('d)')
pi = 0
for i in range(0, 100):
    pi += ((factorial(i) ** 2) * (2 ** (i + 1))) / factorial(2 * i + 1)
print(pi)
# pi = 3.1415926535897922
