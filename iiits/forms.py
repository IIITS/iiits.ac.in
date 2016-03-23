from django.forms import ModelForm, Form, Textarea, TextInput
from iiits.models import News, Notice
class AddNewsForm(ModelForm):
	class Meta:
		model = News
		fields = '__all__'
		widgets = {
			'title':TextInput(attrs={'class':'form-control',
						  'placeholder':'What\'s the title of the news?', 							  'label':'News Headline', 							
						}),
			'content':Textarea(attrs={'class':'form-control',
						  'placeholder':'What\'s the news about? Desciption / content of the news.', 							  'label':'Description/ Content'	
						})
					
		}
class AddNoticeForm(ModelForm):
	class Meta:
		model = Notice 
		fields = '__all__'
		widgets = {
				'title':TextInput(attrs={'class':'form-control',
				'placeholder':'Title of the notice'	
					})
					}
