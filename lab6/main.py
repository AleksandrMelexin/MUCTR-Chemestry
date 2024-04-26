import matplotlib.pyplot as plt
c_a = [0.017]
c_b = [0.014]
c_c = [0]
c_d = [0]

t = [0]
dt = 0.01
n = 400
k1 = 0.5
k2 = 0.2

for i in range(1, n):
    c_a.append(c_a[i-1] + t[i-1] * (-(k1*c_a[i-1]*c_b[i-1])))
    c_b.append(c_b[i-1] + t[i-1] *(-(k1*c_a[i-1]*c_b[i-1])))
    c_c.append(c_c[i-1] + t[i-1] *((k1*c_a[i-1]*c_b[i-1])-(k2*c_c[i-1])))
    c_d.append(c_d[i-1] + t[i-1] *(k2*c_c[i-1]))
    t.append(t[i-1] + dt)

plt.figure()
plt.plot(t, c_a, label='c(C5H10)', color='blue')
plt.plot(t, c_b, label='c(H2)', color='red')
plt.plot(t, c_c, label='c(C5H12)', color='green')
plt.plot(t, c_d, label='c(i-C5H12)', color='yellow')
plt.title('Зависимость концентрации веществ от времени')
plt.ylabel('Концентрация C')
plt.xlabel('Время t')
plt.legend()
plt.grid(True)
plt.show()
