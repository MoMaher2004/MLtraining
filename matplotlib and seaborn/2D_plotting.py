'''
in this file, i will learn to visualize data using matplotlib and seaborn
'''

import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')

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

'''
x = np.random.normal(170, 10, 1000)

plt.boxplot(x)
plt.show()
'''

'''
age = range(0, 75, 5)
malesHeight = np.concatenate([
    np.linspace(0, 20, 5) * 8, 
    np.linspace(20, 50, 5) * 0.4 + 160,
    np.linspace(0, 20, 5) * -0.2 + 180
])
femalesHeight = np.concatenate([
    np.linspace(0, 20, 5) * 7, 
    np.linspace(20, 50, 5) * .2 + 150,
    np.linspace(0, 20, 5) * -.2 + 160
])

plt.plot(age, malesHeight, c='blue', label='Males')
plt.plot(age, femalesHeight, c='pink', label='Females')

plt.title('The mean hight of males VS females in different ages', fontsize=13, fontname='purisa')
plt.xlabel('Age')
plt.ylabel('Hight')

maxMale = malesHeight.max()
maxFemale = femalesHeight.max()
maxHeight = int(max(maxFemale, maxMale))

plt.yticks(range(0, maxHeight + 20, 20), [f"{x} cm" for x in range(0, maxHeight + 20, 20)])

plt.legend(loc='lower center')
plt.show()
'''

'''
x = ['dogs', 'hamisters', 'cats', 'parrots']
y = [20, 14, 30, 2]

plt.pie(y)
plt.legend(labels=x, loc='upper right')
plt.show()
'''

'''
x = np.arange(100)

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(x, np.tan(x))
axs[0, 0].set_title('tan')
axs[0, 0].set_xlabel('x')

axs[0, 1].plot(x, np.tanh(x))
axs[0, 1].set_title('tanh')
axs[0, 1].set_xlabel('x')

axs[1, 0].plot(x, np.cosh(x))
axs[1, 0].set_title('cosh')
axs[1, 0].set_xlabel('x')

axs[1, 1].plot(x, np.sinh(x))
axs[1, 1].set_title('sinh')
axs[1, 1].set_xlabel('x')

fig.suptitle('some functions')
plt.tight_layout()


plt.savefig('plot.svg', format='svg')
# plt.savefig('plot.png', dpi=100, transparent=False)
plt.show()
'''