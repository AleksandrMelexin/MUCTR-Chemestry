from normalize import normalize_data, denormalize_data, normalize_one_row
from get_dataset import get_dataset
import keras
import numpy as np
import pandas as pd

model = keras.models.load_model('ouput.keras')

X, y = get_dataset()

prX = np.array([[430.0, 1.0]])

prX, minPrX, maxPrX = normalize_one_row(prX, X)
X, minsX, maxsX = normalize_data(X)

y, minsy, maxsy = normalize_data(y)

new_y=model.predict(X)

dnX = denormalize_data(X, minsX, maxsX)
dny = denormalize_data(y, minsy, maxsy)
new_y = denormalize_data(new_y, minsy, maxsy) # игрики которые предсказываются моделькой для всех данных

new_y_pr = model.predict(prX)
new_y_pr = denormalize_data(new_y_pr, minsy, maxsy)

print(new_y_pr) #вывод игриков которые нужно предсказать именно для нас из таблицы




