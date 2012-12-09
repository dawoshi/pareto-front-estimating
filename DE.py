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


# Dimensions Extent indicator
max0 = 0
max1 = 0
for Fj_vector in f_vectors:
	for Fk_vector in f_vectors:
		ort_dist = abs(Fk_vector[0] - Fj_vector[0])			# difference between two coordinats (i.e x1 - x2)
		if (ort_dist > max0):
			max0 = 	ort_dist
		ort_dist = abs(Fk_vector[1] - Fj_vector[1])			# difference between two coordinats (i.e y1 - y2)
		if (ort_dist > max1):
			max1 = 	ort_dist
result = max0 + max1	
print "Problem: ", problem, " I_DE = %f" % result