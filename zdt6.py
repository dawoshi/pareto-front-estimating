# get F from X
from math import sqrt, sin, pi, exp

def get_F_from_X(x_vectors):
	f_vectors = []
	for x_vector in x_vectors:
		x1 = float(x_vector[0])
		x2 = float(x_vector[1])
		g = 1 + 9 * (x2 ** 0.25)
		f1 = 1 - exp(-4 * x1) * (sin(6 * pi * x1))**6
		f2 = 1 - (f1/g) ** 2
		f_vector = [f1, f2]
		f_vectors.append(f_vector)
	return f_vectors

def x2(x1):
	return 1 - x1 ** 2

def f2(x1):
	if (not (x1 >= 0.2807753191 and x1 <= 1)):
		return 9000
	x2 = 1 - x1 ** 2
	g = 1 + 9 * (x2 ** 0.25)
	f1 = 1 - exp(-4 * x1) * (sin(6 * pi * x1))**6
	f2 = 1 - (f1/g) ** 2
	return f2

def dist(f1, f1s, f2s):
	x_d = f1 - f1s
	y_d = f2(f1) - f2s
	return sqrt(x_d**2 + y_d**2)

# reads x from file dtlz_output_zdt2.txt
def read_from_file():
	x_vectors = []
	strings = open('dtlz_output_zdt6.txt').read().split('\n')
	for string in strings:
		val = string.split(' ')
		if len(val) == 1:
			break
		x_vector = [val[1], val[2]]
		x_vectors.append(x_vector)
	return x_vectors
