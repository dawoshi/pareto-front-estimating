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

def manhattan_dist(F1_vector, F2_vector):					# Вычисление мэннхэттеновского расстояния между двумя векторами
		return abs(F1_vector[0] - F2_vector[0]) + abs(F1_vector[1] - F2_vector[1])

# Maximum spread indicator
summ = 0;
for Fj_vector in f_vectors:
	maxv = 0
	for Fk_vector in f_vectors:
		current_manhattan_dist = manhattan_dist(Fj_vector, Fk_vector)
		if (current_manhattan_dist > maxv):
			maxv = current_manhattan_dist
	summ += maxv

result = sqrt(summ)
print "Problem: ", problem, " I_MS = %f" % result