from py_scheduler import *

"""
Needs:
url:          string   -> The url of the page
subjects:     [string] -> List of subjects to check (Maybe in a file)
time_columns: [int]    -> List of indexes of the columns with the day/hour/room names
"""

my_subjects = [
	"Cálculo de Varias Variables",
	"Ecuaciones Diferenciales Ordinarias",
	"Fluidos, Ondas y Temperatura",
	"BIOFÍSICA"
]

column_names = [
	"name",
	"group",
	"date/hour/room",
	"date/hour/room",
	"date/hour/room",
	"professor",
	"email",
	"professor2",
	"email2",
]

def main():
	# Some variables needed
	all_subjects_file_name = "data/all_subjects"
	# ============ Make the request and build the tables ============ #
	# If we already have done the request an it is up-to-date then I will not request for it again.
	if(not check_for_table_file(True, all_subjects_file_name)):
		print("File not created yet")
		# Define url
		url = "http://www.dci.ugto.mx/estudiantes/index.php/mcursos/horarios-licenciatura"
		# Generate the subject file
		generate_subject_file(url, all_subjects_file_name, column_names)
	# ============ Read the file generated ============ #
	all_subjects = read_table_file(all_subjects_file_name)
	# ============ Normalize my subs and filter all subjects ============ #
	all_my_subjects = filter_my_subjects(my_subjects, all_subjects)
	print(all_my_subjects)
	# ============ Now we ============ #

	

if __name__ == "__main__":
	main()