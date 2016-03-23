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
	def get_context_data(self, **kwargs):
		context = super(About,self).get_context_data(**kwargs)
		context = dict()
		return context

class Academics(TemplateView):
	template_name=''
	def get_context_data(self, *args, **kwargs):
		context = super(Academics, self).get_context_data(*args, **kwargs)
		return context

class Admissions(TemplateView):
	template_name =  templates['site']['admissions']['home']
	def get_context_data(self, *args, **kwargs):
		context = super(Admissions,self).get_context_data(*args,**kwargs)
		context['admissions_base'] = templates['base']['admissions']
		context['admissions_undergraduate'] = templates['site']['admissions']['undergraduate']
		context['admissions_postgraduate'] = templates['site']['admissions']['postgraduate']
		return context

class Alumni(TemplateView):		
	template_name = ''
	def get_context_data(self, **kwargs):
		context = super(Alumni,self).get_context_data(**kwargs)
		context = dict()
		return context

class CampusLife(TemplateView):
	template_name = ''
	def get_context_data(self, **kwargs):
		context = super(CampusLife,self).get_context_data(**kwargs)
		context = dict()
		return context

class Faculty(TemplateView):
	template_name = 'iiits/faculty/faculty_home.html'
	def get_context_data(self, **kwargs):
		context = super(Faculty,self).get_context_data(**kwargs)
		context = dict()
		return context

class FacultyPage(TemplateView):
	template_name = 'iiits/faculty/faculty_page.html'
	def get_context_data(self, **kwargs):
		context = super(FacultyPage,self).get_context_data(**kwargs)
		context = dict()
		try:
			dept=self.request.GET.get('dept')
		except ObjectDoesNotExist:	
			dept = 'all'
		try:	
			title=self.request.GET.get('title')
		except ObjectDoesNotExist:
			title='all'
		try:		
			ra=self.request.GET.get('ra')
		except ObjectDoesNotExist:
			ra='all'
		try:		
			vs=self.request.GET.get('vs')
		except ObjectDoesNotExist:
			vs = 'false'	
		try	:
			instfac = self.request.GET.get('instfac')
		except ObjectDoesNotExist:	
			instfac = 'true'

		return context

class FacultyProfile(TemplateView):
	template_name='iiits/faculty/faculty_profile.html'
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
		return context


class Home(TemplateView):
	template_name = 'iiits/index.html'
	
	def get_context_data(self, **kwargs):
		
		context = super(Home,self).get_context_data(**kwargs)
		context = {

		}
		
		return context

class MediaRoom(TemplateView):
	template_name=''
	def get_context_data(self, **kwargs):
		context = super(MediaRoom,self).get_context_data(**kwargs)
		context = dict()

		return context

class NewsRoom(TemplateView):	
	template_name = 'iiits/news/list.html'
	model = News
	def get_context_data(self, *args, **kwargs):
		context = super(NewsRoom,self).get_context_data(*args,**kwargs)
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



class Research(TemplateView):
	template_name=''
	def get_context_data(self, **kwargs):
		context = super(Research,self).get_context_data(**kwargs)
		context = dict()

		return context

class Staff(TemplateView):
	template_name=''
	def get_context_data(self, **kwargs):
		context = super(Staff,self).get_context_data(**kwargs)
		context = dict()

		return context

class Students(TemplateView):
	template_name=''
	def get_context_data(self, **kwargs):
		context = super(Students,self).get_context_data(**kwargs)
		context = dict()

		return context

class StudentProfile(TemplateView): 		
	template_name=''
	def get_context_data(self, **kwargs):
		context = super(StudentProfile,self).get_context_data(**kwargs)
		context = dict()

		return context
	


