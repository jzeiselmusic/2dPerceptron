# the idea is to implement a simple perceptron algorithm to be able to
# distinguish between two sets of points that each have 2 characteristics. 

# the data must be linearly separable by a hyperplane

from make_test_data import *
import matplotlib.pyplot as plt
import numpy as np

#initialize the centers of the set of test points
CEN_POINT1 = np.array([-3,1])
CEN_POINT2 = np.array([3,3])

#initialize learning rate
N = .5

#initialize test sets 1 and 2
test_set11,test_set22 = make_test_data(CEN_POINT1,CEN_POINT2,50,100)

#initialize weight vectors w0 and w1 with 0 bias
w = np.array([[1],[-1],[0]])


# add 1 to the end of every data point to account of the learning bias

test_set1 = np.array(list(map(lambda n: np.append(n,1),test_set11)))
test_set2 = np.array(list(map(lambda n: np.append(n,1),test_set22)))


# this is the main algorithm for the training. Iterated 50 times

for j in range(50):
	for i in range(len(test_set1)):
		y_hat = float( np.dot(w.transpose(),test_set1[i]))
		if (y_hat > 0):
			w = np.subtract(w.transpose(),N*test_set1[i])
			w = w.transpose()

	for i in range(len(test_set2)):
		y_hat = float( np.dot(w.transpose(),test_set2[i]))
		if (y_hat < 0):
			w = np.add(w.transpose(),N*test_set2[i])
			w = w.transpose()	
		

print(w)

visualize_data(test_set11,test_set22,w)




