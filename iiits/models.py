from __future__ import unicode_literals
from django.conf import settings
from django.db.models import *
from django.contrib.auth.models import User
from iiits.config import values, static_locations
from django.utils.text import slugify
from ckeditor.fields import RichTextField
import math

from django.utils.timezone import now, timedelta
class Config(Model):
	property_name  = CharField(max_length=50)
	property_value = RichTextField()
	def __str__(self):
		return self.property_name
class StaticImages(Model):
	identifier = CharField(unique=True, max_length=255)
	image = ImageField(upload_to='iiits/images/misc/')
	def __str__(self):
		return self.identifier		
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
	background=ImageField(default='',upload_to=static_locations["ResearchArea"])
	def __str__(self):
		return self.title
		
class Faculty(Model):
	user = OneToOneField(User)
	photo=ImageField(upload_to='iiits/static/iiits/images/faculty/')
	title = ForeignKey(FacultyTitle)
	research_areas = RichTextField(default='Not available')
	department = ForeignKey(Department)
	contact = RichTextField(default='Not provided')
	professional_edu=RichTextField()
	website=RichTextField()
	other_info=RichTextField(default='NA')
	achievements=RichTextField(default='NA')
	public_uri_name=CharField(max_length=100, db_index=True,default='NA', unique=True)
	courses = RichTextField(default='Not available at the moment')
	show_achievements = BooleanField(default=True)
	show_website = BooleanField(default=True)
	show_contact = BooleanField(default=True)
	show_other_info = BooleanField(default=True)
	def getFullName(self):
		return self.user.get_full_name()
	def __str__(self):
		return self.getFullName()	
		


class Institute(Model):
	title = CharField(max_length=150)
	code = CharField(max_length=20)
	website = CharField(max_length=150)
	def __str__(self):
		return self.title
class VisitingFaculty(Model):
	user = OneToOneField(User)
	photo=ImageField(upload_to='iiits/static/iiits/images/faculty/')
	title = ForeignKey(FacultyTitle)
	institute = ForeignKey(Institute)
	courses= RichTextField()
	public_uri_name=CharField(max_length=100, db_index=True, default='NA', unique=True)

	def getFullName(self):
		return self.user.get_full_name()
	def __str__(self):
		return self.getFullName()


class News(Model):
	title 	= CharField(db_index= True,max_length=200)
	content	= RichTextField(default='NA')
	fileupload = FileField(upload_to='iiits/static/iiits/files/news/',null=True,blank=True)
	image = ImageField(upload_to='iiits/static/iiits/images/news/',null=True, blank=True)
	date = DateTimeField(auto_now_add = True)
	def __str__(self):
		return self.title

class NewsStory(Model):
	news = TextField(default='')
	date = DateTimeField( editable=True)
	def __str__(self):
		return self.news
		
class Notice(Model):
	title = CharField(max_length=200)
	description = TextField(default='NA')
	fileupload = FileField(upload_to = 'iiits/static/iiits/files/notice/', null=True, blank=True)
	date = DateTimeField(auto_now_add=True)
	valid_until = DateTimeField(default=now() + timedelta(days=7), editable=True)
	show_description = BooleanField(editable=True,default=False)
	show_fileupload = BooleanField(editable=True,default=False)
	def __str__(self):
		return self.title 
	def show_fileupload(self):
		self.fileupload = True
	def show_description(self):
		self.description = True		
	def change_valid_until(self, datetimefield):
		self.valid_until = datetimefield
	def change_title(self, title):
		self.title = title
class TenderType(Model):
	name=CharField(max_length=255)
	def __str__(self):
		return self.name			
class Tender(Notice,Model):		
	tender_type = ForeignKey(TenderType)

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
		return "/research/centres/"+slugify(self.title)	
	def get_profile(self):
		return ResearchCentreProfile.objects.get(centre=self)
		

class ResearchCentreProfile(Model):
	centre = ForeignKey(ResearchCentre)
	background = ImageField(upload_to=static_locations['ResearchPortfolio'], null=True, blank=True)
	description = RichTextField(default="Sorry, description unavailable at the moment.")
	faculty = RichTextField(default='')
	people = RichTextField(default='')	
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
	research_centres = TextField() #saves comma seperated code of ResearchCentre
	mentors = TextField() # saves comma seperated user.username of faculty or vsfaculty
	photo = ImageField(upload_to=static_locations["ResearchPortfolio"], blank=True, null=True)
	def __str__(self):
		return self.user.get_full_name()
	def image_exist(self):
		return self.photo.__bool__()
class Publication(Model):
	title= CharField(db_index=True,max_length=200)
	description=RichTextField(default='NA')
	link=RichTextField(default='NA')
	fileupload = FileField(upload_to='iiits/static/files/publications/', null=True, blank=True)
	year=CharField(db_index=True,max_length=4, choices=values['YEAR_PUBLICATIONS'])	
	starred=BooleanField(db_index=True,default=False)
	authors = RichTextField(default='NA')
	add_date = DateTimeField(auto_now_add=True, db_index=True)
	keywords=TextField(default='NA')
	def __str__(self):
		return self.title

	def getAuthors(self):
		authors = self.authors.split(',')
		list_authors = list()
		for author in authors:
			user = User.objects.get(username=author.strip())
			list_authors.append(user)
		return list_authors	

	def setAuthors(self, list_authors):
		set_author = str()
		if self.authors == 'NA':
			for x in list_authors:		
				set_author+=x+(',')
			set_author = set_author[:-1]	
		if self.authors!='NA':	
			set_author = self.authors
			for x in list_authors:		
				set_author+=','+x

	def setDescription(self, description):
		self.description = description
		return self.description

	def star(self):
		self.starred = not self.starred
		return self.starred

	def attachFile(self, fileupload):
		self.fileupload = fileupload			 			
		return self.fileupload

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
	title=CharField(max_length=255)
	image= ImageField(upload_to='iiits/static/iiits/images/topstories/')
	body= RichTextField()
	show_on_home_page= BooleanField(default=False)
	date= DateTimeField(auto_now_add=True, editable=True)
	def __str__(self):
		return self.title

	def profile(self):
		return "/mediaroom/topstories/"+slugify(self.title)
	def slug(self):
		return slugify(self.title)	
			

######################
# Campus Life Models #
######################

class CampusLifeEntity(Model):
	'''
	description: Describes a campus life main model. These are displayed in the navigation bar.
	'''
	name = CharField(max_length=255)
	code = CharField(max_length=20, db_index=True)
	rank = PositiveIntegerField(default=100)
	def __str__(self):
		return str(self.name)

class CampusLifeSubEntity(Model):
	belongs_to = ForeignKey(CampusLifeEntity)
	title = CharField(max_length=255)
	description=RichTextField()
	picture=ImageField(upload_to='iiits/images/campuslife/contents')
	show_picture = BooleanField(default=False)
	links = RichTextField()
	show_links=BooleanField(default=False)
	def __str__(self):
		return self.title+ " : "+ str(self.belongs_to)
		
class ContactAddress(Model):
	title = CharField(max_length=255)
	address = RichTextField()
	def __str__(self):
		return self.title
class WriteToUsQuery(Model):
	name = CharField(max_length=255)
	email = CharField(max_length=255)
	phone = CharField(max_length=20)
	query = TextField()
	time = DateTimeField(auto_now_add=True)		
	