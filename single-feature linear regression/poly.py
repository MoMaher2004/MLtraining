
'''
in this file i will make a higher degree model
'''

import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score

data = pd.read_csv('Data.csv')

xTrain, xTest, yTrain, yTest = train_test_split(data['Feature'], data['Target'], test_size=.2)

xTrain = xTrain.values.reshape(-1, 1)
xTest = xTest.values.reshape(-1, 1)
yTrain = yTrain.to_numpy()
yTest = yTest.to_numpy()

poly = PolynomialFeatures(degree=4)
xTrainPoly = poly.fit_transform(xTrain)
xTestPoly = poly.fit_transform(xTest)

model = LinearRegression()
model.fit(xTrainPoly, yTrain)

xCurve = np.linspace(min(data['Feature']), max(data['Feature']), 100).reshape(-1, 1)
xCurvePoly = poly.transform(xCurve)
yCurve = model.predict(xCurvePoly)

yPred = model.predict(xTestPoly)

print(r2_score(yTest, yPred))

plt.scatter(xTest, yTest)
plt.plot(xCurve, yCurve)
plt.show()
