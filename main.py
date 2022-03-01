from py_scheduler import *

"""
Needs:
url:          string   -> The url of the page
subjects:     [string] -> List of subjects to check (Maybe in a file)
column_names  [string] -> List of the names of the columns in the csv
"""

url = "http://www.dci.ugto.mx/estudiantes/index.php/mcursos/horarios-licenciatura"

my_subjects = [
	"Cálculo de Varias Variables",
	"Ecuaciones Diferenciales Ordinarias",
	"BIOFÍSICA"
]

column_names = [
	"_id",
	"name",
	"group",
	"day/hour/room1",
	"day/hour/room2",
	"day/hour/room3",
	"professor1",
	"professor_email1",
	"professor2",
	"professor_email2",
]


def main():
	# Some variables needed
	all_subjects_file_name = "data/all_subjects"
	# ============ Make the request and build the tables ============ #
	# If we already have done the request an it is up-to-date then I will not request for it again.
	if(not check_for_table_file(True, all_subjects_file_name)):
		print("File not created yet")
		# Generate the subject file
		generate_subject_file(url, all_subjects_file_name, column_names)

	# ============ Read the file generated ============ #
	df_all_subjects = read_table_file(all_subjects_file_name)
	# ============ Transform the DataFrame to a list of Subject objects ============ #
	all_subjects = from_df_to_subjects(df_all_subjects)
	# ============ Normalize my subs and filter all subjects ============ #
	all_my_subjects = filter_my_subjects(my_subjects, all_subjects)
	# ============ Make every possible permutation of this subjects ============ #
	all_permutations = make_permutations(all_my_subjects)
	# ============ Filter the validate permutations (no overlap) ============ #
	validated_permutations = list(filter(filter_permutations, all_permutations))
	# ============ Transform the Subject List into a JSON ============ #
	my_subjects_json = from_subjects_to_json(validated_permutations)
	print(my_subjects_json)

if __name__ == "__main__":
	main()