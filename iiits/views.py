from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.http import JsonResponse
from iiits.models import *
from iiits.methods import *
from iiits.algorithms import *
from iiits.forms import *
from iiits.config import *

class About(TemplateView):
	template_name = templates['site']['about']['home']
	def get_context_data(self, **kwargs):
		context = super(About,self).get_context_data(**kwargs)
		context = dict()
		context['base'] = templates['base']['about']
		context['template_bog'] =templates['site']['about']['bog']
		context['template_about_iiit'] =templates['site']['about']['about_iiit']
		context['template_about_sricity'] =templates['site']['about']['about_sricity']
		context['template_location'] =templates['site']['about']['location']
		context['template_reaching_iiit'] =templates['site']['about']['reaching_iiit']
		return context

class Academics(TemplateView):
	template_name=templates['site']['academics']['home']
	def get_context_data(self, *args, **kwargs):
		context = super(Academics, self).get_context_data(*args, **kwargs)
		context['base'] = templates['base']['academics']
		context['academics_timetable'] = templates['site']['academics']['timetable']
		context['academics_curriculum'] = templates['site']['academics']['curriculum']
		context['academics_general_info'] = templates['site']['academics']['general_info']
		context['academics_programmes'] = templates['site']['academics']['programmes']
		context['timetable_ug1'] = AcademicsTimeTable.objects.get(batchnsem__startswith='UG1')
		context['timetable_ug2'] = AcademicsTimeTable.objects.get(batchnsem__startswith='UG2')
		context['timetable_ug3_cse'] = AcademicsTimeTable.objects.get(batchnsem__startswith='UG3',
														    	   branch='CSE')
		context['timetable_ug3_ece'] = AcademicsTimeTable.objects.get(batchnsem__startswith='UG3',
														           branch= 'ECE')	
		context['curriculum_ug1_sem1']= AcademicsResources.objects.get(title='CURRICULUM_UG1_SEM1')
		context['curriculum_ug1_sem2']= AcademicsResources.objects.get(title='CURRICULUM_UG1_SEM2')
		context['note_ug_curriculum'] = Notes.objects.get(title='UG_CURRICULUM')
		context['note_ug_curriculum_benchmarking'] = Notes.objects.get(title='UG_CURRICULUM_BENCHMARKING')
		context['programmes']= AcademicsProgramme.objects.all()
		context['note_programmes']=Notes.objects.get(title='ACADEMIC_PROGRAMMES')
		context['almanac']= AcademicsResources.objects.get(title='Almanac')
		context['calendar']= AcademicsResources.objects.get(title='CALENDAR')
		context['holidays'] = AcademicsResources.objects.get(title='HOLIDAYS')
		return context

class Admissions(TemplateView):
	template_name =  templates['site']['admissions']['home']
	def get_context_data(self, *args, **kwargs):
		context = super(Admissions,self).get_context_data(*args,**kwargs)
		context['title']=strings['admissions_title']
		context['base'] = templates['base']['admissions']
		context['admissions_undergraduate'] = templates['site']['admissions']['undergraduate']
		context['admissions_postgraduate'] = templates['site']['admissions']['postgraduate']
		context['fee_structure'] = AdmissionsFeeStructure.objects.all()[0]
		context['financial_assistance'] = AdmissionsFinancialAssistance.objects.order_by('order_no')
		context['policy'] = Notes.objects.get(title='POLICY')
		context['fee_mode_of_payment'] = AdmissionsFeeModeofPayment.objects.all()
		context['fee_mode_of_payment_notes'] = Notes.objects.get(title='FEE')
		return context

class Alumni(TemplateView):		
	template_name = templates['site']['alumni']['home']
	def get_context_data(self, **kwargs):
		context = super(Alumni,self).get_context_data(**kwargs)
		context = dict()
		context['alumni_base']= templates['base']['alumni']
		context['alumni_list']= templates['site']['alumni']['list']
		return context

class CampusLife(TemplateView):
	template_name = templates['site']['campus_life']['home']
	def get_context_data(self, **kwargs):
		context = super(CampusLife,self).get_context_data(**kwargs)
		context = dict()
		context['base'] = templates['base']['campus_life']
		return context

class FacultyPage(TemplateView):
	template_name = templates['site']['faculty']['home']
	def get_context_data(self, **kwargs):
		context = super(FacultyPage,self).get_context_data(**kwargs)
		context = dict()
		context['base'] = templates['base']['faculty']
		context['faculty_mast'] = templates['site']['faculty']['mast']
		faculty_list = getAllFaculty()
		vs_faculty_list = getAllVisitingFaculty()
		context['inst_faculty_list1'] = faculty_list[0]
		context['inst_faculty_list2'] = faculty_list[1]
	
		context['vs_faculty_list1'] = vs_faculty_list[0]
		context['vs_faculty_list2'] = vs_faculty_list[1]	
		return context

class FacultyProfile(TemplateView):
	template_name= templates['site']['faculty']['profile']
	def get_context_data(self, **kwargs):
		context = super(FacultyProfile,self).get_context_data(**kwargs)	
		context=dict()
		path=self.request.path
		public_uri_name = getPublicURI(path)
		try:
			faculty=Faculty.objects.get(public_uri_name=public_uri_name)
			
			context['faculty']=faculty
			context['search_status']=200
		except ObjectDoesNotExist:
			context['search_status']=404		
		context['base'] = templates['base']['faculty']
		context['faculty_mast'] = templates['site']['faculty']['mast']
		context['faculty_bio'] = templates['site']['faculty']['bio']
		context['faculty_publications'] = templates['site']['faculty']['publications']
		context['faculty_teaching']	= templates['site']['faculty']['teaching']
		context['courses']= getAllCoursesFaculty(public_uri_name=public_uri_name)
		context['publications']=getAllPublicationsFaculty(public_uri_name=public_uri_name)
		return context


class Home(TemplateView):
	template_name = 'iiits/index.html'
	
	def get_context_data(self, **kwargs):
		
		context = super(Home,self).get_context_data(**kwargs)
		context = {

		}
		
		return context

class MediaRoom(TemplateView):
	template_name = templates['site']['mediaroom']['home']
	def get_context_data(self, **kwargs):
		context = super(MediaRoom,self).get_context_data(**kwargs)
		context = dict()
		context['base']=templates['base']['mediaroom']
		return context

class NewsRoom(TemplateView):	
	template_name = templates['site']['news']['home']
	
	def get_context_data(self, *args, **kwargs):
		context = super(NewsRoom,self).get_context_data(*args,**kwargs)
		context['base']=templates['base']['news']
		all_news = News.objects.all().order_by('-date') #latest news first
		paginator = Paginator(all_news, values.get('NEWS_PAGINATION_MAX_ENTRIES'))
		page = self.request.GET.get('page')
		try:
			page=int(page)
		except TypeError:
			page=1	
		 
		context['pagebuttons'] = getPageButtons(paginator.num_pages, page, values.get('NEWS_PAGINATION_MAX_ENTRIES'))
		
		try:
        		page_news = paginator.page(page)
    		except PageNotAnInteger:
        		page_news = paginator.page(1)
    		except EmptyPage:
        		page_news = paginator.page(paginator.num_pages)
        	context['page_news']=page_news

		return context


class Notice(TemplateView):
	template_name = templates['site']['notice']['home']
	def get_context_data(self, *args, **kwargs):
		context = super(Notice,self).get_context_data(*args,**kwargs)
		context['base']=templates['base']['notice']
		return context
class Parents(TemplateView):
	template_name = templates['site']['parents']['home']
	def get_context_data(self, *args, **kwargs):
		context = super(Parents,self).get_context_data(*args,**kwargs)
		context['base']=templates['base']['parents']
		return context
class Staff(TemplateView):
	template_name = templates['site']['staff']['home']
	def get_context_data(self, *args, **kwargs):
		context = super(Staff,self).get_context_data(*args,**kwargs)
		context['base']=templates['base']['staff']
		return context
class Students(TemplateView):
	template_name = templates['site']['students']['home']
	def get_context_data(self, *args, **kwargs):
		context = super(Students,self).get_context_data(*args,**kwargs)
		context['base']=templates['base']['students']
		return context
class Alumni(TemplateView):
	template_name = templates['site']['alumni']['home']
	def get_context_data(self, *args, **kwargs):
		context = super(Alumni,self).get_context_data(*args,**kwargs)
		context['base']=templates['base']['alumni']
		return context		
class Research(TemplateView):
	template_name=templates['site']['research']['home']
	def get_context_data(self, **kwargs):
		context = super(Research,self).get_context_data(**kwargs)
		context = dict()
		context['title']=strings['research_title']
		context['base'] = templates['base']['research']
		context['research_areas'] = templates['site']['research']['areas']
		context['research_centres'] = templates['site']['research']['centres']
		context['research_portfolio'] = templates['site']['research']['portfolio']
		context['research_publications'] = templates['site']['research']['publications']
		context['research_scholars'] = templates['site']['research']['scholars']
		context['centres1'] = getAllResearchCentres()[0]
		context['centres2'] = getAllResearchCentres()[1]
		context['centres3'] = getAllResearchCentres()[2]
		context['areas1'] = getAllResearchAreas()[0]
		context['areas2'] = getAllResearchAreas()[1]
		context['areas3'] = getAllResearchAreas()[2]
			
		#context['publications'] = getAllPublications()
		#context['portfolio'] = getPortfolio()
		context['scholars'] = getListOfScholars()

		return context
class ResearchAreaProfile(TemplateView):
	template_name = templates['site']['research']['area_profile']
class ResearchCentreProfile(TemplateView):
	template_name = templates['site']['research']['centre_profile']


class StudentProfile(TemplateView): 		
	template_name=''
	def get_context_data(self, **kwargs):
		context = super(StudentProfile,self).get_context_data(**kwargs)
		context = dict()

		return context
	


