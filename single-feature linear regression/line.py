
'''
here i will code a very basic example of linear regression
additionally i will use basic ploting
below are the tasks
'''

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score

# read data and visualize it

data = pd.read_csv('Data.csv')

data.sort_values(by='Feature', inplace=True)

plt.plot(data['Feature'], data['Target'])
plt.title('dataset')
plt.show()

# split the data into testing and training

xTrain, xTest, yTrain, yTest = train_test_split(data['Feature'], data['Target'], test_size = .2)

xTrain = [ [x] for x in xTrain.to_numpy()]
xTest = [ [x] for x in xTest.to_numpy()]
yTrain = yTrain.to_numpy()
yTest = yTest.to_numpy()

# build the model and fit the training data to it

model = LinearRegression()

model.fit(xTrain, yTrain)

# visualize prediction vs real

yPred = model.predict(xTest)

plt.scatter(xTest, yTest, color='black', label='True points')
plt.scatter(xTest, yPred, color='red', label='Predicted points')
plt.plot(xTest, yPred, linewidth=1, color='blue', label='Reg. line')
plt.scatter(xTrain, yTrain, color='green', label='Training points')
plt.title('prediction vs real')
plt.legend()
plt.show()

# calculate accuracy using R2 score

print(r2_score(yTest, yPred))