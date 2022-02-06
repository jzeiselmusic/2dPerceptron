# create random test data that is linearly seperable
import random
import numpy as np
from awgn import *
import matplotlib.pyplot as plt

def make_test_data(a,b,variance,n):
# make two sets of n number of linearly separable data points 
# that are random about points a and b.
# this is done by essentially adding gaussian white noise to sets 
# of n number of points a and b.
	set1 = np.zeros([n,2])
	set2 = np.zeros([n,2])

	set1 = np.array(list(map(lambda x: x+a,set1)))
	set2 = np.array(list(map(lambda x: x+b,set2)))
	
	set1 = awgn(set1,1/variance)
	set2 = awgn(set2,1/variance)
	return set1,set2


def visualize_data(testdata1,testdata2,weights):
	y0 = (-weights[2] - weights[0]*0)/weights[1]
	y1 = (-weights[2] - weights[0]*1)/weights[1]
	testdata1x,testdata1y = zip(*testdata1)
	testdata2x,testdata2y = zip(*testdata2)
	fig1 = plt.figure(1)
	 
	plt.scatter(testdata1x,testdata1y)
	plt.scatter(testdata2x,testdata2y)
	plt.plot([y0,y1],scaley=False)
	plt.show()
	




