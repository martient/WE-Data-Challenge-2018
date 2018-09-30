#!/usr/bin/python
# coding: utf-8

from pprint import pprint
import json_transform as transform
import friend_finder as ff
import clean
import sys
import csv
import json

def main():
	if len(sys.argv) < 2:
		print "ERREUR 01: VEUILLEZ SPÉCIFIER LE CHEMIN DU DATASET .csv"
		sys.exit(84)
	f = open(sys.argv[1], 'r')
	dataset_rush = list(csv.reader(f.read().splitlines()))
	f.close()
	data_to_keep = clean.clean(dataset_rush, 60, 190)
	json_dataset = transform.tranform_data(dataset_rush, data_to_keep)
	f = open("ressource/dataset.json", "w")
	f.write(json.dumps(json_dataset))
	f.close()
	ff.data_process(json_dataset)


if __name__ == '__main__':
	main()