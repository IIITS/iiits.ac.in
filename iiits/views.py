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

FAC_ENTRIES_PER_PAGE = 10
NEWS_ENTRIES_PER_PAGE = 5
class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response

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



class NewsRoomView(TemplateView):	
	template_name = 'iiits/news/list.html'
	model = News
	def get_context_data(self, *args, **kwargs):
		context = super(NewsRoomView,self).get_context_data(*args,**kwargs)
		all_news = News.objects.all().order_by('-date') #latest news first
		paginator = Paginator(all_news, NEWS_ENTRIES_PER_PAGE)
		page = self.request.GET.get('page')
		try:
			page=int(page)
		except TypeError:
			page=1	
		 
		context['pagebuttons'] = getPageButtons(paginator.num_pages, page, NEWS_ENTRIES_PER_PAGE)
		
		try:
        		page_news = paginator.page(page)
    		except PageNotAnInteger:
        		page_news = paginator.page(1)
    		except EmptyPage:
        		page_news = paginator.page(paginator.num_pages)
        	context['page_news']=page_news

		return context

class AdmissionView(TemplateView):
	template_name = '' 
	def get_context_data(self, *args, **kwargs):
		context = super(AdmissionView,self).get_context_data(*args,**kwargs)
		return context

	


