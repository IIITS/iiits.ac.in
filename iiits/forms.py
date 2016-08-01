from django.forms import Form, ModelForm, TextInput, Textarea, PasswordInput, CharField, Select
from django.contrib.auth.forms import AuthenticationForm 
from iiits.models import *
from django.contrib.auth.models import Group
from django.db.models import Q
from iiits.methods import get_iterable_users
from django import forms

class SetPasswordForm(forms.Form):
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    new_password1 = forms.CharField(label=("New password"),
                                    widget=forms.PasswordInput(
                                    	attrs={'class':'form-control'}
                                    	))
    new_password2 = forms.CharField(label=("New password confirmation"),
                                    widget=forms.PasswordInput(
                                    	attrs={'class':'form-control'}
                                    	))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


class PasswordChangeForm(SetPasswordForm):
    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect': ("Your old password was entered incorrectly. "
                                "Please enter it again."),
    })
    old_password = forms.CharField(label=("Old password"),
                                   widget=forms.PasswordInput(
                                    	attrs={'class':'form-control'}
                                    	))

    field_order = ['old_password', 'new_password1', 'new_password2']

    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password


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
		fields = ['title','description','link','keywords','authors','fileupload','year']
		widgets = {
				'title':TextInput(attrs={'class':'form-control',
										 'placeholder':'Title of the publication'
								}),
				'description':Textarea(attrs={'class':'form-control',
										 'placeholder':'Description of the publication'
								}),
				'link':TextInput(attrs={'class':'form-control',
										 'placeholder':'Please provide a link (if any)'
								}),
				'keywords':Textarea(attrs={'class':'form-control',
										 'placeholder':'keywords'
								}),
				'authors':Select(choices=get_iterable_users(Group.objects.get(name='Faculty@IIITS').user_set.get_queryset()))


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