#! /usr/bin python
# coding: utf-8

import json

#def tranform_data(dataset, index_list):
#	event_index = 0
#	if len(index_list) > 0 and len(index_list[0]) > 0:
#		while (event_index < len(index_list)):
#			user_index = 0
#			while (user_index < len(dataset) / 2):
#				json_format_tmp = {}
#				json_format_tmp["id"] = user_index
#				print json.dumps(json_format_tmp, ensure_ascii=False)
#				user_index += 1
#			event_index += 1

def test():
	user_index = 0
	while (user_index < 40):
		json_format_tmp = {}
		json_format_tmp["id"] = user_index
		json_format_tmp[{}] = []
		json_format_tmp["x"] = 10
		print json.dumps(json_format_tmp, ensure_ascii=False)
		user_index += 1
		pass
	pass

test()