# When the data base is horrible I will fix it by hand
def manage_row_exceptions(row):
	if(row["_ID"] == 42):
		print("File _ID 42 fixed")
		row["DAY/HOUR/ROOM1"] = "MARTES/15-17/F2"

	return row