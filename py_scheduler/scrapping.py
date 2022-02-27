import requests
from bs4 import BeautifulSoup
from .tools import super_normalize

def fetch_page(url):
	page = requests.get(url)
	return BeautifulSoup(page.content, 'html.parser')

def get_rows(page):
	table = page.find_all('tbody')[1]
	rows = table.find_all("tr")
	return rows

def get_column_names(column_names):
	table_column_names = []
	for data in column_names: # Ignoring the index
		table_column_names.append(normalize(data.strip()))

	return table_column_names

def get_content_rows(rows):
	pd_rows = []
	for row in rows:
		pd_row = [] # Note is different from pd_rows
		for data in row.find_all('td')[1:]:
			text = data.text.strip()
			normalized_text = normalize(text)
			pd_row.append(normalized_text) # Save the rows
		pd_rows.append(pd_row)

	return pd_rows