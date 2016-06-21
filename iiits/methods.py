import re
import math
from iiits.models import *
def chunksIntoThree(List):
	sz = len(List)
	L1 = list()
	L2 = list()
	L3 = list()
	for x in range(sz):
		if x % 3 == 0:
			L1.append(List[x])
		elif x % 3 == 1:
			L2.append(List[x])
		elif x % 3 == 2:
			L3.append(List[x])
			
	return [L1, L2, L3] 
def chunksIntoTwo(List):
	sz = len(List)
	L1 = list()
	L2 = list()
	
	for x in range(sz):
		if x % 2 == 0:
			L1.append(List[x])
		elif x % 2 == 1:
			L2.append(List[x])
		
			
	return [L1, L2] 	  

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
	lower = curr_page - int(math.floor(int(entries_per_page) / 2 ))
	upper = curr_page + int(math.floor(int(entries_per_page) / 2 ))
	
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


def getAllPublicationsFaculty(public_uri_name):
	Results = list()
	publications = Publication.objects.all()
	for p in publications:
		p_authors = p.authors.split(',')
		if public_uri_name in p_authors:
			Results.append(p)
	return Results			

def getAllFaculty():
	return Faculty.objects.order_by('user__first_name')
def getAllVisitingFaculty():
	return VisitingFaculty.objects.order_by('user__first_name')
def getAllStaff():
	return Staff.objects.order_by('user__first_name')
def getAllResearchCentres():
	return ResearchCentre.objects.order_by('title')
	
def getAllResearchAreas():
	return ResearchArea.objects.order_by('title')
	
#def getAllPublications():
#	return Publication.objects.
#def getPortfolio():

def getListOfScholars():
	return ResearchStudent.objects.order_by('user__first_name')
