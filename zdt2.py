# get F from X
from math import sqrt

def get_F_from_X(x_vectors):
	f_vectors = []
	for x_vector in x_vectors:
		x1 = float(x_vector[0])
		x2 = float(x_vector[1])
		g = 1 + 9 * x2
		f1 = x1
		f2 = g * (1 - (x1/g)**2)
		f_vector = [f1, f2]
		f_vectors.append(f_vector)
	return f_vectors

def x2(x1):
	return 1 - x1**2

def f2(f1):
	return (10 - 9 * (f1**2)) * (1 - (f1/(10 - 9 * (f1**2)))**2)

def dist(f1, f1s, f2s):
	x_d = f1 - f1s
	y_d = f2(f1) - f2s
	return sqrt(x_d**2 + y_d**2)

# reads x from file dtlz_output_zdt2.txt
def read_from_file():
	x_vectors = []
	strings = open('dtlz_output_zdt2-maxgen200.txt').read().split('\n')
	for string in strings:
		val = string.split(' ')
		if len(val) == 1:
			break
		x_vector = [val[1], val[2]]
		x_vectors.append(x_vector)
	return x_vectors
