# -*- coding: utf-8 -*-
"""
@author: Gaurav
"""
#Import Libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
#Import and Extract Data
dataset = pd.read_csv('kc_house_data.csv')
Y = dataset.pop("price")
X = dataset.iloc[:,2:18].values
#Split Data in Train-Test
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,
                                                    random_state=0)
#Build Model
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
Y_predict = regressor.predict(X_test)
#Error Finding
print("Mean Absolute Error: ",
      metrics.mean_absolute_error(Y_test, Y_predict))
print("Mean Squared Error: ",
      metrics.mean_squared_error(Y_test, Y_predict))
print("Root Mean Squared Error: ",
      np.sqrt(metrics.mean_squared_error(Y_test,Y_predict)))
