'''
in this file, i will learn to visualize data using matplotlib and seaborn
'''

import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt

'''
x = np.random.random(50) * 100
y = np.random.random(50) * 100

plt.scatter(x, y, c='red', marker='3', s=200)
plt.show()
'''

'''
x = range(20)
y = np.random.random(20)

plt.plot(x, y, c='#643', lw=3, linestyle='--')
plt.show()
'''

'''
x = ['dogs', 'hamisters', 'cats', 'parrots']
y = [20, 14, 30, 2]

plt.bar(x, y, color='#328532', align='center', width=0.5, edgecolor='cyan', lw=4)
plt.show()
'''

'''
x = np.random.normal(20, 15, 1000)

plt.hist(x, bins=20, cumulative=True)
plt.show()
'''

'''
x = np.random.normal(33, 20, 1000)

plt.hist(x, bins=[x.min(), 15, 33, x.max()])
plt.show()
'''

'''
x = ['dogs', 'hamisters', 'cats', 'parrots']
y = [20, 14, 30, 2]
explods = [.05, .05, .05, .15]

plt.pie(y, labels=x, explode=explods, autopct='%.2f%%', pctdistance=1.3, startangle=70)
plt.show()
'''


# next is boxplot