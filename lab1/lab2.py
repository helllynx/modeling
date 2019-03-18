# Lab 2
import numpy as np
import matplotlib.pyplot as plt


def normalN1(N):
    return [np.sum(np.random.rand(1, 12)) - 6 for _ in range(N)]


def normalN2(N):
    res = []
    for _ in range(1, N // 2):
        s = 0
        while s == 0 or s > 1:
            x = np.random.rand(1) * 2 - 1
            y = np.random.rand(1) * 2 - 1
            s = x * x + y * y

        k = np.sqrt(-2 * np.log(s) / s)
        res.append(x * k)
        res.append(y * k)
    return res


def randN(N, x0=7, a=52, c=65, m=71):
    res = [np.mod(a * x0 + c, m)]
    for i in range(1,N):
        res.append(np.mod(a*res[i-1]+c, m))
    return res

def plot_hist(values, a, b):
    s = np.sum(values)
    values = [i/s for i in values]

    plt.hist(values)

    m = 1/(b-a)
    x = np.arange(a-1, b+1, 0.1)
    y = []

    for i in range(len(x)):
        if x[i] < a or x[i] > b:
            y.append(0)
        else:
            y.append(m)
    plt.plot(x,y)
    plt.show()

def plot_hist_normal(values):
    s = np.sum(values)
    values = [i/s for i in values]



    plt.hist(values)

    m = 0
    d = 1
    x = np.arange(-4*np.sqrt(d), 4*np.sqrt(d), 0.01)
    y = np.exp(-(x-m)**2/(2*d))/np.sqrt(d*2*np.pi)

    plt.plot(x, y)
    plt.show()

def findT(values):
    for i in range(2, len(values)):
        if values[i] == values[0]:
            T = i-1
            return T


# ========== EX1 ==========

# N = 10000
# X0 = 7
# a = 52
# c = 65
# m = 71
#
#
# values_1 = randN(N, X0, a, c, m)
#
# plot_hist(values_1, 0, m - 1)
#
# print(findT(values_1))
#
# values_2 = []
# for i in range(N):
#     if values_1[i] < m/2:
#         values_2.append(values_1[i])
#
# plot_hist(values_2, 0, (m - 1) / 2)
#
# print(findT(values_2))

# ========== EX2 ==========

N = 1000
m = 0
d = 1

values_1 = normalN1(N)
values_2 = normalN2(N)

plot_hist_normal(values_1)
plot_hist_normal(values_2)