# getting used to matplotlib


import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data
import numpy as np


fig = plt.figure()


ax = fig.add_subplot(1, 1, 1, projection='3d')


# plot a 3D wireframe like in the example mplot3d/wire3d_demo
X = [[]] #nuber of hidden layers
Y = [[]] #number of nodes per hidden layer
Z = [[]] # test accuracy



with open('layers0_5_nodes1_20.txt') as file:
    line = file.readline()
    numbers = line.split()
    x[0].append(round(float(numbers[0])), 4)


ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)

plt.show()



plt.show(block=True)
