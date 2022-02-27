import pandas as pd

def check_for_table_file(check, name):
	# We not always want to check for the file
	if not check:
		return check

	try:
		f = open(f"{name}.csv", "r")
		return True
	except:
		return False

def create_file(file_name, data, columns, index=False):
	df = pd.DataFrame(data, columns=columns)
	df.to_csv(f"{file_name}.csv", index=index)
	print("File created!")
	return df
	

def read_file(file_name):
	return pd.read_csv(file_name, header=0)