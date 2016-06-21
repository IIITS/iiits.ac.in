from django.conf import settings
from django.conf.urls import url,include, patterns
from django.contrib import admin
from iiits import views, create, delete, update, config
urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^faculty/$', views.FacultyPage.as_view(), name='facultypage'),
    url(r'^faculty/(~*)([a-z-._A-Z]*)$', views.FacultyProfile.as_view(),	name='facultyprofile'),
    url(r'^newsroom/$', views.NewsRoom.as_view(), name='newsroom'),
    url(r'^addnews/$', 	create.AddNews.as_view()	,   name='addnews'),
    url(r'^admissions/$', views.Admissions.as_view(), name='admissions'),
    url(r'^academics/$',  views.Academics.as_view(),  name='academics'),
    url(r'^research/$',   views.Research.as_view(),   name='research'),
    url(r'^research/centres/([a-zA-Z-]*)/$',      views.ResearchCentreProfile.as_view(), name='research-profile'),
    url(r'^research/areas/([a-zA-Z-]*)/$',      views.ResearchAreaProfile.as_view(), name='research-area'),
    url(r'^about/$',  views.About.as_view(), name="about"),
    url(r'^parents/$', views.Parents.as_view(), name="parents"),
    url(r'^students/(~*)([a-z-._A-Z]*)$',	views.Students.as_view(),	name='students'),
    url(r'^staff/(~*)([a-z-._A-Z]*)$',		views.Staff.as_view(),	name='staff'),
    url(r'^alumni/(~*)([a-z-._A-Z]*)$',	views.Alumni.as_view(),	name='alumni'),
    url(r'^mediaroom/(?P<path>.*)$',			views.MediaRoom.as_view(),	name='media'),
    url(r'^campuslife/$', views.CampusLife.as_view(), name='campuslife'),
    url(r'^careers/$', views.Career.as_view(), name='career'),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    #url(r'^/cms/$', views.CMSHome.as_view(), name='cmshome')	
]

if settings.SERVE_MEDIA:
	urlpatterns += (
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT})
)
