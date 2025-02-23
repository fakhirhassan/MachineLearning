import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


X = 6 * np.random.rand(100,1) -3
Y = 0.5 * X**2 + 1.5*X + 2 + np.random.randn(100,1)
# plt.scatter(X , Y , color = "green")
# plt.xlabel("X dataset")
# plt.ylabel("Y dataset")
from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size= 0.2 , random_state=42)
# from sklearn.linear_model import LinearRegression
# regression1 = LinearRegression()
# regression1.fit(X_train , Y_train)
# from sklearn.metrics import r2_score
# score = r2_score(Y_test , regression1.predict(X_test))
# print(score)
# plt.plot(X_train , regression1.predict(X_train))
# plt.scatter(X_train , Y_train)
# plt.xlabel("X dataset")
# plt.ylabel("Y dataset")

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2 , include_bias=True)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

from sklearn.linear_model import LinearRegression
regression1 = LinearRegression()
regression1.fit(X_train_poly , Y_train)
# from sklearn.metrics import r2_score
# score = r2_score(Y_test , regression1.predict(X_test_poly))
# print(score)

# plt.scatter(X_train , regression1.predict(X_train_poly) , color = "red")
# plt.scatter(X_train , Y_train , color = "green")
# plt.xlabel("X dataset")
# plt.ylabel("Y dataset")

#prediction of new dataset
X_new = np.linspace(-3,3,200).reshape(200,1)
X_new_poly = poly.transform(X_new)

Y_new = regression1.predict(X_new_poly)
# plt.plot(X_new , Y_new , 'r-' , linewidth = 2 , label = "prediction")
# plt.plot(X_train , Y_train , "b." , label = "training points")
# plt.plot(X_test , Y_test , "g." , label = "testing points")
# plt.xlabel("X dataset")
# plt.ylabel("Y dataset")
# plt.legend()
# plt.show()

from sklearn.pipeline import Pipeline

def poly_regression(degree):
    X_new = np.linspace(-3,3,200).reshape(200,1)
    poly_feature = PolynomialFeatures(degree = degree , include_bias= True)
    line_regression  = LinearRegression()
    poly_regression = Pipeline([
        ('poly', poly_feature),
        ('line', line_regression)
    ])
    poly_regression.fit(X_train , Y_train)
    y_pred_new = poly_regression.predict(X_new)
    plt.plot(X_new , y_pred_new , label = "degree" + str(degree) , linewidth = 2)
    plt.plot(X_train , Y_train , "b." , linewidth = 3)
    plt.plot(X_test , Y_test , "g." , linewidth = 3)
    plt.xlabel("X dataset")
    plt.ylabel("Y dataset")
    plt.legend(loc = "upper left")
    plt.axis([-4,4,0,10])
    plt.show()

poly_regression(3)