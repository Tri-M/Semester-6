import numpy as np
import matplotlib.pyplot as plt

def trapezoid(x, a, b, c, d):
    if x <= a or x >= d:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return 1
    else:
        return (d - x) / (d - c)

a = 1
b = 3
c = 5
d = 7


x = np.linspace(0, 10, 100)
membership = np.array([trapezoid(xi, a, b, c, d) for xi in x])

plt.plot(x, membership)
plt.title('Trapezoidal Membership Function')
plt.xlabel('x')
plt.ylabel('Membership')
plt.show()
