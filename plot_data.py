# getting used to matplotlib


import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data
import numpy as np



reading_from = "cleaned_data.txt"





fig = plt.figure()



plot1 = fig.add_subplot(1, 1, 1, projection='3d')



# plot a 3D wireframe like in the example mplot3d/wire3d_demo
X = [[]] #nuber of hidden layers
Y = [[]] #number of nodes per hidden layer
Z = [[]] # val accuracy
Z1 = [[]] # val loss
Z2 = [[]] # training accuracy


with open(reading_from) as file:
    header = file.readline()
    while True:
        line = file.readline()
        if line == "":
            break

        numbers = line.split()
        X[0].append(float(numbers[0]))
        Y[0].append(float(numbers[1]))
        Z[0].append(float(numbers[4]))
        Z1[0].append(float(numbers[5]))
        Z2[0].append(float(numbers[2]))

X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)
Z1 = np.array(Z1)
Z2 = np.array(Z2)

#plot1
plot1.scatter(X, Y, Z)
#plot1.scatter(X, Y, Z2)
plot1.set_xlabel('Hidden Layers')
plot1.set_ylabel('Nodes per Hidden Layer')
plot1.set_zlabel('Accuracy') # if Z
#plot1.set_zlabel('Test Loss') # if Z1
plot1.set_title("Performance")






plt.show()



plt.show(block=True)
