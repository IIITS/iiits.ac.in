from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView, View
from django.conf import settings
from iiits.models import *
from iiits.methods import *
from iiits.algorithms import *

FAC_ENTRIES_PER_PAGE = 10
class HomeView(TemplateView):
	template_name = 'iiits/index.html'
	
	def get_context_data(self, **kwargs):
		
		context = super(HomeView,self).get_context_data(**kwargs)
		context = {

		}
		
		return context

class FacultyView(TemplateView):
	template_name = 'iiits/faculty/faculty_home.html'
	def get_context_data(self, **kwargs):
		context = super(FacultyView,self).get_context_data(**kwargs)
		context = dict()

		return context		

class FacultyPageView(TemplateView):
	template_name = 'iiits/faculty/faculty_page.html'
	def get_context_data(self, **kwargs):
		context = super(FacultyPageView,self).get_context_data(**kwargs)
		context = dict()
		
		dept=self.request.GET.get('dept')
		title=self.request.GET.get('title')
		ra=self.request.GET.get('ra')
		vs=self.request.GET.get('vs')
		instfac = self.request.GET.get('instfac')
		
		fac = FacultySearch(dept=dept,title=title,ra=ra,vs=vs,instfac=instfac)
		faculty=fac.search()
		paginate = PaginationAlgorithm(FAC_ENTRIES_PER_PAGE)
		fac_list = paginate.divide(faculty,len(faculty))

		context['faculty'] = faculty
		return context

class FacultyProfileView(TemplateView):
	template_name='iiits/faculty/faculty_profile.html'
	def get_context_data(self, **kwargs):
		context = super(FacultyProfileView,self).get_context_data(**kwargs)	
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

