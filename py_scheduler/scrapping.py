from bs4 import BeautifulSoup
import requests

def fetch_page(url):
	page = requests.get(url)
	return BeautifulSoup(page.content, 'html.parser')

def get_rows(page):
	table = page.find_all('tbody')[1]
	rows = table.find_all("tr")
	return rows

def get_column_names(row):
	table_column_names = []
	for data in row.find_all('td')[1:]: # Ignoring the index
		table_column_names.append(data.text.strip())

	return table_column_names

def get_content_rows(rows):
	pd_rows = []
	for row in rows:
		pd_row = [] # Note is different from pd_rows
		for data in row.find_all('td'):
			pd_row.append(data.text) # Save the rows
		pd_rows.append(pd_row)

	return pd_rows