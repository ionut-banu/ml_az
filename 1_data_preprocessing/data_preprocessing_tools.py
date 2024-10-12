# -*- coding: utf-8 -*-
"""data_preprocessing_tools.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ef-D5IxLJ61LMxFj-RzfmsL62VZZxz92

# Data Preprocessing Tools

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(X)

print(y)

"""## Taking care of missing data"""

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

print(X)

"""## Encoding categorical data

### Encoding the Independent Variable
"""

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

print(X)

"""### Encoding the Dependent Variable"""

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

print(y)

"""## Splitting the dataset into the Training set and Test set

## Feature Scaling
"""