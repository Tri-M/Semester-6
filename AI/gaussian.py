import numpy as np
import matplotlib.pyplot as plt

def gaussmf(x, mean, sigma):
    return np.exp(-((x - mean)**2) / (2 * sigma**2))

x = np.arange(0, 11, 1)


center = 5
sigma = 2


mfx = gaussmf(x, center, sigma)


plt.plot(x, mfx, 'b', linewidth=1.5, label='Gaussian MF')
plt.title('Gaussian Membership Function')
plt.ylabel('Membership')
plt.xlabel('Input Variable')
plt.legend(loc='center right')
plt.show()
