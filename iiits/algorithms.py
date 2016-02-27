from iiits.lang import *
from iiits.models import *
from math import floor, ceil
class PaginationAlgorithm:
	def __init__(self, num_entries_per_page):
		self.num_pages = 0
		self.num_entries_per_page = num_entries_per_page 
		self.num_alpha_per_set = 0
		self.lang = 'EN'
	def divide(self, entries):
		'''
		Divides the page into number of pages.	
		'''
		num_alphabets_lang = LANG[self.lang]['num_alphabets']
		if entries > self.num_entries_per_page:
			try:
				self.num_pages = int(ceil(float(entries) / float(self.num_entries_per_page)))
			except ZeroDivisionError:
				self.num_pages = 1
			
			try:
				if self.num_pages >= num_alphabets_lang:
					self.num_alpha_per_set = int(ceil(float(num_alphabets_lang) / float(self.num_pages)))
				else:
					self.num_alpha_per_set = int(ceil(float(num_alphabets_lang) / float(self.num_pages)))
			except ZeroDivisionError:
				 	self.num_alpha_per_set = num_alphabets_lang
		
		else: 
			self.num_pages = 1
		
		return True
	
	def numberOfPages(self):
		'''
		To retrieve the number of Pages used for Pagination
		'''
		return self.num_pages
	def numberOfEntriesPerPage(self):
		'''
		To retrieve number of Entries that would appear on a single page
		'''
		return self.num_entries_per_page
	def alphaSet(self):
		'''
		To receive an equally divided list of sets
		'''
		alpha_per_set = self.num_alpha_per_set
		alphabets = LANG[self.lang]['alphabets']
		alpha_set = dict()
		alpha_set['length'] = 0 
		alpha_set['set'] = dict()
		# stores the actual alphabet sets
		for j in range(0, self.numberOfPages()):
			alpha_set['length']+=1
			for i in range(0,self.num_alpha_per_set):
				try:
					alph = alphabets[0]
					alphabets.remove(alph)
					if alpha_set['length'] in alpha_set['set'].keys():
						alpha_set['set'][alpha_set['length']].append(alph)
					else:	
						alpha_set['set'][alpha_set['length']]=list(alph)
				except IndexError:
					break

		return alpha_set	

	def setlang(self, lang):

		if lang in LANG.keys():
			self.lang = lang
			return True
		return False	

class FacultySearch:
	def __init__(self,dept,title, ra, vs, instfac):
		if dept != 'all':
			self.department= Department.objects.get(code=dept)
		else:
			self.department= 'all'
		if title != 'all':		
			self.title= FacultyTitle.objects.get(code=title)
		else: 	
			self.title = 'all'
		if ra != 'all':	
			self.ra = ResearchArea.objects.get(code=ra)
		else:
			self.ra = 'all'	
		self.vs = vs
		self.instfac = instfac
	def getAllFaculty(self):
		results=dict()
		results['instfac'] = Faculty.objects.order_by('getFullName')
		results['vsfac']   = VisitingFaculty.objects.order_by('getFullName')
		return results
	def getInstFaculty(self):
		results = dict()
		results['instfac'] = Faculty.objects.order_by('getFullName')
		results['vsfac'] = None
		return results
	def getVisFaculty(self):
		results = dict()
		results['instfac']=None
		results['vsfac'] = VisitingFaculty.objects.order_by('getFullName')
		return results
	def getFacultyByDept(self):	
		results = dict()
		results['instfac']=Faculty.objects.filter(department=self.department).order_by('getFullName')
		results['vsfac']=None
		return results
	def getFacultyByTitle(self):
		results = dict()
		results['instfac']=Faculty.objects.filter(title=self.title).order_by('getFullName')
		results['vsfac']=None
		return results
	def getFacultyByResearch(self):
		results = dict()
		results['instfac']=Faculty.objects.filter(dept=self.dept).order_by('getFullName')
		results['vsfac']=None
		return results		
	def search(self):
		if self.dept != 'all':
			results = getFacultyByDept()
		elif self.title != 'all': 
		    results = getFacultyByTitle()
		elif self.ra != 'all':
			results = getFacultyByResearch()
		elif self.vs == 'true' and self.instfac == 'false':
			results = getVisFaculty()
		elif self.vs == 'false' and self.instfac == 'true':
			results = getInstFaculty()
		else:
			results = getAllFaculty()
		return results		
	
