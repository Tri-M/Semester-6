import numpy as np
import matplotlib.pyplot as plt

def triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

a = 0
b = 5
c = 10


x = np.linspace(-2, 12, 1000)

y = [triangular(i, a, b, c) for i in x]


plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Membership value')
plt.title('Triangular membership function')
plt.show()
