from file_tools import *
from scrapping import *

def generate_subject_file(url, file_name):
	# Request the page
	print("Fetching the page...")
	html_page = fetch_page(url)
	# Get all the rows
	rows = get_rows(html_page)
	# Get the column names
	table_column_names = get_column_names(rows[0])
	# Get the rows in a python matrix (list of lists)
	pd_rows = get_content_rows(rows[1:])
	# Generate a DataFrame and save in local
	create_file(
		f"{file_name}.csv",
		pd_rows,
		table_column_names
	)