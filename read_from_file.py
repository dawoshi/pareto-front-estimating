# -*- coding: utf8 -*-

# Функция для чтения множества Парето из файла
def read_from_file(filestring):
	vectors = []
	strings = open(filestring).read().split('\n')
	for string in strings:
		val = string.split(' ')
		if (len(val) == 1 or len(val) == 2):
			break
		vector = [val[1], val[2]]
		vectors.append(vector)
	return vectors
