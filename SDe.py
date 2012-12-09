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

def byWhatEOneVectorDominateOther(vector1, vector2):			# vector1 dominate vector2; used in SpacingDistributionInE indicator
	e1 = vector1[0] / float(vector2[0])			# e in first component
	e2 = vector1[1] / float(vector2[1])			# e in first component
	e = max(e1, e2)							# taking max because min don't satisfy other inequality
	return e

# Spacing Distribution In E indicator
f1 = 0.00001
min_e = 9000
for Fj_vector in f_vectors:
	while f1 <= 1:
		f1_val = f1
		f2_val = f2(f1)
		Fk_vector = [f1_val, f2_val]
		e = byWhatEOneVectorDominateOther(Fj_vector, Fk_vector)
		if e < min_e:
			min_e = e
		f1 += 0.0001
result = min_e
print "Problem: ", problem, " I_SDe = %f" % result