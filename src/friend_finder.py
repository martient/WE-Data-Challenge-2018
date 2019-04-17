#!/usr/bin/python
# coding: utf-8

from sklearn.cluster import DBSCAN
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def exploit(data):
	clustering = DBSCAN(eps=5, min_samples=1, metric="precomputed").fit_predict(data)
	return clustering

def data_process(datas):
	for i in range(0, len(datas)):
		data = []
		distance = []
		for user in datas[i]["User"]:
			data.append([float(user["x"]), float(user["y"])])
		a = 0
		for user in data:
			tmp = []
			for user2 in data:
				X1 = float(user[0])
				X2 = float(user2[0])
				Y1 = float(user[1])
				Y2 = float(user2[1])
				tmp.append(sqrt((X2 - X1)**2 + (Y2 - Y1)**2))
			distance.append(tmp)
		plt.imshow(distance)
		plt.show()
		liste = []
		A = np.asarray(distance)
		for j in range(1, len(A) - 1):
			for k in range(i+1, len(A)):
				liste.append(A[j][k])
		# plt.hist(liste)
		tmp = np.percentile(np.array(liste), [i for i in range(11)])
		# plt.imshow(A < 999.65)
		cluster = exploit(np.asarray(distance))
		plot = []
		p = 0
		for user in data:
			if cluster[p] == 0:
				plt.scatter(user[0], user[1], s=40, c='red', label='Group 0')
			if cluster[p] == 1:
				plt.scatter(user[0], user[1], s=40, c='blue', label='Group 1')
			if cluster[p] == 2:
				plt.scatter(user[0], user[1], s=40, c='green', label='Group 2')
			if cluster[p] == 3:
				plt.scatter(user[0], user[1], s=40, c='pink', label='Group 3')
			if cluster[p] == 4:
				plt.scatter(user[0], user[1], s=40, c='yellow', label='Group 4')
			if cluster[p] == 5:
				plt.scatter(user[0], user[1], s=40, c='black', label='Group 5')
			if cluster[p] == 6:
				plt.scatter(user[0], user[1], s=40, c='purple', label='Group 6')
			if cluster[p] == 7:
				plt.scatter(user[0], user[1], s=40, c='orange', label='Group 7')
			if cluster[p] == 8:
				plt.scatter(user[0], user[1], s=40, c='brown', label='Group 8')
			if cluster[p] == 9:
				plt.scatter(user[0], user[1], s=40, c='grey', label='Group 9')
			p += 1
		plt.grid()
		plt.show()
		break