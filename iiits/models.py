from __future__ import unicode_literals
from django.conf import settings
from django.db.models import *
from django.contrib.auth.models import User
from iiits.config import values, static_locations
from django.utils.text import slugify
class Config(Model):
	property_name  = CharField(max_length=50)
	property_value = TextField()
	def __str__(self):
		return self.property_name
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
	research_areas = TextField(default='')#ResearchArea codes comma-separated
	department = ForeignKey(Department)
	contact_no=TextField()
	professional_edu=TextField()
	website=TextField()
	other_info=TextField(default='NA')
	achievements=TextField(default='NA')
	public_uri_name=CharField(max_length=100, db_index=True,default='NA', unique=True)


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


class Institute(Model):
	title = CharField(max_length=150)
	code = CharField(max_length=20)
	website = CharField(max_length=150)
	def __str__(self):
		return self.title
class VisitingFaculty(Model):
	user = OneToOneField(User)
	photo = photo=ImageField(upload_to='iiits/static/iiits/images/faculty/')
	title = ForeignKey(FacultyTitle)
	institute = ForeignKey(Institute)
	courses= TextField()
	public_uri_name=CharField(max_length=100, db_index=True, default='NA', unique=True)

	def getFullName(self):
		return self.user.get_full_name()
	def __str__(self):
		return self.getFullName()
class Course(Model):
	'''
	This Model stores the details of the courses being taught at the university.\n
	Fields are:\n
	1) courseid - unique id of the course by which it could be identified. max length is 20.\n
	2) name - Name of the course\n
	3) faculties - comma separated list of faculties. Please note that there shouldn't be spaces before or after a comma. If you are editing this using the CMS, then you need not worry about public uri name of faculty. However, if you editing through the web administration, please not that you need to enter the public uri name without the '~' symbol. Eg: uma.garimella, hrishikesh etc.
	'''
	courseid=CharField(max_length=20, db_index=True)
	name=TextField()
	faculties=TextField()
	def __str__(self):
		return str(self.courseid) + " - " + str(self.name)
	def checkFacultyTeaches(self, fac_uri_name):
		if fac_uri_name in self.faculties.split(','):
			return True
		return False

class News(Model):
	title 	= CharField(db_index= True,max_length=200)
	content	= TextField(default='NA')
	fileupload = FileField(upload_to='iiits/static/iiits/files/news/',null=True,blank=True)
	image = ImageField(upload_to='iiits/static/iiits/images/news/',null=True, blank=True)
	date = DateTimeField(auto_now_add = True)

class Notice(Model):
	noticeno = CharField(max_length=20, db_index=True)
	title = CharField(max_length=200)
	fileupload = FileField(upload_to = 'iiits/static/iiits/files/notice/', null=True, blank=True)
	date = DateTimeField(auto_now_add=True)


class AdmissionsFeeStructure(Model):
	academic_year = CharField(max_length=200, default='2016-2017')
	tution_fee = TextField()
	admission = TextField()
	caution_deposit = TextField()
	hostel_water_electric = TextField()
	mess = TextField()
	textbooks = TextField()
	def __str__(self):
		return self.academic_year
class AdmissionsFeeModeofPayment(Model):
	title = CharField(max_length=50)
	description = TextField()
	def __str__(self):
		return self.title

class Notes(Model):
	title = CharField(max_length=100, db_index=True, 
					  choices=values["NOTES"], default=values["NOTES_DEFAULT"])
	notes = TextField()		
	def __str__(self):
		return self.title

class AdmissionsFinancialAssistance(Model):
	title = CharField(max_length=50)
	content = TextField()
	order_no = 	PositiveIntegerField(db_index=True)
	def __str__(self):
		return str(self.order_no) + " - " + self.title  



class AcademicsTimeTable(Model):
	batchnsem = CharField(max_length=20, choices=values["ACADEMICS_BATCHES"], 
					  default = values["ACADEMICS_BATCHES_DEFAULT"], db_index=True)
	branch = CharField(max_length=20, choices=values["ACADEMICS_BRANCHES"],
					   default=values["ACADEMICS_BRANCHES_DEFAULT"])
	
	fileupload = FileField(upload_to=static_locations["AcademicsTimeTable"])
	session = CharField(max_length=20, choices=values["ACADEMICS_SESSION"],
					    default=values["ACADEMICS_SESSION_DEFAULT"])
	year = CharField(max_length=10, choices=values["YEAR"],
					 default=values["YEAR_DEFAULT"])
	def __str__(self):
			return self.batchnsem + self.branch + self.session + self.year

class AcademicsProgramme(Model):
	programme = TextField()
	seats = TextField()
	def __str__(self):
		return self.programme

class AcademicsResources(Model):
	title = CharField(max_length=50, choices=values["ACADEMICS_RESOURCES"],
					  default=values["ACADEMICS_RESOURCES_DEFAULT"], db_index=True)
	session = CharField(max_length=20, choices=values["ACADEMICS_SESSION"],
					    default=values["ACADEMICS_SESSION_DEFAULT"])
	year = CharField(max_length=10, choices=values["YEAR"],
					 default=values["YEAR_DEFAULT"])
	fileupload = FileField(upload_to=static_locations["AcademicsResources"])
	def __str__(self):
			return self.title

class ResearchCentre(Model):
	code = CharField(db_index=True, max_length=20)
	title= CharField(db_index=True, max_length=150)
	research_areas= TextField()
	def __str__(self):
		return self.title
	def get_url(self):
		return "/research/centres/"+slugify(self.title)+"/"	

class ResearchCentreProfile(Model):
	centre = ForeignKey(ResearchCentre)
	description = TextField()
	people = TextField()	
	def __str__(self):
		return self.centre
class ResearchPortfolio(Model):
	research_areas = TextField()
	faculty = TextField(null=True, blank=True)
	title = CharField(max_length=200)
	description = TextField()
	image = ImageField(null=True, blank=True, upload_to=static_locations["ResearchPortfolio"])	
	fileupload = FileField(null=True, blank=True, upload_to=static_locations["ResearchPortfolio"])

class ResearchStudent(Model):
	user=OneToOneField(User)
	research_centres = TextField() #saves comma seperated code of ResearchCentre
	mentors = TextField() # saves comma seperated user.username of faculty or vsfaculty

class Publication(Model):
	title= CharField(db_index=True,max_length=200)
	description=TextField()
	link=TextField()
	fileupload = FileField(upload_to='iiits/static/files/publications/')
	year=CharField(db_index=True,max_length=4)	
	starred=BooleanField(db_index=True,default=False)
	authors = TextField()

class ImageSlider(Model):
	image = ImageField(upload_to='iiits/static/iiits/images/imageslider')
	order_no = CharField(max_length=20,default='0',choices=(('0','0'),
		('1','1'),
		('2','2'),
		('3','3'),
		('4','4'),
		('5','5'),
		('6','6'))
	)
	caption = TextField()
	def __str__(self):
		return self.order_no

class StaffDesignation(Model):
	name = CharField(max_length=100)
	def __str__(self):
		return self.name
class Staff(Model):
	user = ForeignKey(User)
	designation = ForeignKey(StaffDesignation)
	photo = ImageField(upload_to='iiits/static/iiits/images/staff')	
	def __str__(self):
		return self.user.get_full_name()	

class CareerType(Model):
	type_name = CharField(max_length=255)
	code = CharField(max_length=10)
	def __str__(self):
		return self.type_name
class Career(Model):
	title = CharField(max_length = 255)
	notification = FileField(upload_to='iiits/static/files/careers/')	
	is_expired = BooleanField(default=False)
	datetime = DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.title
class CareerNonFacultyPosition(Career, Model):		
	career_type = CharField(max_length=255, choices=CareerType.objects.all())
	details = TextField(null=True)
	def __str__(self):
		return self.title
class ConsultancyContract(Career, Model):
	def __str__(self):
		return self.title

class TopStory(Model):
	title=CharField(max_length=20)
	image= ImageField(upload_to='iiits/static/iiits/images/topstories/')
	body= TextField()
	news_link=ForeignKey(News)
	show_on_home_page= BooleanField(default=False)
	def __str__(self):
		return self.title
	def getLink(self):
		return slugify(self.news_link.title, allow_unicode=True)

