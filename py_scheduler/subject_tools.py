import math
import json 

from .models.subject import Subject
from .models.day import Day, TimeRange
from .manage_exceptions import manage_row_exceptions
from .tools import *

def from_str_to_time_range(s):
	time_range = TimeRange()
	splitted = s.split('-')
	if(len(splitted) == 2):
		splitted = map(lambda sp: sp.replace(':', '.'), splitted)
		hours = list(map(float, splitted))
		time_range = TimeRange(hours[0], hours[1])

	return time_range
	

def from_str_to_day(s):
	day, hour_string, room = '', '', ''
	string_splitted = s.split("/")
	if len(string_splitted) == 3:
		day, hour_string, room = string_splitted
	elif len(string_splitted) == 2:
		day, hour_string = string_splitted

	#print(hour_string)
	time_range = from_str_to_time_range(hour_string)

	return {
		"day": day,
		"time_range": time_range,
		"room": room,
	}


def create_days(items):
	days = []
	for key, value in items.items():
		if "day/hour/room" in key:
			days.append(Day(**from_str_to_day(value)))
	
	return days

def from_row_to_subject(row):
	sub_items = {}
	for c_name in row.index:
		sub_items[c_name.lower()] = row[c_name]
		# Clean the nan values
		if(type(row[c_name]) == float):
			if(math.isnan(row[c_name])):
				sub_items[c_name.lower()] = ''

	sub_items["time_zones"] = create_days(sub_items)
	return Subject(**sub_items)

def from_df_to_subjects(df):
	subjects = []
	for _, row in df.iterrows():
		row = manage_row_exceptions(row)
		try:
			subjects.append(from_row_to_subject(row))
		except Exception as e:
			print("Hubo un error en:")
			print(row)
			raise Exception(e)

	return subjects

def filter_my_subjects(my_subjects_list, all_subjects):
	# Normalize my subjects
	my_norm_subs = list(map(super_normalize, my_subjects_list))
	name = all_subjects[0].name
	all_my_subjects = {}
	for sub in all_subjects:
		if sub.name in my_norm_subs:
			if sub.name not in all_my_subjects: all_my_subjects[sub.name] = []
			all_my_subjects[sub.name].append(sub)

	return all_my_subjects

def print_subject_list(subjects):
	for subject in subjects:
		print(subject)
		print('--------')

def from_subjects_to_json(all_subjects):
	all_subjects_json = []
	for subjects in all_subjects:
		subjects_json = []
		for subject in subjects:
			subjects_json.append(subject.for_jsonify())

		all_subjects_json.append(subjects_json)

	return json.dumps(all_subjects_json, indent=2)


