
'''
in this code i will just preprocess data set of titanic dataset
'''

import numpy as np
import pandas as pd
import matplotlib as plt

data = pd.read_csv('train.csv')

print(data.info())
print(data.head())
print(data.shape)

data.drop(['PassengerId', 'Name', 'Ticket', 'Fare', 'Embarked'], axis=1, inplace=True)

plt.plot(data['Fare'], data['Survived'])
plt.show()

print(data.head())