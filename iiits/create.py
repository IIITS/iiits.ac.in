from iiits.config import templates, urls

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