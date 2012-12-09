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


# Deviation from Uniform distribution indicator
def evk_dist(Fi_vector, Fj_vector):		# distance between two points
	return sqrt((Fi_vector[0] - Fj_vector[0])**2 + (Fi_vector[1] - Fj_vector[1])**2)

d = []
for Fj_vector in f_vectors:
	minv = 9000
	for Fk_vector in f_vectors:
		if (Fj_vector == Fk_vector):
			continue;
		current_evk_dist = evk_dist(Fj_vector, Fk_vector)
		if (current_evk_dist < minv):
			minv = current_evk_dist
	d.append(minv)

d_mean = sum(d) / float(len(d))
summ = 0
for dj in d:
	summ = summ + abs(dj - d_mean)
result = summ / archive_potency
print "Problem: ", problem, " I_DU = %f" % result