# -*- coding: utf-8 -*-
"""
@author: Gaurav
"""
#Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn import metrics
#Import and Extract Data
dataset = pd.read_csv("rank_salary.csv")
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,-1].values
#Finding appropriate ploynomial degree with minimum error
rmse = 0
pe = 0
d = 2
while (rmse <= pe):
    pe = rmse
    polyReg = PolynomialFeatures(degree= d)
    XPoly = polyReg.fit_transform(X)
    poly_regressor = LinearRegression()
    poly_regressor.fit(XPoly, Y)
    YPredict = poly_regressor.predict(XPoly)
    rmse = np.sqrt(metrics.mean_squared_error(Y,YPredict))
    if d < 3:
        pe = rmse
    d += 1
#Plot Data
plt.scatter(X, Y, color='red')
plt.plot(X, YPredict, color='blue')
plt.title("Polynomial Regression")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()
#Display Error and degree of ploynomial 
print("Degree:", d-1)
print("MAE: ",metrics.mean_absolute_error(Y,YPredict))
print("MSE: ",metrics.mean_squared_error(Y,YPredict))
print("RMSE: ",np.sqrt(metrics.mean_squared_error(Y,YPredict)))
salP = poly_regressor.predict(polyReg.fit_transform([[7.5]]))
print("Salary for rank 7.5 is Rs",salP[0])  