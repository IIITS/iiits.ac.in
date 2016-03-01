import re
import math
from iiits.models import * 
def ifNone(obj, beautifier):
	if obj is None:
		return beautifier
	else:
		return obj	

def getPublicURI(path):
	results = re.search(r'(?<=~)[A-Za-z_.]*',path)
	print path
	return results.group(0)

def getAllFacultyByRA(raid):
	F = Faculty.objects.all()
	results = []
	for f in F:
		if	raid in f.research_areas:
			results.append(f)
	return results		

def getPageButtons(num_pages, curr_page, entries_per_page):
	lower = curr_page - int(math.floor(entries_per_page / 2 ))
	upper = curr_page + int(math.floor(entries_per_page / 2 ))
	
	if lower <= 0:
		lower = 1
		upper = entries_per_page
	if upper >= num_pages:
		if num_pages >= entries_per_page:
			lower = num_pages - entries_per_page
			upper= num_pages
		else:
			lower = 1	
			upper = num_pages
	buttons = [ x for x in range(lower, upper+1)]	
	return buttons