from django.views.generic.edit import UpdateView
from iiits.config import templates
from iiits.models import *
class ChangeFeeStructure(UpdateView):
	model = AdmissionsFeeStructure
	template_name = templates.get('change_fee_structure')
'''
class ChangeUGAdmissions(UpdateView):
	model = AdmissionsUGAdmissions
	template_name = templates.get('change_ug_admissions')

class ChangePGAdmissions(UpdateView):
	model = AdmissionsPGAdmissions
	template_name = templates.get('change_pg_admissions')

class ChangeMSAdmissions(UpdateView):
	model = AdmissionsMSAdmissions
	template_name = templates.get('change_ms_admisssions')

class ChangeMTechAdmissions(UpdateView):
	model = AdmissionsMTechAdmissions
	template_name = templates.get('change_mtech_admissions')	

class ChangePHDAdmissions(UpdateView):
	model = AdmissionsPHDAdmissions
	template_name = templates.get('change_phd_admissions')	
'''	