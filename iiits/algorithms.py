from iiits.lang import *
from iiits.models import *

from iiits.methods import *
from iiits import parsers
from math import floor, ceil

class PaginationAlgorithm:
	def __init__(self, num_entries_per_page):
		self.num_pages = 0
		self.num_entries_per_page = num_entries_per_page 
		self.num_alpha_per_set = 0
		self.lang = 'EN'
	def divide(self, data, entries):
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
	parser = parsers
	def __init__(self,dept,title, ra, vs, instfac):
		try:
			self.department= Department.objects.get(code=dept)
		except ObjectDoesNotExist:
			self.department= parsers.FACULTY_SEARCH['department']['default_value']
		try	:	
			self.title= FacultyTitle.objects.get(code=title)
		except ObjectDoesNotExist: 	
			self.title = parsers.FACULTY_SEARCH['title']['default_value']
		try:	
			self.ra = ResearchArea.objects.get(code=ra)
		except ObjectDoesNotExist:
			self.ra = parsers.FACULTY_SEARCH['research_area']['default_value']	
		try:
			self.vs = vs
		except ObjectDoesNotExist:
			self.vs = parsers.FACULTY_SEARCH['visiting_faculty']['default_value']
		try:	
			self.instfac = instfac
		except ObjectDoesNotExist: 
			self.instfac = parsers.FACULTY_SEARCH['institute_faculty']['default_value']	
	def classifier(self, TS, ES):
		length = len(TS)
		identified = list()
		for i in range(0, length):
			if TS[i] != ES[i].get('default_value'):
				identified.append(i)
				break
		return identified		
	def search(self):

		deptParser = parsers.FACULTY_SEARCH.get('department')
		titleParser = parsers.FACULTY_SEARCH.get('title')
		researchAreaParser = parsers.FACULTY_SEARCH.get('research_area')
		instfacParser = parsers.FACULTY_SEARCH.get('institute_faculty')
		vsParser = parsers.FACULTY_SEARCH.get('visiting_faculty')
		TrainerSet = [self.department, self.title, self.ra, self.vs, self.instfac]
		ExpectedSet = [deptParser,titleParser,researchAreaParser,instfacParser, vsParser]
		classified = self.classifier(TrainerSet, ExpectedSet)		
		if len(classified) == 0:
			results = {
			'instfac' : Faculty.objects.all(),
			'vsfac': VisitingFaculty.objects.all()
			}
		else:
			DECISION = {1:self.department,2:self.title,3:self.ra,4:self.vs,5:self.instfac}
			if 1 + classified[0] > 3:
				print "here", classified[0]
				results = {'instfac':  Faculty.objects.order_by('getFullName') , 'vsfac':None} if (1 + classified[0]) == 4 else { 'instfac':None, 'vsfac': VisitingFaculty.objects.order_by('user__first_name')}
			else:
				if   1 + classified[0] == 1:
					results = {
						'instfac': Faculty.objects.filter(department=self.department).order_by('getFullName'),
						'vsfac':None
					}
				elif 1 + classified[0] == 2:
					results = {
						'instfac': Faculty.objects.filter(title=self.title).order_by('getFullName'),
						'vsfac':None
					}	
				elif 1 + classified[0] == 3:
					results = {
						'instfac': getAllFacultyByRA(self.ra.id),
						'vsfac':None
					}
		return results			