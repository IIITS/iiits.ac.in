import re
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
