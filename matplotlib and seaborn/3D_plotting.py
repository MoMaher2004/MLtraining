'''
3D plotting
'''

import numpy as np
import matplotlib.pyplot as plt

td = plt.axes(projection='3d')


'''
x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

td.scatter(x, y, z)

td.set_title('3d plotting')
td.set_xlabel('x')
td.set_ylabel('y')
td.set_zlabel('z')

plt.show()
'''

'''
x = np.arange(-5, 5, .1)
y = np.arange(-5, 5, .1)

X, Y = np.meshgrid(x, y)

Z = np.sin(X) + np.cos(Y)

td.plot_surface(X, Y, Z, cmap='cool')

td.view_init(elev=90)

plt.show()
'''
