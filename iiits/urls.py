from django.conf import settings
from django.conf.urls import url,include, patterns
from django.contrib import admin
from iiits import views, create, delete, update, config
urlpatterns = [
    url(r'^$', 								views.Home.as_view(), name='home'),
    url(r'^faculty/$',                 views.FacultyPage.as_view(), name='facultypage'),
    url(r'^faculty/(~*)([a-z-._A-Z]*)$',	views.FacultyProfile.as_view(),	name='facultyprofile'),
    url(r'^newsroom/$', 					views.NewsRoom.as_view(), name='newsroom'),
    url(r'^addnews/$', 						create.AddNews.as_view()	,   name='addnews'),
    url(r'^admissions/$',                   views.Admissions.as_view(), name='admissions'),
    url(r'^academics/$',                    views.Academics.as_view(),  name='academics'),
    url(r'^research/$',                     views.Research.as_view(),   name='research'),
    #url(r'^students/(~*)([a-z-._A-Z]*)$',	StudentsView.as_view(),	name='students'),
    #url(r'^staff/(~*)([a-z-._A-Z]*)$',		StaffView.as_view(),	name='staff'),
    #url(r'^alumni/(~*)([a-z-._A-Z]*)$',	AlumniView.as_view(),	name='alumni'),
    #url(r'^mediaroom/(?P<path>.*)$',			MediaView.as_view(),	name='media'),	
]

if settings.SERVE_MEDIA:
	urlpatterns += (
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT})
)
