import numpy as np


set_a = np.array([0.1, 0.3, 0.5, 0.7, 0.9])
set_b = np.array([0.2, 0.4, 0.6, 0.8])


union = np.union1d(set_a, set_b)
print("Union of set A and set B:", union)


intersection = np.intersect1d(set_a, set_b)
print("Intersection of set A and set B:", intersection)


difference = np.setdiff1d(set_a, set_b)
print("Difference of set A and set B:", difference)


complement = 1 - set_a
print("Complement of set A:", complement)
