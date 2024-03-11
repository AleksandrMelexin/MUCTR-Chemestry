import pandas as pd


def get_dataset():
  data = pd.read_csv("data.csv")
  
  X=data[["Temperature","Pressure"]].to_numpy()
  y=data[["Density"]].to_numpy()
  return X, y