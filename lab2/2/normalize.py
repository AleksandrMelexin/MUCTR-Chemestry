import pandas as pd

def normalize_data(X):
  nX=X.copy();
  minsX=[]
  maxsX=[]

  for j in range(0,X.shape[1]):
    minsX.append(min(X[:,j]))
    maxsX.append(max(X[:,j]))

    for i in range(0,X.shape[0]):
      nX[i,j]=(X[i,j]-minsX[j])/(maxsX[j]-minsX[j])*0.9+0.1
  return nX,minsX,maxsX

def normalize_one_row(X, all_data_X):
  nX=X.copy();
  minsX=[]
  maxsX=[]

  for j in range(0,X.shape[1]):
    minsX.append(min(all_data_X[:,j]))
    maxsX.append(max(all_data_X[:,j]))
    
    for i in range(0,X.shape[0]):
      nX[i,j]=(X[i,j]-minsX[j])/(maxsX[j]-minsX[j])*0.9+0.1
  return nX,minsX,maxsX

def denormalize_data(X,minsX,maxsX):
  dX=X.copy();
  for j in range(0,X.shape[1]):
    for i in range(0,X.shape[0]):
      dX[i,j]=((X[i,j]-0.1)/0.9)*(maxsX[j]-minsX[j])+minsX[j]
  return dX

