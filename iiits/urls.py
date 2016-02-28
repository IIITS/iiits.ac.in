from django.conf.urls import url,include
from django.contrib import admin
from iiits.views import *
urlpatterns = [
    url(r'^$', 								HomeView.as_view(), name='home'),
    url(r'^faculty/$', 	                    FacultyView.as_view(), name='faculty'),
    url(r'^faculty/(~*)([a-z-._A-Z]*)$',	FacultyPageView.as_view(),	name='facultyprofile'),

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
