from django.contrib import admin
from iiits.models import *



admin.site.register(AcademicsProgramme)
admin.site.register(AcademicsResources)
admin.site.register(AcademicsTimeTable)
admin.site.register(AdmissionsFeeModeofPayment)
admin.site.register(AdmissionsFeeStructure)
admin.site.register(AdmissionsFinancialAssistance)
admin.site.register(CampusLifeEntity)
admin.site.register(CampusLifeSubEntity)
admin.site.register(CareerType)	
admin.site.register(CareerFacultyPosition)
admin.site.register(CareerNonFacultyPosition)
admin.site.register(ConsultancyContract)
admin.site.register(ContactAddress)
admin.site.register(Config)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(FacultyTitle)
admin.site.register(ImageSlider)
admin.site.register(Institute)
admin.site.register(News)
admin.site.register(NewsStory)
admin.site.register(Notes)
admin.site.register(Notice)
admin.site.register(Publication)
admin.site.register(ResearchArea)
admin.site.register(ResearchCentre)
admin.site.register(ResearchCentreProfile)
admin.site.register(ResearchPortfolio)
admin.site.register(ResearchStudent)
admin.site.register(Tender)
admin.site.register(TenderType)
admin.site.register(TopStory)
admin.site.register(Staff)
admin.site.register(StaffDesignation)
admin.site.register(StaticImages)
admin.site.register(VisitingFaculty)

admin.AdminSite.site_header = "IIITS web administration"
admin.AdminSite.site_title = "Developed by Sahal Sajjad"
admin.AdminSite.index_title = "Developed by Sahal Sajjad"
