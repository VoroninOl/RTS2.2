import math
import matplotlib.pyplot as plt
from random import *
import time
import numpy as np

n = 10
Wmax = 900
N = 256

x = [0 for i in range(N)]

start = time.time()
for i in range(n):
    A = uniform(0, 1)
    F = uniform(0, 1)
    for j in range(0, N):
        x[j] += A * math.sin(Wmax / n * j * i + F)

w= np.zeros((int(N/2), int(N/2)))
for i in range(int(N/2)):
    for k in range(int(N/2)):
        w[i][k] = math.cos(4*math.pi/N * i * k ) + math.sin(4 * math.pi/N * i * k)

w_new = [0 for i in range(N)]
for i in range(N):
    w_new[i] = math.cos(2*math.pi/N * i ) + math.sin(2 * math.pi/N * i)

F_I = [0 for i in range(int(N/2))]
F_II = [0 for i in range(int(N/2))]
F = [0 for i in range(int(N))]

for p in range(int(N/2)):
    for k in range(int(N/2)):
        F_II[p] += x[2 * k] * w[p][k]
        F_I[p] += x[2 * k + 1] * w[p][k]

for p in range(N):
    if p < (N/2):
        F[p] += F_II[p] + w_new[p] * F_I[p]
    else:
        F[p] += F_II[p - int(N/2)] - w_new[p] * F_I[p - int(N/2)]

plt.plot(range(0, N), F)
plt.grid()
plt.show()
