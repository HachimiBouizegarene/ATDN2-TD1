import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

data = pd.read_csv('rendement_mais.csv')

#pretraitement des donnees 
encoder = LabelEncoder()
data["TYPE_SOL"] = encoder.fit_transform(data['TYPE_SOL'])

X = data.drop(columns=["RENDEMENT_T_HA"])
Y = data["RENDEMENT_T_HA"]
print(Y)

train_x, test_x, train_y, test_y = train_test_split(X,Y, test_size=0.2, random_state=10)

#regression lineaire 
model = LinearRegression()
model.fit(train_x, train_y)

pred_y_reg_lin = model.predict(test_x)
print(f"MAE Regression lineaire : {mean_absolute_error(y_pred=pred_y_reg_lin, y_true=test_y)}")
print(f"MSE, Regression lineaire : {mean_squared_error(y_pred=pred_y_reg_lin, y_true=test_y)}")
print(f"RMSE, Regression lineaire : {np.sqrt(mean_squared_error(y_pred=pred_y_reg_lin, y_true=test_y))}")

#regression polynomial

poly = PolynomialFeatures(degree=3)  #
train_x_poly = poly.fit_transform(train_x)
test_x_poly = poly.transform(test_x)

model_poly = LinearRegression()
model_poly.fit(train_x_poly, train_y)

pred_y_poly = model_poly.predict(test_x_poly)

print(f"MAE Regression polynomiale : {mean_absolute_error(y_pred=pred_y_poly, y_true=test_y)}")
print(f"MSE Regression polynomiale : {mean_squared_error(y_pred=pred_y_poly, y_true=test_y)}")
print(f"RMSE Regression polynomiale : {np.sqrt(mean_squared_error(y_pred=pred_y_poly, y_true=test_y))}")
