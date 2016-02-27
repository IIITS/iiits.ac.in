from __future__ import unicode_literals

from django.db.models import *
from django.contrib.auth.models import User
class Department(Model):
	name = CharField(max_length=100)
	code = CharField(db_index=True,max_length=20)
class FacultyTitle(Model):
	title = CharField(max_length=100)
	code = CharField(db_index=True,max_length=20)
class ResearchArea(Model):
	title = CharField(max_length=150)
	code = CharField(db_index=True,max_length=50)
	
class Faculty(Model):
	user = OneToOneField(User)
	photo=ImageField(upload_to='iiits/static/iiits/images/faculty/')
	title = ForeignKey(FacultyTitle)
	research_areas = CommaSeparatedIntegerField(max_length=150)#ResearchArea IDs
	department = ForeignKey(Department)
	contact_no=TextField()
	professional_edu=TextField()
	website=TextField()
	def getFullName(self):
		return self.user.get_full_name()

class VisitingFaculty(Model):
	user = OneToOneField(User)
	photo = photo=ImageField(upload_to='iiits/static/iiits/images/faculty/')
	institute = TextField()
	courses= TextField()
	def getFullName(self):
		return self.user.get_full_name()
class Publications(Model):
	title= CharField(db_index=True,max_length=200)
	description=TextField()
	link=TextField()
	fileupload = FileField()
	year=CharField(db_index=True,max_length=4)	
	starred=BooleanField(db_index=True,default=False)
	

'''
class Staff(Model):
class UGStudent(Model):
class PGStudent(Model):
class DoctoralStudent(Model):
class ResearchScholar(Model):
class Alumni(Model):
class 
'''
