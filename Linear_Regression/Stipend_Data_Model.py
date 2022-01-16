# -*- coding: utf-8 -*-
"""
@author: Gaurav
"""
#Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
#Import and Extract Data
dataset = pd.read_csv('Stipend_Data.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,1].values
#Split Data in Train-Test
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,
                                                    random_state=0)
#Build Model
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
#Predict test data
Y_predict = regressor.predict(X_test)
#Plot Data
plt.scatter(X_test, Y_test, color='Red')
plt.plot(X_test, Y_predict, color='Blue')
plt.title('Testing Data Analysis')
plt.xlabel('Years of Exp.')
plt.ylabel('Stipend')
#Error Finding
print("Mean Absolute Error: ",
      metrics.mean_absolute_error(Y_test, Y_predict))
print("Mean Squared Error: ",
      metrics.mean_squared_error(Y_test, Y_predict))
print("Root Mean Squared Error: ",
      np.sqrt(metrics.mean_squared_error(Y_test,Y_predict)))