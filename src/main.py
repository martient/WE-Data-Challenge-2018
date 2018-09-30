#!/usr/bin/python
# coding: utf-8

import pandas as pd
import clean
import sys
from pprint import pprint
import csv
from io import StringIO
import os

def main():
	if len(sys.argv) < 2:
		print "ERREUR 01: VEUILLEZ SPÉCIFIER LE CHEMIN DU DATASET .csv"
		sys.exit(84)
	f = open(sys.argv[1], 'r')
	dataset_rush = list(csv.reader(f.read().splitlines()))
	data_to_keep = clean.clean(dataset_rush, 60, 190)

if __name__ == '__main__':
	main()