from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, logout, authenticate
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
import json

class About(TemplateView):
	template_name = templates['site']['about']['home']
	def get_context_data(self, **kwargs):
		context = super(About,self).get_context_data(**kwargs)
		context['user_active']=False
		if self.request.user.is_active:
			context['user_active']=True
			context['user']=self.request.user
		
		context['base'] = templates['base']['root']
		context['mast'] = templates['build']['mast']
		context['MAST_TEXT']="About"
		context['template_bog'] =templates['site']['about']['bog']
		context['template_about_iiit'] =templates['site']['about']['about_iiit']
		context['template_about_sricity'] =templates['site']['about']['about_sricity']
		context['template_location'] =templates['site']['about']['location']
		context['template_reaching_iiit'] =templates['site']['about']['reaching_iiit']
		context['template_contact_us'] =templates['site']['about']['contact_us']
		try:
			context['si_location_iiit_map'] = StaticImages.objects.get(identifier='location_iiit_map')
		except ObjectDoesNotExist:
			donothing=True
		context['contact_us']= ContactAddress.objects.all()
		try:
			context['admissions_help_desk']=Config.objects.get(property_name='admissions_help_desk')	
		except ObjectDoesNotExist:
			context['admissions_help_desk']= "Not Available at the moment."
		return context

class Academics(TemplateView):
	template_name=templates['site']['academics']['home']
	def get_context_data(self, *args, **kwargs):
		context = super(Academics, self).get_context_data(*args, **kwargs)
		context['user_active']=False
		if self.request.user.is_active:
			context['user_active']=True
			context['user']=self.request.user
		
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
		context['user_active']=False
		if self.request.user.is_active:
			context['user_active']=True
			context['user']=self.request.user
		
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
		context['user_active']=False
		if self.request.user.is_active:
			context['user_active']=True
			context['user']=self.request.user
		
		
		context['base'] = templates['base']['root']
		context['alumni_list']= templates['site']['alumni']['list']
		context['mast'] = templates['build']['mast']
		context['MAST_TEXT']="Alumni"
		return context

class CampusLife(TemplateView):
	template_name = templates['site']['campus_life']['home']
	def get_context_data(self, **kwargs):
		context = super(CampusLife,self).get_context_data(**kwargs)
		context['user_active']=False
		if self.request.user.is_active:
			context['user_active']=True
			context['user']=self.request.user
		context['base'] = templates['base']['root']
		context['mast'] = templates['build']['mast']
		context['MAST_TEXT']="Campus Life"
		context['templates_facilities'] = templates['site']['campus_life']['facilities']
		context['templates_events'] = templates['site']['campus_life']['events']
		context['templates_student_life'] = templates['site']['campus_life']['student_life']
		context['campus_life_entities'] = CampusLifeEntity.objects.order_by('rank','name')
		context['cl_sub']=beautifyCLSE(CampusLifeSubEntity.objects.order_by('belongs_to__code'))
		return context
class Career(TemplateView):
	template_name = templates['site']['career']['home']
	def get_context_data(self, **kwargs):
		context = super(Career,self).get_context_data(**kwargs)
		context['user_active']=False
		if self.request.user.is_active:
			context['user_active']=True
			context['user']=self.request.user

		context['base'] = templates['base']['root']
		context['mast'] = templates['build']['mast']
		context['templates_fac'] = templates['site']['career']['fac']
		context['templates_other'] = templates['site']['career']['other']
		context['templates_consultancy'] = templates['site']['career']['consultancy']
		context['MAST_TEXT']="Careers"
		context['fac'] = 	    CareerFacultyPosition.objects.filter(is_expired=False).order_by('-datetime')
		context['non_fac'] = CareerNonFacultyPosition.objects.filter(is_expired=False).order_by('-datetime')
		context['consultancy'] =  ConsultancyContract.objects.filter(is_expired=False).order_by('-datetime')
		context['data']={'staff':"Hi"}
		return context

class FacultyPage(TemplateView):
	template_name = templates['site']['faculty']['home']
	def get_context_data(self, **kwargs):
		context = super(FacultyPage,self).get_context_data(**kwargs)
		context['user_active']=False
		if self.request.user.is_active:
			context['user_active']=True
			context['user']=self.request.user
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
		context['user_active']=False
		if self.request.user.is_active:
			context['user_active']=True
			context['user']=self.request.user
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
		context['user_active']=False
		if self.request.user.is_active:
			context['user_active']=True
			context['user']=self.request.user
		image_slider = ImageSlider.objects.order_by('order_no')
		context = {
			'image_slider_no':[x for x in range(1,len(image_slider)+1,1)],
			'image_slider_images':image_slider,
			'topstories': TopStory.objects.filter(show_on_home_page=True),
			
		}
		try:
			context['headlines']=News.objects.order_by('-date')[0:5]
		except IndexError as error:
			news =  News.objects.order_by('-date')
			context['headlines']=news[0:news.length]	
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
			context['user_active']=False
			if self.request.user.is_active:
				context['user_active']=True
				context['user']=self.request.user
			context = super(Login,self).get_context_data(**kwargs)
			context['form']=self.form_class
			return context
		

class MediaRoom(TemplateView):
	template_name = templates['site']['mediaroom']['home']
	def get_context_data(self, **kwargs):
		context = super(MediaRoom,self).get_context_data(**kwargs)
		context['user_active']=False
		if self.request.user.is_active:
			context['user_active']=True
			context['user']=self.request.user
		
		context['base']=templates['base']['root']
		context['mast'] = templates['build']['mast']
		context['media_topstories'] = templates['site']['mediaroom']['topstories']
		context['media_newsletter'] = templates['site']['mediaroom']['newsletter']
		context['media_gallery'] = templates['site']['mediaroom']['gallery']
		context['MAST_TEXT']="Media"
		topstories = TopStory.objects.order_by('-date')
		context['topstories'] = topstories
		return context
class TopStoryProfile(TemplateView):
	template_name = templates['site']['mediaroom']['topstory-profile']		
	def get_context_data(self, **kwargs):
		context = super(TopStoryProfile,self).get_context_data(**kwargs)
		return context
class NewsRoom(TemplateView):	
	template_name = templates['site']['news']['home']
	
	def get_context_data(self, *args, **kwargs):
		context = super(NewsRoom,self).get_context_data(*args,**kwargs)
		context['user_active']=False
		if self.request.user.is_active:
			context['user_active']=True
			context['user']=self.request.user
		context['base']=templates['base']['root']
		context['templates_news']=templates['site']['news']['news']
		context['templates_notices']=templates['site']['news']['notices']
		context['templates_tenders']=templates['site']['news']['tenders']
		context['templates_archives']=templates['site']['news']['archives']
		all_news = News.objects.all().order_by('-date') #latest news first
		all_news_stories = NewsStory.objects.order_by('-date')
		all_notices = Notice.objects.order_by('-valid_until')
		tender_const = Tender.objects.filter(tender_type=TenderType.objects.get(name='construction'))
		tender_other = Tender.objects.filter(tender_type=TenderType.objects.get(name='other'))
		news_paginator = Paginator(all_news_stories, values.get('NEWS_PAGINATION_MAX_ENTRIES'))
		notices_paginator = Paginator(all_notices, values.get('NEWS_PAGINATION_MAX_ENTRIES'))
		tender_const_paginator = Paginator(tender_const, values.get('NEWS_PAGINATION_MAX_ENTRIES'))
		tender_other_paginator = Paginator(tender_other, values.get('NEWS_PAGINATION_MAX_ENTRIES'))
		page = self.request.GET.get('page')
		context['mast'] = templates['build']['mast']
		context['MAST_TEXT']="News & Notices"	
		try:
			page=int(page)
		except TypeError:
			page=1
		try:
        		page_news = news_paginator.page(page)
        		page_notice = notices_paginator.page(page)
        		tend_other  = tender_other_paginator.page(page)
        		tend_const = tender_const_paginator.page(page)
        		prev = page - 1
        		nex = page + 1
    		except PageNotAnInteger:
        		page_news = news_paginator.page(1)
        		page_notice= notices_paginator.page(1)
        		tend_other  = tender_other_paginator(1)
        		tend_const = tender_const_paginator(1)
        		prev = 1
        		nex = 2
    		except EmptyPage:
        		page_news = news_paginator.page(news_paginator.num_pages)
        		page_notices = notices_paginator.page(notices_paginator.num_pages)
        		tend_other  = tender_other_paginator.page(tender_other_paginator.num_pages)
        		tend_const = tender_const_paginator.page(tender_const_paginator.num_pages)
        		prev= num_pages - 1
        		nex = num_pages
        	context['news_stories']=page_news
        	context['has_previous']=page_news.has_previous()
        	context['has_next']=page_news.has_next()
        	context['notices'] = page_notice
        	context['tender_construction']=tend_const
        	context['tender_other']= tend_other
        	context['prev']=prev
        	context['next']=nex
        	context['title']="News & Notices"
		return context

class Parents(FormView):
	template_name = templates['site']['parents']['home']
	form_class = LoginForm
	def get_context_data(self, *args, **kwargs):
		context = super(Parents,self).get_context_data(*args,**kwargs)
		context['user_active']=False
		if self.request.user.is_active:
			context['user_active']=True
			context['user']=self.request.user
		context['base']=templates['base']['root']
		context['mast'] = templates['build']['mast']
		context['MAST_TEXT']="Parents"
		context['form']=LoginForm
		return context
class Staff(TemplateView):
	template_name = templates['site']['staff']['home']
	def get_context_data(self, *args, **kwargs):
		context = super(Staff,self).get_context_data(*args,**kwargs)
		context['user_active']=False
		if self.request.user.is_active:
			context['user_active']=True
			context['user']=self.request.user
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
		context['user_active']=False
		if self.request.user.is_active:
			context['user_active']=True
			context['user']=self.request.user
		context['base']=templates['base']['root']
		context['mast'] = templates['build']['mast']
		context['MAST_TEXT']="Students"
		return context
		
class Research(TemplateView):
	template_name=templates['site']['research']['home']
	def get_context_data(self, **kwargs):
		context = super(Research,self).get_context_data(**kwargs)
		context['user_active']=False
		if self.request.user.is_active:
			context['user_active']=True
			context['user']=self.request.user
		context['title']=strings['research_title']
		context['base'] = templates['base']['root']
		context['research_areas'] = templates['site']['research']['areas']
		context['research_centres'] = templates['site']['research']['centres']
		context['research_portfolio'] = templates['site']['research']['portfolio']
		context['research_publications'] = templates['site']['research']['publications']
		context['research_scholars'] = templates['site']['research']['scholars']
		context['centres'] = getAllResearchCentres()
		context['areas'] = getAllResearchAreas()
		publications = getPublications()
		page = self.request.GET.get('page')
		try:
			page=int(page)
		except TypeError:
			page=1	
		paginator = Paginator(publications, values.get('NEWS_PAGINATION_MAX_ENTRIES'))
		try:
        		pub = paginator.page(page)
        		pub_prev = page - 1
        		pub_nex = page + 1
    		except PageNotAnInteger:
        		pub = paginator.page(1)
        		pub_prev = 1
        		pub_nex = 2
    		except EmptyPage:
        		pub = paginator.page(paginator.num_pages)
        		pub_prev= num_pages - 1
        		pub_nex = num_pages
 	        context['pub']=pub		
 	        context['pub_has_previous']=pub.has_previous()
 	        context['pub_has_next']=pub.has_next()
 	        context['pub_prev']=pub_prev
 	        context['pub_next']=pub_nex		
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
		context['user_active']=False
		if self.request.user.is_active:
			context['user_active']=True
			context['user']=self.request.user
		context['base'] = templates['base']['root']
		context['mast'] = templates['build']['mast']
		
		return context
class ResearchCentreProfile(TemplateView):
	template_name = templates['site']['research']['centre_profile']
	def get_context_data(self, **kwargs):
		context = super(ResearchCentreProfile,self).get_context_data(**kwargs)
		context['user_active']=False
		if self.request.user.is_active:
			context['user_active']=True
			context['user']=self.request.user
		context['base'] = templates['base']['root']
		return context

class StudentProfile(TemplateView): 		
	template_name=''
	def get_context_data(self, **kwargs):
		context = super(StudentProfile,self).get_context_data(**kwargs)
		context['user_active']=False
		if self.request.user.is_active:
			context['user_active']=True
			context['user']=self.request.user
		context['base'] = templates['base']['root']
		return context
	
def staff_list(request):
	staff = getAllStaff()
	result=list()
	for x in staff:
		result.append({
				"name":x.user.get_full_name(),
				"position":str(x.designation),
				"image_url":x.photo.url
			})
	return JsonResponse(json.dumps(result),safe=False)	

def get_cl_codes(request):
	results = list()
	cle = CampusLifeEntity.objects.order_by('rank','name')
	for c in cle:
		results.append(str(c.code))
	return JsonResponse(json.dumps(results), safe=False)	
def login_view(request):
	username= request.POST['username']
	password= request.POST['password']
	user = authenticate(username=username, password=password)
	redirect_to = settings.LOGIN_REDIRECT_URL
	if user is not None:
		if user.is_active:
			login(request,user)
		else:
			return JsonResponse({"code":300,"message":"Email or Password incorrect!"})
	else:		
		return JsonResponse({"code":300,"message":"Email or Password incorrect!"})
    	return HttpResponseRedirect('/')
def write_to_us(request):
   	name = request.POST['name']
   	email = request.POST['email']
   	phone = request.POST['phone']
   	query = request.POST['query']
   	return HttpResponse({"message":"success"})