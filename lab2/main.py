from math import log
from math import exp
from numpy import mean
import numpy as np
import pandas as pd
from sklearn.model_selection import RepeatedKFold
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
from matplotlib import pyplot as plt
from normalize import normalize_data, denormalize_data
from get_dataset import get_dataset


def get_model(n_inputs, n_outputs):
    model = Sequential()
    model.add(Dense(2, input_dim=n_inputs, activation='sigmoid'))
    model.add(Dense(n_outputs, activation='linear'))
    opt1 = optimizers.Adam(learning_rate=0.005)
    model.compile(loss='mae', metrics=['mape'], optimizer=opt1)
    model.summary()
    return model


def evaluate_model(X, y):
    n_inputs, n_outputs = X.shape[1], y.shape[1]
    cv = RepeatedKFold(n_splits=5, n_repeats=1, random_state=22527)
    i = 0
    MAPE = 300
    for train_ix, test_ix in cv.split(X):
        i = i + 1
        X_train, X_test = X[train_ix], X[test_ix]
        y_train, y_test = y[train_ix], y[test_ix]
        model = get_model(n_inputs, n_outputs)
        history = model.fit(X_train, y_train, verbose=0, epochs=1000)
        plt.plot(history.history['loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'val'], loc='upper left')
        [mae_train, mape_train] = model.evaluate(X_train, y_train)
        [mae_test, mape_test] = model.evaluate(X_test, y_test)
        [mae, mape] = model.evaluate(X, y)
        if (mape < MAPE):
            MAPE = mape
            model2 = model
    plt.show()
    return mae, mape, model2


X, y = get_dataset()
X, minsX, maxsX = normalize_data(X)
y, minsy, maxsy = normalize_data(y)
mae, mape, model = evaluate_model(X, y)
model.save('ML.keras')
