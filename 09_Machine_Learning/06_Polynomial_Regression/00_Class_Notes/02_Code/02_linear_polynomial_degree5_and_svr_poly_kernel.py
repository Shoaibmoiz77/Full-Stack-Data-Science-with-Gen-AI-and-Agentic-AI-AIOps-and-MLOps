import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"D:\NIT\1. NIT_Batches\2. EVENING BATCH\N_Batch -- 4.00PM -- Feb 27\4. Oct\1st - poly\1.POLYNOMIAL REGRESSION\emp_sal.csv")

X = dataset.iloc[:, 1:2].values 
y = dataset.iloc[:, 2].values 

# liner regression model 

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)  

# linear regression visualizaton 
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Linear Regression graph')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# we will build polynomial model
from sklearn.preprocessing import PolynomialFeatures  
poly_reg = PolynomialFeatures(degree = 5) 
X_poly = poly_reg.fit_transform(X)  

poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)  

plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Level or Salary(Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show() 

lin_model_pred = lin_reg.predict([[6.5]]) 
lin_model_pred 

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
poly_model_pred

# SVR MODEL  

from sklearn.svm import SVR 
svr_reg = SVR(kernel='poly', degree = 4, gamma = 'auto') 
svr_reg.fit(X, y) 

svr_model_pred = svr_reg.predict([[6.5]]) 
svr_model_pred

#print(svr_reg.get_params())
 











