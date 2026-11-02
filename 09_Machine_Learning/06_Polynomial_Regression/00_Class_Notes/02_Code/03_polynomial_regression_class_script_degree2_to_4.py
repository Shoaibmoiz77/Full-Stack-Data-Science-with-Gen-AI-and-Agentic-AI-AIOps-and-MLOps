# We will learn slightly advanced ML model called as - POLYNOMIAL REGRESSION MODEL
#We did before was simple linear regression and multiple linear regression modeL
#so far we build a linear regressor as linear & multilinear regressor

#from now we are going to build regressor but that are not linear any more 
#polynomial regression is not linear regressor, then we build svr, then we build the decission tree regressor & random forset regression model which are not linear at all
#if i use polynomial term in simple linear regression then that is called as polynomial regressor
#next svr,dt,random forest based will be based on more complex theory

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#************************************************************************************************************************

# Importing the dataset
dataset = pd.read_csv(r"C:\Users\kdata\Desktop\KODI WORK\1. NARESH\2. EVENING BATCH\N_Batch -- 7.30PM\3. MAY\16th,17th\1.POLYNOMIAL REGRESSION\emp_sal.csv")
#we are HR team working for big company & we are about hire a new employee, after interveiw we do see that new employee is good and fit for the job
#we have to give an offer for the potential new employee & now its time to negotiate whats going to be the future salary of this new employee in the company
#so begining of the negotiation new employee is telling that he has experience and earned 161K annual salary in previous company, so this employee is asking for more then 161K
#however someone in HR team trying to call to the previous employee to check the previous employee information, the information about the 161kannual salary of future potential of new employee
#but unfortunately all the information HR person manage to get from previous employer is the dataset which we are going to see
#dataset is simple table of salary of the 10 different position in the previous company
#so the HR member of team runs the simple analysis on excel adn observe that there is non -linear relationshipb/w the position level & salary
#However the HR person get another very relavant info - new employee has Regional Manager for 2yrs now usually average it takes 4 yrs to jump from regional manager to partner
#so this employee is halfway b/w leve 6 & level 7, so we can say that level is 6.5
#so now the HR guy is very much excited he can telling the team to build a regression model to predict the new employee salary
#new employee is telling his annual sal is 161K & lets predict new employee is truth or bluff by using polynomial regression

#now lets see what index we need to check, so when we look at the table hear we want to predict the salary  based on different level and then we predict salary of 6.5 level 
#we dont need the categorical column becuase that column is equivalent to level only
#we encoded the positio level associated with each position level 
#so we need 2 columns to build the ML model & machine will learn the corelation b/w position and salary to predict if the employee is bluffing about salary
#so we dont need the categorical data & we consider only 2 columns
#so our X-matrix is only one column is level and y-matrix is salary
#this dataset contains 3 columns - position , level & salary
#if you take indexing from column wise then postion would be 0 index - position,1st index is lvele & 2nd index one is salary indexing


X = dataset.iloc[:, 1:2].values
#now we will create X matrix of feature and we will spcify the index 1 - LEVEL & however there is something
#then i have to mention 2 because in python upper bound of range is excluded
y = dataset.iloc[:, 2].values
#Dependent variable we will specify the index 2

#our main goal is to predict if this employee is bluffing  by building machine learning model that is polynomial model

#************************************************************************************************************************

# Splitting the dataset into the Training set and Test set
#but in this case we dont need to do the training & tesinng , lets see the reason
#if you look at the dataset we have only 10 observation & when we have small no. of observation then it doesnot make a sence split the data into trainin & testing 
#so we dont have enough information to train the model
#onter point is we want to make very accurate prediction becuasewe are trying to predict the salary of new employee, if we not build the accurate the prediction 
#in order to make accurate prediction we need to have maximum observation so that model will get perfectly get the corelation b/w the dataset 
#only for this time we will allow ourself to take whole dataset to train the ML model 

#************************************************************************************************************************

#feature scaling is also not required on this case becuase we have to add polynomial function right
# also we will use same linear regression library for this also
# so no need to feature scaling and no need to training and testing also

#************************************************************************************************************************
#In this section we build the linear regression model & also we gonna build the polynomial regression model to fit the dataset
#why we creating the 2 models becusae if we go backe to the equation & also compare the both results

# Fitting Linear Regression to the dataset

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
#To compare both linear model created lin_reg & for polynomial we will mention as lin_reg2
#so create a object of lin_reg and called the class LinearRegression
lin_reg.fit(X, y)
#fit the lin_reg object to X & y. now our simple linear regression is ready 

#*************************************************************************************************************************

#Now lets build the polynomial regression model
#to create this model we will import a PolynomialFeature

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
#preprocessing is library we used for feature scaling in data preprocessing
#from preprocessing library we called the class as PolynomialFeatures class
poly_reg = PolynomialFeatures() # we mentoine 2 degree 
#create an object called poly_reg & we will assigned the degree 
#what exactly poly_reg will do the transform the feature of X & y to new matrix called X_poly & y_poly
#polyfeature will transfer from X1 to X1square, X2 to X2 square 
#it will transferm untill you mention the power
#in one independent variable X  till 2,3,4 or 5 columns will be crreated based on the power
#to the first step i will mention the default degree is 2 
X_poly = poly_reg.fit_transform(X)
#finaly we will create new X_poy object or X_poly matrix to hold newly created columns by polyfeatures
#poly_reg is the object to fit and transform from X to X_poly matrix
#we are transform from X independent to poly by adding degree 2

#Lets see the variable explore what happend hear first upol click on X you get the orighinal level & in X_poly matrix we have 3 columns
#in the X_poly where is our X which is our second column & if you see 2nd then you get the degree of square
#remember in multiple linear regression we have to add manualy of column 1 called constant 
#when you called Poly_reg_transform automatically or bydefault 1 will be created

poly_reg.fit(X_poly, y)
#now we have to fit the poly_reg fit instad of x we have to fit with X_poly, y
#in linear we have done lin_reg.fit (x,y)

#*************************************************************************************************************************

lin_reg_2 = LinearRegression()
#we crate an 2nd object for same LinearRegression
lin_reg_2.fit(X_poly, y)
#now we need to fit lineare regression object to X_poly & y
#now our polynomial model is created & we will ready to review the truth or bluff part
#now we build 2 regressor - linear regressor and polynomial regressor

#*************************************************************************************************************************

#now we gonna visualize all the result & we will start all the observation point on x-asix and we will 10 related salary on y-axis
#first we will draw the visualtin of linear regression model and then we will build the visualize of polynomial regression model
#we will compare the true value of true observaiton made by the model

# Visualising the Linear Regression results

#lets starts the plotting by true observation 
plt.scatter(X, y, color = 'red')
#we are going to plot for actual value of X & y
plt.plot(X, lin_reg.predict(X), color = 'blue')
#now plot for the prediction line where x coordinate are predictin points & for y-cordinates predicted value which is lin_reg.predict (x)
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#now we visualize the linar regression graph,lets check the difference b/w actual point & predicted point
#prediction of linear regression model is straight line, red - real observation point & blue is predicted observation point
#this is not a right predicton, as i said linear model if you applied on non-linear dataset then you wont get the accurate predictino
#only one point close to the prediction & one point is very far from the prediction line
#lets take one example is if you take top point actual sal is 100million but predicte is 60000 which had some error rate
#thats why we need the batter model & this is linear model prediction 
#next step is we will build the non-linear model

#************************************************************************************************************************

# Visualising the Polynomial Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
#in y-coordinate we have to replace with lin_reg2 which we create for poly regression model
#X_poly is not defined cuz we already defined in above plot, so insted of X_poly we will define complete fit_trasnform code 
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#After execute first thing we dont have straing line hear & we got curve hear & we can say that polynomial regression is not a linear regression model
#you can easily say that distinguish b/w linear model & non-linear model
#linear model is straigt line but non-linear is not a straight line
# lets take the highst point which is ceo whose actual sal is 100k but found predicted as 90k, but better then last time 
#still we can say bit improved not accurate model which model thats the reason we have to increase the degree from 2 to 3
#if you check what is the predicted sal of 6.5 yr of exper whose sal was 161k but as per model predict that almost equal so we can say that employee is honest
# blue curve is much better complare to last then the linear regression model
#now we can do much better by adding degree from 2 to 3

#only you have to do is adding instead of 3 for better improvement 
#our loop is approching is much better , and you can say that poly model is quite improving 
#now if you observe that ceo actual salar is almost try to equal to predicted & based on this situation you can say that can we imporve the model bit more 
#next step you have to do is adding one more degree to 4  & now you get that blue curve is almost fit to the actual point and you can that employee is genuine 

# Final step to do and that is weeather the new employee is truth or bluff by predicting by polynomial 
#new empoyy previous sal is 161k , we will compare this value to our prediction & we will see if the employee was bluffing 

#*************************************************************************************************************************

# Predicting a new result with Linear Regression
lin_reg.predict([[6.5]])
#means that show me the predicted salary coresponding to 6.5 & lets see what our linear regression model is predict 
#if you go back to linear plot 6.5 level we got as 331k somewher around & this is linear regression result and this is not the definitely not the best one for prediction

# now we will see the salary of 6.5 level what is the prediction salary part

# Predicting a new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
#This code show me that predicted salary of 6.5 level using poly reg model
#That means employee is True and we solved this by using polyregression model













