import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder


def read_classification_data(file_path):
    df = pd.read_csv(file_path)
    df.c = np.uint8(df.c)
    x = np.array(np.matrix(df)[:,0:2])
    oh = OneHotEncoder()
    y = oh.fit_transform(np.array(np.matrix(df)[:,2])).toarray()
    return x, y


def read_regression_data(file_path, index_col=0):
    df = pd.read_csv(file_path, index_col=index_col) 
    n = len(df)
    x = np.reshape(np.array(df.x), (n, 1))
    y = np.reshape(np.array(df.y), (n, 1))
    return x, y