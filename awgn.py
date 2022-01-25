# take in a set of points and randomize them according to awgn
from numpy import sum,isrealobj,sqrt
from numpy.random import standard_normal


def awgn(s,SNR,L=1):
	gamma = 10**(SNR/10)
	if s.ndim == 1:
		P = L*sum(abs(s)**2)/len(s)
	else:
		P = L*sum(sum(abs(2)**2))/len(s)
	N0 = P/gamma 
	if isrealobj(s):
		n = sqrt(N0/2)*standard_normal(s.shape)
	else:
		n = sqrt(N0/2)*(standard_normal(s.shape) \
		 +1j*standard_normal(s.shape))
	r = s + 3*n
	return r


