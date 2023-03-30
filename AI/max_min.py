import numpy as np


R = np.array([[0.2, 0.4, 0.6, 0.8, 0.9],
              [0.1, 0.3, 0.5, 0.7, 0.8],
              [0.1, 0.3, 0.5, 0.7, 0.8],
              [0.1, 0.3, 0.5, 0.7, 0.8]])
S = np.array([[0.2, 0.5, 0.8],
              [0.4, 0.6, 0.8],
              [0.2, 0.5, 0.8],
              [0.1, 0.3, 0.5]])


A = np.array([1, 2, 3, 4])
B = np.array([5, 6, 7, 8, 9])
C = np.array([10, 11, 12])
AxBxC = [(a, b, c) for a in A for b in B for c in C]


RoS = np.zeros((len(B), len(C)))
for i in range(len(B)):
    for j in range(len(C)):
        max_min = []
        for k in range(len(A)):
            for l in range(len(S)):
                if A[k] == R[k, i] and A[k] == S[k, j]:
                    max_min.append(min(R[k, i], S[k, j]))
        RoS[i, j] = max(max_min)
