from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from iiits.config import templates, urls
from iiits.mixins import AjaxableResponseMixin
from iiits.models import *
from iiits.forms import *

# Notice Board
class AddNotice(AjaxableResponseMixin, CreateView):
	model=Notice
	form_class=AddNoticeForm
	template_name=templates['cms']['notice']['add_notice']
	success_url=urls['cms']['notice']['add_success']
# News Room
class AddNews(AjaxableResponseMixin ,CreateView):
	model=News
	form_class=AddNewsForm
	template_name=templates['cms']['news']['add_news']
	success_url= urls['cms']['news']['add_success']

class AddPublication(AjaxableResponseMixin, CreateView):
	model = Publication
	form_class = AddPublicationForm
	template_name = templates['cms']['publications']['add_publication']
	success_url = urls['cms']['publications']['add_success']

def addStarPublication(request):
	return HttpResponse("Hi")		

def successPublication(request):
	return HttpResponseRedirect('/faculty/')	