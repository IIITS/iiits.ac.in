from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView, View
from django.conf import settings
from iiits.models import *
from iiits.methods import *
from iiits.algorithms import *

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

class FacultyProfileView(TemplateView):
	template_name = 'iiits/faculty/faculty_profile.html'
	def get_context_data(self, **kwargs):
		context = super(FacultyProfileView,self).get_context_data(**kwargs)
		context = dict()
		dept=self.request.GET.get('dept')
		dept =ifNone(dept,'all')
		title=self.request.GET.get('title')
		title = ifNone(title,'all')
		ra=self.request.GET.get('ra')
		ra = ifNone(ra, 'all')
		vs=self.request.GET.get('vs')
		vs = ifNone(vs,'true')
		instfac = self.request.GET.get('instfac')
		instfac = ifNone(instfac,'true')
		
		fac = FacultySearch(dept=dept,title=title,ra=ra,vs=vs,instfac=instfac)
		faculty=fac.search()
		context['faculty'] = faculty
		return context		

