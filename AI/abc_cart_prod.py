import numpy as np


A = np.array([0.2, 0.4, 0.6, 0.8])
B = np.array([0.1, 0.3, 0.5, 0.7, 0.9])
C = np.array([0.2, 0.5, 0.8])


R = np.zeros((len(A), len(B)))
for i in range(len(A)):
    for j in range(len(B)):
        R[i, j] = np.minimum(A[i], B[j])


S = np.zeros((len(A), len(C)))
for i in range(len(A)):
    for j in range(len(C)):
        S[i, j] = np.minimum(A[i], C[j])
