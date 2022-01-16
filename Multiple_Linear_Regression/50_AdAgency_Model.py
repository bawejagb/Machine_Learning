# -*- coding: utf-8 -*-
"""
@author: Gaurav
"""
#Import Libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
#Import and Extract Data
dataset = pd.read_csv('50_AdAgency.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,-1].values
#Encode Label columns
lablelencoder = LabelEncoder()
X[:,3] = lablelencoder.fit_transform(X[:,3])
oneHE = ColumnTransformer([("City", OneHotEncoder(), [3])],
                          remainder = 'passthrough')
X = oneHE.fit_transform(X)
X = X[:,1:]
#Split Data in Train-Test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                    test_size=0.2,random_state=0)
#Build Model
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
Y_predict = regressor.predict(X_test)
#Error Finding
print(metrics.mean_absolute_error(Y_test, Y_predict))
print(metrics.mean_squared_error(Y_test, Y_predict))
print(np.sqrt(metrics.mean_squared_error(Y_test, Y_predict)))