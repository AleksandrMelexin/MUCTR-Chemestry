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


def get_dataset():
    data = pd.read_csv("data.csv")
    print(data)
    # data=data[data["GL"]==0]
    X = data[["Temperature", "Pressure"]].to_numpy()
    y = data[["Density"]].to_numpy()  # ,"GL"
    return X, y


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
    print("Inputs = ", n_inputs, " Outputs = ", n_outputs)
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
            print("Saving model...")
        print('fold: %d' % i)
        print('> MAE train: %.3f' % mae_train)
        print('> MAE test: %.3f' % mae_test)
        print('> MAPE train: %.3f' % mape_train)
        print('> MAPE test: %.3f' % mape_test)
        print('> MAE total: %.3f' % mae)
        print('> MAPE total: %.3f' % mape)
    plt.show()
    return mae, mape, model2


def normalize_data(X):
    nX = X.copy()
    minsX = []
    maxsX = []
    for j in range(0, X.shape[1]):
        minsX.append(min(X[:, j]))
        maxsX.append(max(X[:, j]))
        for i in range(0, X.shape[0]):
            nX[i, j] = (X[i, j] - minsX[j]) / (maxsX[j] - minsX[j]) * 0.9 + 0.1
    return nX, minsX, maxsX


def denormalize_data(X, minsX, maxsX):
    dX = X.copy()
    for j in range(0, X.shape[1]):
        for i in range(0, X.shape[0]):
            dX[i, j] = ((X[i, j] - 0.1) / 0.9) * (maxsX[j] - minsX[j]) + minsX[j]
    return dX


X, y = get_dataset()
X, minsX, maxsX = normalize_data(X)
y, minsy, maxsy = normalize_data(y)
mae, mape, model = evaluate_model(X, y)
model.save('ML.keras')
print('MAE: %.3f MAPE: %.3f' % (mae, mape))
