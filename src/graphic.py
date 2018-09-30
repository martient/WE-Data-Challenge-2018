#!/usr/bin/python
# coding: utf-8

from math import *
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

def test():
	# Black removed and is used for noise instead.
	unique_labels = set(labels)
	colors = [plt.cm.Spectral(each)
		for each in np.linspace(0, 1, len(unique_labels))]
	for k, col in zip(unique_labels, colors):
		if k == -1:
			# Black used for noise.
			col = [0, 0, 0, 1]
		class_member_mask = (labels == k)
		xy = X[class_member_mask & core_samples_mask]
		plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
			markeredgecolor='k', markersize=14)
		xy = X[class_member_mask & ~core_samples_mask]
		plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
			markeredgecolor='k', markersize=6)
	plt.title('Estimated number of clusters: %d' % n_clusters_)
	plt.show()
	pass

test()