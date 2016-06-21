from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import JsonResponse, HttpResponseRedirect
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
		context['base'] = templates['base']['root']
		context['mast'] = templates['build']['mast']
		context['MAST_TEXT']="About"
		context['template_bog'] =templates['site']['about']['bog']
		context['template_about_iiit'] =templates['site']['about']['about_iiit']
		context['template_about_sricity'] =templates['site']['about']['about_sricity']
		context['template_location'] =templates['site']['about']['location']
		context['template_reaching_iiit'] =templates['site']['about']['reaching_iiit']
		context['template_contact_us'] =templates['site']['about']['contact_us']
		return context

class Academics(TemplateView):
	template_name=templates['site']['academics']['home']
	def get_context_data(self, *args, **kwargs):
		context = super(Academics, self).get_context_data(*args, **kwargs)
		context['base'] = templates['base']['root']
		context['mast'] = templates['build']['mast']
		context['MAST_TEXT']="Academics"
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
		context['base'] = templates['base']['root']
		context['mast'] = templates['build']['mast']
		context['MAST_TEXT']="Admissions"
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
		context['base'] = templates['base']['root']
		context['alumni_list']= templates['site']['alumni']['list']
		context['mast'] = templates['build']['mast']
		context['MAST_TEXT']="Alumni"
		return context

class CampusLife(TemplateView):
	template_name = templates['site']['campus_life']['home']
	def get_context_data(self, **kwargs):
		context = super(CampusLife,self).get_context_data(**kwargs)
		context = dict()
		context['base'] = templates['base']['root']
		context['mast'] = templates['build']['mast']
		context['MAST_TEXT']="Campus Life"
		context['templates_facilities'] = templates['site']['campus_life']['facilities']
		context['templates_events'] = templates['site']['campus_life']['events']
		context['templates_student_life'] = templates['site']['campus_life']['student_life']
		context['facilities'] = Facility.objects.order_by('title')
		context['events'] = Event.objects.order_by('title')
		context['student_life_articles'] = StudentLifeArticle.objects.order_by('title')
		return context
class Career(TemplateView):
	template_name = templates['site']['career']['home']
	def get_context_data(self, **kwargs):
		context = super(Career,self).get_context_data(**kwargs)
		context = dict()
		context['base'] = templates['base']['root']
		context['mast'] = templates['build']['mast']
		context['templates_fac'] = templates['site']['career']['fac']
		context['templates_non_fac'] = templates['site']['career']['non_fac']
		context['templates_consultancy'] = templates['site']['career']['consultancy']
		context['MAST_TEXT']="Careers"
		context['fac'] = 	    CareerFacultyPosition.objects.filter(is_expired=False).order_by('-datetime')
		context['non_fac'] = CareerNonFacultyPosition.objects.filter(is_expired=False).order_by('-datetime')
		context['consultancy'] =  ConsultancyContract.objects.filter(is_expired=False).order_by('-datetime')
		return context

class FacultyPage(TemplateView):
	template_name = templates['site']['faculty']['home']
	def get_context_data(self, **kwargs):
		context = super(FacultyPage,self).get_context_data(**kwargs)
		context = dict()
		context['base'] = templates['base']['root']
		context['mast'] = templates['build']['mast']
		context['MAST_TEXT']="Faculty"
		faculty_list = getAllFaculty()
		vs_faculty_list = getAllVisitingFaculty()
		context['inst_faculty_list'] = getAllFaculty()
		context['vs_faculty_list'] = getAllVisitingFaculty()
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
		context['base'] = templates['base']['root']
		context['mast'] = templates['build']['mast']
		context['MAST_TEXT']="Faculty"
		context['faculty_bio'] = templates['site']['faculty']['bio']
		context['faculty_publications'] = templates['site']['faculty']['publications']
		context['faculty_teaching']	= templates['site']['faculty']['teaching']
		context['publications']=getAllPublicationsFaculty(public_uri_name=public_uri_name)
		return context


class Home(TemplateView):
	template_name = 'iiits/index.html'
	
	def get_context_data(self, **kwargs):
		
		context = super(Home,self).get_context_data(**kwargs)
		image_slider = ImageSlider.objects.order_by('order_no')
		context = {
			'image_slider_no':[x for x in range(1,len(image_slider)+1,1)],
			'image_slider_images':image_slider,
			'topstories': TopStory.objects.filter(show_on_home_page=True)
		}
		return context

class LoginView(FormView):
	form_class = LoginForm
	template_name = 'login.html'
	success_url = settings.LOGIN_REDIRECT_URL
		
	def form_valid(self,form):
		redirect_to = settings.LOGIN_REDIRECT_URL
        	login(self.request, form.get_user())
        	if self.request.session.test_cookie_worked():
           		self.request.session.delete_test_cookie()
        	return HttpResponseRedirect(redirect_to) 
	
	def form_invalid(self,form):	
		return super(Login, self).form_invalid(form)
	@method_decorator(sensitive_post_parameters())	
	def dispatch(self, *args, **kwargs):
		if self.request.user.is_active:
			return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
		return super(Login,self).dispatch(*args, **kwargs)
	def get_context_data(self, **kwargs):
			context = super(Login,self).get_context_data(**kwargs)
			context['form']=self.form_class
			return context
		

class MediaRoom(TemplateView):
	template_name = templates['site']['mediaroom']['home']
	def get_context_data(self, **kwargs):
		context = super(MediaRoom,self).get_context_data(**kwargs)
		context = dict()
		context['base']=templates['base']['root']
		context['mast'] = templates['build']['mast']
		context['MAST_TEXT']="Media"
		return context

class NewsRoom(TemplateView):	
	template_name = templates['site']['news']['home']
	
	def get_context_data(self, *args, **kwargs):
		context = super(NewsRoom,self).get_context_data(*args,**kwargs)
		context['base']=templates['base']['root']
		context['templates_news']=templates['site']['news']['news']
		context['templates_notices']=templates['site']['news']['notices']
		context['templates_tenders']=templates['site']['news']['tenders']
		context['templates_archives']=templates['site']['news']['archives']
		all_news = News.objects.all().order_by('-date') #latest news first
		paginator = Paginator(all_news, values.get('NEWS_PAGINATION_MAX_ENTRIES'))
		page = self.request.GET.get('page')
		context['mast'] = templates['build']['mast']
		context['MAST_TEXT']="News & Notices"	
		try:
			page=int(page)
		except TypeError:
			page=1	
		 
		context['pagebuttons'] = getPageButtons(paginator.num_pages, page, values.get('NEWS_PAGINATION_MAX_ENTRIES'))
		
		try:
        		page_news = paginator.page(page)
        		prev = page - 1
        		nex = page + 1
    		except PageNotAnInteger:
        		page_news = paginator.page(1)
        		prev = 1
        		nex = 2
    		except EmptyPage:
        		page_news = paginator.page(paginator.num_pages)
        		prev= num_pages - 1
        		nex = num_pages
        	context['page_news']=page_news
        	context['has_previous']=page_news.has_previous()
        	context['has_next']=page_news.has_next()
        	context['prev']=prev
        	context['next']=nex
        	context['title']="News & Notices"
		return context

class Parents(FormView):
	template_name = templates['site']['parents']['home']
	form_class = LoginForm
	def get_context_data(self, *args, **kwargs):
		context = super(Parents,self).get_context_data(*args,**kwargs)
		context['base']=templates['base']['root']
		context['mast'] = templates['build']['mast']
		context['MAST_TEXT']="Parents"
		context['form']=LoginForm
		return context
class Staff(TemplateView):
	template_name = templates['site']['staff']['home']
	def get_context_data(self, *args, **kwargs):
		context = super(Staff,self).get_context_data(*args,**kwargs)
		staff_list = getAllStaff()
		context['base']=templates['base']['root']
		context['mast']=templates['build']['mast']
		context['MAST_TEXT']= "Staff"
		context['staff_list'] = staff_list
	
		return context
class Students(TemplateView):
	template_name = templates['site']['students']['home']
	def get_context_data(self, *args, **kwargs):
		context = super(Students,self).get_context_data(*args,**kwargs)
		context['base']=templates['base']['root']
		context['mast'] = templates['build']['mast']
		context['MAST_TEXT']="Students"
		return context
		
class Research(TemplateView):
	template_name=templates['site']['research']['home']
	def get_context_data(self, **kwargs):
		context = super(Research,self).get_context_data(**kwargs)
		context = dict()
		context['title']=strings['research_title']
		context['base'] = templates['base']['root']
		context['research_areas'] = templates['site']['research']['areas']
		context['research_centres'] = templates['site']['research']['centres']
		context['research_portfolio'] = templates['site']['research']['portfolio']
		context['research_publications'] = templates['site']['research']['publications']
		context['research_scholars'] = templates['site']['research']['scholars']
		context['centres'] = getAllResearchCentres()
		context['areas'] = getAllResearchAreas()
		context['mast'] = templates['build']['mast']
		context['MAST_TEXT']="Research"	
		#context['publications'] = getAllPublications()
		#context['portfolio'] = getPortfolio()
		context['scholars'] = getListOfScholars()

		return context
class ResearchAreaProfile(TemplateView):
	template_name = templates['site']['research']['area_profile']
	def get_context_data(self, **kwargs):
		context = super(ResearchAreaProfile,self).get_context_data(**kwargs)
		context = dict()
		context['base'] = templates['base']['root']
		context['mast'] = templates['build']['mast']
		
		return context
class ResearchCentreProfile(TemplateView):
	template_name = templates['site']['research']['centre_profile']
	def get_context_data(self, **kwargs):
		context = super(ResearchCentreProfile,self).get_context_data(**kwargs)
		context = dict()
		context['base'] = templates['base']['root']
		return context

class StudentProfile(TemplateView): 		
	template_name=''
	def get_context_data(self, **kwargs):
		context = super(StudentProfile,self).get_context_data(**kwargs)
		context = dict()
		context['base'] = templates['base']['root']
		return context
	


