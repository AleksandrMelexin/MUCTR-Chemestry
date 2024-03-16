import keras
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from normalize import normalize_data, denormalize_data, normalize_one_row
from get_dataset import get_dataset

model = keras.models.load_model('ML.keras')
X, y = get_dataset()
prX = np.array([[293.0, 4.0]])

# нормализуем входные данные
prX, minPrX, maxPrX = normalize_one_row(prX, X)
X, minsX, maxsX = normalize_data(X)
y, minsy, maxsy = normalize_data(y)

new_y = model.predict(X)
new_y_pr = model.predict(prX)

# денормализуем посчитанные данные
dnX = denormalize_data(X, minsX, maxsX)
prDnX = denormalize_data(prX, minsX, maxsX)
dny = denormalize_data(y, minsy, maxsy)
new_y = denormalize_data(new_y, minsy, maxsy)
new_y_pr = denormalize_data(new_y_pr, minsy, maxsy)

fig, ax = plt.subplots(1, 2)
temps = []
ydata = [[], []]
ax[0].set_title("P = const = 4.14 бар")
for i in range(119, 136):
    temps.append([dnX[i][0]])
    ydata[0].append(dny[i][0])
    ydata[1].append(new_y[i][0])
ax[0].plot(temps, ydata[0], "ro")  # помещаем на график экспериментальные данные при p = 4.14 бар
ax[0].plot(temps, ydata[1])  # помещаем на график предсказанные нейросетью данные при p = 4.14 бар

ax[0].plot(prDnX[0][0], new_y_pr[0], "bo")  # ставим на график точку предсказанную неёросетью

ax[1].set_title("P = const = 2.72 бар")
temps = []
ydata = [[], []]
for i in range(85, 102):
    temps.append([dnX[i][0]])
    ydata[0].append(dny[i][0])
    ydata[1].append(new_y[i][0])
ax[1].plot(temps, ydata[0], "ro")  # помещаем на график экспериментальные данные при p = 2.72 бар
ax[1].plot(temps, ydata[1])  # помещаем на график предсказанные нейросетью данные при p = 2.72 бар
plt.ylabel("p, кг/м^3")
plt.xlabel("T, K")
plt.show()
