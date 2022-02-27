import unicodedata

def super_normalize(s):
	return ''.join(c for c in unicodedata.normalize('NFD', s) 
					if unicodedata.category(c) != 'Mn').upper()