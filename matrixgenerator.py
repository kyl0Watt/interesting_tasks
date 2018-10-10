#!/usr/bin/env python3
# -*- coding: utf8 -*-

import random


def matgen(x, y=-1):
	y = x if y == -1 else y
   	matrix = []
	for i in range(x):
		matrix.append([])
		for j in range(y):
			matrix[i].append(random.randint(10,99))
	return matrix


if __name__ == '__main__':
	print(matgen(3))
	print(matgen(3,4))
	print(matgen(9))
	print(matgen(9,18))