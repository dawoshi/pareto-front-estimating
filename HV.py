# -*- coding: utf8 -*-

from os import sys
from math import sqrt

file_with_archive = sys.argv[1]
problem = sys.argv[2]

if (problem == 'zdt1'):									# В зависимости от тестовой задачи загружаем функцию определения расстояния точки до фронта (dist), 
	from zdt1 import dist, get_F_from_X, f2, x2			# функцию трансформирования входных данных в виде множества Парето в данные, представляющие фронт Парето (get_F_from_X),
if (problem == 'zdt2'):									# функцию точного фронта Парето (f2), функцию точного множества Парето (x2) 
	from zdt2 import dist, get_F_from_X, f2, x2
if (problem == 'zdt3'):
	from zdt3 import dist, get_F_from_X, f2, x2
if (problem == 'zdt4'):
	from zdt4 import dist, get_F_from_X, f2, x2
if (problem == 'zdt6'):
	from zdt6 import dist, get_F_from_X, f2, x2

from read_from_file	import *								# Следующая функция read_from_file определена в файле read_from_file.py

x_vectors = read_from_file(file_with_archive)				# Вектора X, представляющие собой множество Парето
f_vectors = get_F_from_X(x_vectors)							# Вектора F, представляющие собой множество Парето
archive_potency = len(f_vectors)


# Hypercube V
min_x = 9000
min_y = 9000
max_x = 0
max_y = 0
for f_vector in f_vectors:
	current_x = f_vector[0]
	current_y = f_vector[1]
	if (current_x > max_x):
		max_x = current_x
	if (current_y > max_y):
		max_y = current_y
	if (current_x < min_x):
		min_x = current_x
	if (current_y < min_y):
		min_y = current_y
def min_val(val1, val2):
	if val1 < val2:
		return val1
	else:
		return val2
def max_val(val1, val2):
	if val1 > val2:
		return val1
	else:
		return val2

min_coordinate = min_val(min_x, min_y)
max_coordinate = max_val(max_x, max_y)
result = (max_coordinate - min_coordinate)**2
print "Problem: ", problem, " I_HV = %f" % result
