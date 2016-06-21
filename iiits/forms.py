from django.forms import ModelForm, TextInput, Textarea, PasswordInput, CharField
from django.contrib.auth.forms import AuthenticationForm 
from iiits.models import *

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
class AddPublicationForm(ModelForm):
	class Meta:
		model = Publication
		exclude = ('authors',)
		widgets = {
				'title':TextInput(attrs={'class':'form-control',
										 'placeholder':'Title of the publication'
								}),

		}					

class LoginForm(AuthenticationForm):
	username = CharField()
	password = CharField()
	class Meta:
		widgets={
			'username':TextInput(attrs={
			'class':'form-control',
			'id':'username',
			'placeholder':'Enter your username or email'
			}),
			'password':PasswordInput(attrs={
			'class':'form-control',
			'id':'password',
			'placeholder':'Enter your password'
			})
		}	