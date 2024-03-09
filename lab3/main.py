# аривнт 14
from scipy.optimize import minimize
import math
import numpy as np
import math


def gipps(x, g1, g2):
    R = 8.3144
    T = 298.15
    return R * T * (x * g1 + (1 - x) * g2)


def gamma_calc(x, y, P, P0):
    return (P * y) / (P0 * x)


def antyan(A, B, C):
    T = 298.15
    return math.exp(((A - B) / (T + C))) / 750.1


P1 = antyan(18.91, 3803.98, -41.68)
P2 = antyan(15.9, 2788.51, -52.36)
X1 = [0.1, 0.3, 0.5, 0.7, 0.9]
Y1 = [0.244, 0.324, 0.379, 0.406, 0.580]
P = [0.1550, 0.1630, 0.1617, 0.1545, 0.1250]
g = []
gamma1 = []
gamma2 = []

for i in range(len(P)):
    gamma1.append(gamma_calc(X1[i], Y1[i], P[i], P1))
    gamma2.append(gamma_calc(1 - X1[i], 1 - Y1[i], P[i], P2))
    g.append(gipps(X1[i], gamma1[i], gamma2[i]))


def func(x, x1=X1, g=g):
    R = 8.3144
    T = 298.15
    A1, A2 = x[0], x[1]
    sum = 0.0
    for i in range(0, 5):
        x2 = 1 - x1[i]
        print(x2 + A2 * x1[i])
        g_r = R * T * (-x1[i] * math.log(x1[i] + A1 * x2) - x2 * math.log(x2 + A2 * x1[i]))
        sum += abs(g[i] - g_r)
    return sum


res = minimize(func, x0=[0.5, 0.5], method='Nelder-Mead', tol=1e-6)
'''
print(P1)
print(P2)
print(*gamma1)
print(*gamma2)
print(*g)
'''
print(res.message)
print(res.x)
