import numpy as np
import matplotlib.pyplot as plt


def f1(r, t, t0, N0):
    Nt = []
    for i in t:
        Nt.append(N0 * np.exp(r * (i - t0)))
    return Nt


def f2(r, b, t, t0, N0):
    Nt = []
    k = r / b
    for i in t:
        Nt.append(k * N0 * np.exp(r * (i - t0)) / (k + N0 * (np.exp(r * (i - t0)) - 1)))
    return Nt


def f3(r, b, t, N0):
    Nt = []
    k = r / b
    Nt.append(N0)
    for i in range(1, len(t)):
        Nt.append(Nt[i - 1] + r * Nt[i - 1] * (1 - Nt[i - 1] / k))
    return Nt


t0 = 0
r = 0.05
k = 40
N0 = 5

N = 200
b = r / k
t = range(N)
#
# 1. Темп прироста не зависит от численности
plt.title('Не зависит от численности')
plt.ylabel('Nt')
plt.xlabel('t')
plt.plot(t, f1(r, t, t0, N0))
# plt.show()
#
# # 2. Уменьшается линейно с увеличение численности
plt.title('Уменьшается линейно с увеличением численности')
plt.ylabel('Nt')
plt.xlabel('t')
plt.plot(t, f2(r, b, t, t0, N0))
plt.show()
#
# # 3. Наличие некоторого ресурса
plt.title('При наличии ресурса')
plt.ylabel('Nt')
plt.xlabel('t')
plt.plot(t, f3(r, b, t, N0))
plt.show()
