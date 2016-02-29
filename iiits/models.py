from __future__ import unicode_literals
from django.conf import settings
from django.db.models import *
from django.contrib.auth.models import User
class Department(Model):
	name = CharField(max_length=100)
	code = CharField(db_index=True,max_length=20)
	def __str__(self):
		return self.name
class FacultyTitle(Model):
	title = CharField(max_length=100)
	code = CharField(db_index=True,max_length=20)
	def __str__(self):
		return self.title
class ResearchArea(Model):
	title = CharField(max_length=150)
	code = CharField(db_index=True,max_length=50)
	def __str__(self):
		return self.title
		
class Faculty(Model):
	user = OneToOneField(User)
	photo=ImageField(upload_to='iiits/static/iiits/images/faculty/')
	title = ForeignKey(FacultyTitle)
	research_areas = CommaSeparatedIntegerField(max_length=150)#ResearchArea IDs
	department = ForeignKey(Department)
	contact_no=TextField()
	professional_edu=TextField()
	website=TextField()
	other_info=TextField(default='NA')
	achievements=TextField(default='NA')
	public_uri_name=CharField(max_length=100, db_index=True,default='NA')


	def getFullName(self):
		return self.user.get_full_name()
	def __str__(self):
		return self.getFullName()	
	def getAllResearchInterests(self):
		results = list()
		for x in self.research_areas:
			try:
				r = ResearchArea.objects.get(id=int(x))
				results.appends(r)
			except ObjectDoesNotExist:
				donothing=True	
		return results		

class VisitingFaculty(Model):
	user = OneToOneField(User)
	photo = photo=ImageField(upload_to=settings.STATIC_URL+'iiits/images/faculty/')
	institute = TextField()
	courses= TextField()
	public_uri_name=CharField(max_length=100, db_index=True, default='NA')
	
class Publications(Model):
	title= CharField(db_index=True,max_length=200)
	description=TextField()
	link=TextField()
	fileupload = FileField()
	year=CharField(db_index=True,max_length=4)	
	starred=BooleanField(db_index=True,default=False)
	
class News(Model):
	title 	= CharField(db_index= True,max_length=200)
	content	= TextField(default='NA')
	fileupload = FileField(upload_to=settings.STATIC_URL+'iiits/files/news/',null=True,blank=True)
	image = ImageField(upload_to=settings.STATIC_URL+'iiits/images/news/',null=True, blank=True)
	date = DateTimeField(auto_now_add = True)

'''
class Staff(Model):
class UGStudent(Model):
class PGStudent(Model):
class DoctoralStudent(Model):
class ResearchScholar(Model):
class Alumni(Model): 
'''
