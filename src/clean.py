#!/usr/bin/python
# coding: utf-8

from math import *

def clean(dataset, delta, seuil):
	dataset_move = calc_move(dataset, delta)
	i = 0
	pic = False
	keep_time = []
	tmp = []
	pic_tmp = -1
	pic_time = 0
	while (i < len(dataset_move)):
		if (dataset_move[i] > seuil**2 and pic == False):
			pre_pic = 0
			pic = True
		elif (dataset_move[i] > seuil**2 and pre_pic >= 4 and pre_pic <= 20):
			for pic_time in tmp:
				keep_time.append(pic_time)
			tmp = []
			pic_tmp = -1
		elif (dataset_move[i] > seuil**2 and pre_pic > 20):
			tmp = []
			pic_tmp = i
			pre_pic = 0
		if (pic == True and pic_tmp != i):
			tmp.append(i)
			pre_pic += 1
		elif (pic == True):
			pre_pic += 1
		i += 1
	i = 0
	return keep_time

def calc_move(dataset, delta):
	y = 0
	i = 0
	len_data = len(dataset)
	len_col = len(dataset[0])
	dataset_move = []
	while (i + delta < len_col):
		y = 0
		tmp_move = 0
		while (y + 1 < len_data):
			X1 = float(dataset[y][i])
			X2 = float(dataset[y][i + delta])
			Y1 = float(dataset[y + 1][i])
			Y2 = float(dataset[y + 1][i + delta])
			tmp_move += (X2 - X1)**2 + (Y2 - Y1)**2
			y += 2
		dataset_move.append(tmp_move)
		i += delta
	return dataset_move