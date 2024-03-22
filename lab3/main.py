import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt


def antyan(A, B, C):
    T = 298.15
    return np.exp(A - B / (C + T)) / 750.0668


def experimental_gibbs(exp_x1, exp_y1, pressure): # вычисляем энергию Гиббса по экспериментальным данным
    exp_x2 = np.array([1 - i for i in exp_x1])
    exp_y2 = np.array([1 - i for i in exp_y1])
    # расчет давления p0
    press_a = antyan(18.91, 3803.98, -41.68)
    press_b = antyan(15.9, 2788.51, -52.36)
    # функция для расчета гамм
    gamma_f = lambda x, y, pressure, press_0: (y * pressure) / (x * press_0)
    gamma_1_exp = [gamma_f(exp_x1[i], exp_y1[i], pressure[i], press_a) for i in range(len(exp_x1))]
    gamma_2_exp = [gamma_f(exp_x2[i], exp_y2[i], pressure[i], press_b) for i in range(len(exp_x1))]
    # экспериментальная формула для расчета избыточной энергии Гиббса
    g_experimental = np.array(
        [8.314 * t * (exp_x1[i] * np.log(gamma_1_exp[i]) + exp_x2[i] * np.log(gamma_2_exp[i])) for i in
         range(len(exp_x1))])
    return g_experimental

# модель Вильсона
def model_wilson(alpha12, alpha21, exp_x1, t, v1_l, v2_l):
    exp_x2 = np.array([1 - i for i in exp_x1])
    # вычисляем дельты по формуле
    delta12 = (v2_l / v1_l) * np.exp(-alpha12 / (8.314 * t))
    delta21 = (v1_l / v2_l) * np.exp(-alpha21 / (8.314 * t))
    # получение энергии Вилсона через дельты
    g_wilson = 8.314 * t * (-exp_x1 * np.log(abs(exp_x1 + delta12 * exp_x2)) - exp_x2 * np.log(abs(exp_x2 + delta21 * exp_x1)))
    return g_wilson


t = 298.15
x1 = np.array([0.1, 0.3, 0.5, 0.7, 0.9])
x2 = np.array([1 - i for i in x1])
y1 = np.array([0.244, 0.324, 0.379, 0.406, 0.580])
y2 = [1 - i for i in y1]
press = [0.1550, 0.1630, 0.1617, 0.1545, 0.1250]
g_exp = experimental_gibbs(x1, y1, press)

Tc = [516.2, 562.1]
Pc = [63.83 * 1e5, 48.94 * 1e5]
omega = [0.64, 0.21]
v1 = (((((8.314 * Tc[0]) / Pc[0]) * np.power(0.29056 - 0.08775 * omega[0], 1 + (1 - (t / Tc[0])) ** (2.0 / 7)))))
v2 = (((((8.314 * Tc[1]) / Pc[1]) * np.power(0.29056 - 0.08775 * omega[1], 1 + (1 - (t / Tc[1])) ** (2 / 7)))))

minimize_it = lambda alphas: np.sqrt(np.sum((np.array(g_exp) - model_wilson(alphas[0], alphas[1], x1, t, v1, v2)))** 2) 
x_init = np.array([1000, 1000])
answ = minimize(minimize_it, x_init, method='Nelder-Mead', tol=1e-3).x # минимизация функции

# равномерное распределение значений х в заданном диапазоне
x1_new = np.linspace(0, 1, 1000)
x2_new = np.array([1 - i for i in x1_new])
delta12 = (v2 / v1) * np.exp(-answ[0] / (8.314 * t))
delta21 = (v1 / v2) * np.exp(-answ[1] / (8.314 * t))
gamma1 = np.exp(-np.log(x1_new + delta12 * x2_new) + x2_new * (
            (delta12 / (x1_new + delta12 * x2_new)) - (delta21 / (x2_new + delta21 * x1_new))))
gamma2 = np.exp(-np.log(x2_new + delta21 * x1_new) - x1_new * (
            (delta12 / (x1_new + delta12 * x2_new)) - (delta21 / (x2_new + delta21 * x1_new))))
press_a = antyan(18.91, 3803.98, -41.68)
press_b = antyan(15.9, 2788.51, -52.36)
x1_new[0] += 1e-12
x2_new[-1] += 1e-12
y1_new = np.nan_to_num((gamma1 * x1_new * press_a) / (gamma2 * x2_new * press_b))
y1_new = y1_new / (y1_new + 1)
y2_new = np.array([1 - i for i in y1_new])
press_new = (gamma1 * x1_new * press_a) / y1_new

# построение графиков
plt.figure()
plt.title("Диаграмма x от y")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x1_new, y1_new)
plt.scatter(x1, y1, 5, "green")
plt.plot(x2_new, y2_new)
plt.scatter(x2, y2, 5, "red")
plt.figure()
plt.title("Диаграмма P от x и y")
plt.ylabel("P, bar")
plt.plot(x1_new, press_new)
plt.plot(y1_new, press_new)
plt.scatter(x1, press, 5, "green")
plt.scatter(y1, press, 5, "red")
plt.show()