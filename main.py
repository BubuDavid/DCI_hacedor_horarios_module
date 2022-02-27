from py_scheduler import *

"""
Needs:
url:          string -> The url of the page
time_columns: [int]  -> Indexes of the columns with the day/hour/room names
"""

def main():
	# ============ Make the request and build the tables ============ #
	# If we already have done the request an it is up-to-date then I will not request for it again.
	if(not check_for_table_file(True)):
		print("File not created yet")
		# Define url
		url = "http://www.dci.ugto.mx/estudiantes/index.php/mcursos/horarios-licenciatura"
		# Generate the subject file
		generate_subject_file(url)
	# ============ Read the file generated ============ #
	all_subjects = read_file('subjects')
	print(all_subjects)

if __name__ == "__main__":
	main()