#! /usr/bin python
# coding: utf-8

def tranform_data(dataset, index_list):
	event_index = 1
	if len(index_list) > 0:
		json_format_tmp = {}
		while (event_index < len(index_list) + 1):
			user_index = 0
			json_format_tmp[event_index - 1] = {}
			json_format_tmp[event_index - 1]["id"] = event_index
			json_format_tmp[event_index - 1]["User"] = []
			while (user_index < len(dataset) / 2):
				json_format_tmp[event_index - 1]["User"].append({"id": user_index + 1,"x": dataset[user_index * 2][index_list[event_index - 1]],
					"y": dataset[user_index * 2 + 1][index_list[event_index - 1]]})
				user_index += 1
			event_index += 1
		return json_format_tmp