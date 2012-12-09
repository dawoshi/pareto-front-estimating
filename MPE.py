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


def min_dist_to_dot(f1s, f2s, step):		# used in GeneralizationDistance and MaximumParetoFrontError indicators
	f1 = 0.0001
	min_residual = 100;
	while f1 <= 1:
		residual = dist(f1, f1s, f2s)
		if (residual < min_residual):
			min_dist = residual
			min_residual = residual
		f1 += step
	return min_dist

# Maximum Pareto Front Error indicator
maxv = 0
for f_vector in f_vectors:
	min_dist_for_dot1 = min_dist_to_dot(f_vector[0], f_vector[1], 0.00001)
	if (min_dist_for_dot1 > maxv):
		maxv = min_dist_for_dot1
result = maxv		
print "Problem: ", problem, " I_MPE = %f" % result