from .tools import *

def filter_my_subjects(my_subjects, all_subjects):
	# Normalize my subjects
	my_norm_subs = [super_normalize(s) for s in my_subjects]
	name = all_subjects.columns[0]
	all_my_subjects = []
	for _, row in all_subjects.iterrows():
		if row[name] in my_norm_subs:
			if row[name] not in all_my_subjects: all_my_subjects[row[name]] = []
			all_my_subjects[row[name]].append(row)

	return all_my_subjects