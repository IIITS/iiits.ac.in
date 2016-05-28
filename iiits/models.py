from __future__ import unicode_literals
from django.conf import settings
from django.db.models import *
from django.contrib.auth.models import User
from iiits.config import values, static_locations
from django.utils.text import slugify
from ckeditor.fields import RichTextField
import math
class Config(Model):
	property_name  = CharField(max_length=50)
	property_value = RichTextField()
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
	research_areas = RichTextField(default='')#ResearchArea codes comma-separated
	department = ForeignKey(Department)
	contact_no=RichTextField()
	professional_edu=RichTextField()
	website=RichTextField()
	other_info=RichTextField(default='NA')
	achievements=RichTextField(default='NA')
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
	courses= RichTextField()
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
	name=RichTextField()
	faculties=RichTextField()
	def __str__(self):
		return str(self.courseid) + " - " + str(self.name)
	def checkFacultyTeaches(self, fac_uri_name):
		if fac_uri_name in self.faculties.split(','):
			return True
		return False

class News(Model):
	title 	= CharField(db_index= True,max_length=200)
	content	= RichTextField(default='NA')
	fileupload = FileField(upload_to='iiits/static/iiits/files/news/',null=True,blank=True)
	image = ImageField(upload_to='iiits/static/iiits/images/news/',null=True, blank=True)
	date = DateTimeField(auto_now_add = True)
	def __str__(self):
		return self.title
	
		
class Notice(Model):
	noticeno = CharField(max_length=20, db_index=True)
	title = CharField(max_length=200)
	fileupload = FileField(upload_to = 'iiits/static/iiits/files/notice/', null=True, blank=True)
	date = DateTimeField(auto_now_add=True)


class AdmissionsFeeStructure(Model):
	academic_year = CharField(max_length=200, default='2016-2017')
	tution_fee = RichTextField()
	admission = RichTextField()
	caution_deposit = RichTextField()
	hostel_water_electric = RichTextField()
	mess = RichTextField()
	textbooks = RichTextField()
	def __str__(self):
		return self.academic_year
class AdmissionsFeeModeofPayment(Model):
	title = CharField(max_length=50)
	description = RichTextField()
	def __str__(self):
		return self.title

class Notes(Model):
	title = CharField(max_length=100, db_index=True, 
					  choices=values["NOTES"], default=values["NOTES_DEFAULT"])
	notes = RichTextField()		
	def __str__(self):
		return self.title

class AdmissionsFinancialAssistance(Model):
	title = CharField(max_length=50)
	content = RichTextField()
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
	programme = RichTextField()
	seats = RichTextField()
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
	research_areas= RichTextField()
	def __str__(self):
		return self.title
	def get_url(self):
		return "/research/centres/"+slugify(self.title)+"/"	

class ResearchCentreProfile(Model):
	centre = ForeignKey(ResearchCentre)
	description = RichTextField()
	people = RichTextField()	
	def __str__(self):
		return self.centre
class ResearchPortfolio(Model):
	research_areas = RichTextField()
	faculty = RichTextField(null=True, blank=True)
	title = CharField(max_length=200)
	description = RichTextField()
	image = ImageField(null=True, blank=True, upload_to=static_locations["ResearchPortfolio"])	
	fileupload = FileField(null=True, blank=True, upload_to=static_locations["ResearchPortfolio"])

class ResearchStudent(Model):
	user=OneToOneField(User)
	research_centres = RichTextField() #saves comma seperated code of ResearchCentre
	mentors = RichTextField() # saves comma seperated user.username of faculty or vsfaculty

class Publication(Model):
	title= CharField(db_index=True,max_length=200)
	description=RichTextField()
	link=RichTextField()
	fileupload = FileField(upload_to='iiits/static/files/publications/')
	year=CharField(db_index=True,max_length=4)	
	starred=BooleanField(db_index=True,default=False)
	authors = RichTextField()

class ImageSlider(Model):
	"""
	A maximum of 6 images allowed in the image slider.
	Image with caption and its order no is stored.
	"""
	image = ImageField(upload_to='iiits/static/iiits/images/imageslider')
	order_no = CharField(max_length=20,default='0',choices=(('0','0'),
		('1','1'),
		('2','2'),
		('3','3'),
		('4','4'),
		('5','5'),
		('6','6'))
	)
	caption = RichTextField()
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
	description = RichTextField()
	is_expired = BooleanField(default=False)
	datetime = DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.title
class CareerNonFacultyPosition(Career, Model):		
	career_type = CharField(max_length=255, choices=CareerType.objects.all())
	details = RichTextField(null=True)
	def __str__(self):
		return self.title
class ConsultancyContract(Career, Model):
	def __str__(self):
		return self.title
class CareerFacultyPosition(Career, Model):
	def __str__(self):
		return self.title
class TopStory(Model):
	title=CharField(max_length=20)
	image= ImageField(upload_to='iiits/static/iiits/images/topstories/')
	body= RichTextField()
	news_link=ForeignKey(News)
	show_on_home_page= BooleanField(default=False)
	def __str__(self):
		return self.title
	def getLink(self):
		AllNews = News.objects.all()
		position = 0
		for x in range(1, len(AllNews)+1, 1):
			if AllNews[x-1] == self.news_link:
				position = x
				break
		NEWS_PAGINATION_MAX_ENTRIES = int(values['NEWS_PAGINATION_MAX_ENTRIES'])	
		page = math.ceil((position*1.0 )/(NEWS_PAGINATION_MAX_ENTRIES*1.0))
		return "newsroom/?page="+ str(int(page)) + "#"+slugify(self.news_link.title)

