from django.contrib import admin
from iiits.models import *


admin.site.register(Faculty)
admin.site.register(FacultyTitle)
admin.site.register(VisitingFaculty)
admin.site.register(Department)
admin.site.register(AcademicsResources)
admin.site.register(AcademicsTimeTable)
admin.site.register(AcademicsProgramme)
admin.site.register(AdmissionsFeeStructure)
admin.site.register(AdmissionsFinancialAssistance)
admin.site.register(AdmissionsFeeModeofPayment)
admin.site.register(Course)
admin.site.register(Notes)
admin.site.register(Publications)
admin.site.register(ResearchStudent)
admin.site.register(ResearchPortfolio)
admin.site.register(ResearchCentre)
admin.site.register(ResearchArea)
admin.site.register(Notice)
admin.site.register(News)

admin.AdminSite.site_header = "IIITS web administration"
admin.AdminSite.site_title = "Developed by Sahal Sajjad"
admin.AdminSite.index_title = "Developed by Sahal Sajjad"