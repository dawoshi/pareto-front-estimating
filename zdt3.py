# get F from X
from math import sqrt, sin, pi

def get_F_from_X(x_vectors):
	f_vectors = []
	for x_vector in x_vectors:
		x1 = float(x_vector[0])
		x2 = float(x_vector[1])
		if x1 == 0:
			continue;
		if validateX1(x1) == 9000:
			print "outer x1"
			continue
		g = 1 + 9 * x2
		f1 = x1		
		f2 = g * (1 - sqrt(x1/g) - x1/(g * sin(10 * pi * x1)))
		f_vector = [f1, f2]
		f_vectors.append(f_vector)
	return f_vectors

def x2(x1):
	return 1 - sqrt(x1) - x1 * sin(10 * pi * x1)

def validateX1(x1):
	if (x1 >= 0 and x1 <= 0.0830015349 or
		x1 > 0.2222287280 and x1 <= 0.2577623634 or 			#0.1822287280			
		x1 > 0.4093136748 and x1 <= 0.4538821041 or
		x1 > 0.6183967944 and x1 <= 0.6525117038 or
		x1 > 0.8233317983 and x1 <= 0.8518328654):
		return x1
	else:
		return 9000

def f2(f1):
	x1 = f1
	if (not (x1 >= 0 and x1 <= 0.0830015349 or
		x1 > 0.2222287280 and x1 <= 0.2577623634 or   			#0.1822287280
		x1 > 0.4093136748 and x1 <= 0.4538821041 or
		x1 > 0.6183967944 and x1 <= 0.6525117038 or
		x1 > 0.8233317983 and x1 <= 0.8518328654)):
		return 9000

	x2 = 1 - sqrt(x1) - x1 * sin(10 * pi * x1)
	g = 1 + 9 * x2
	if (g <= 0):			# to avoid exeption
		#print "avoiding exception, f1-x1: ", f1, " g: ", g
		g = 0.000000001		
	f2 = g * (1 - sqrt(x1/g) - x1/(g * sin(10 * pi * x1)))
	return f2

def dist(f1, f1s, f2s):
	x_d = f1 - f1s
	y_d = f2(f1) - f2s
	return sqrt(x_d**2 + y_d**2)

