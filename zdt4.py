# get F from X
from math import sqrt, cos, pi

def get_F_from_X(x_vectors):
	f_vectors = []
	for x_vector in x_vectors:
		x1 = float(x_vector[0])
		x2 = float(x_vector[1])		
		f1 = x1
		g = 1 + 10 + (x2 ** 2 - 10 * cos(4 * pi * x2))
		f2 = g * (1 - (x1/g) ** 2)
		f_vector = [f1, f2]
		f_vectors.append(f_vector)
	return f_vectors

def x2(x1):
	return 1 - sqrt(x1)

def f2(f1):
	x1 = f1
	x2 = 1 - sqrt(x1)
	g = 1 + 10 + (x2 ** 2 - 10 * cos(4 * pi * x2))
	f2 = g * (1 - (x1/g)**2)
	return f2

def dist(f1, f1s, f2s):
	x_d = f1 - f1s
	y_d = f2(f1) - f2s
	return sqrt(x_d**2 + y_d**2)
