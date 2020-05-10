import math
import matplotlib.pyplot as plt
from random import *
import time
import numpy as np

n = 10
Wmax = 900
N = 256

x = [0 for i in range(N)]
start1 = time.time()

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
end1 = time.time()
start2 = time.time()
F2 = np.fft.fft(x)
end2 = time.time()
print("Час виконання fft за допомогою програмної реалізації -", end1 - start1)
print("Час виконання fft за допомогою numpy -", (end2*pow(10,10) - start2*pow(10,10)), "*10^-10")
fig = plt.figure()
ax_1 = fig.add_subplot(2, 1, 1)
ax_2 = fig.add_subplot(2, 1, 2)
ax_1.plot(range(0, N), F)
ax_2.plot(range(0, N), F2)
ax_1.set(title='fft algorithm')
ax_2.set(title='fft numpy')
ax_1.grid()
ax_2.grid()
plt.show()
