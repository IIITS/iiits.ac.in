def getFacultyByDept(request,dept):
	result=dict()
	result['faculty']=Faculty.objects.filter(department__code=dept).order_by('user__first_name')
	result['instfac']='true'
	result['vsfac']='false'
	return JsonResponse(result,safe=False)
def getFacultyByRA(request,raid):
	result=dict()
	result['faculty']=Faculty.objects.filter(research_areas__contains=raid).order_by('user__first_name')
	result['instfac']='true'
	result['vsfac']='false'
	return JsonResponse(result,safe=False)
def getFacultyByTitle(request,title):
	result=dict()
	result['faculty']=Faculty.objects.filter(title=title).order_by('user__first_name')
	result['instfac']='true'
	result['vsfac']='false'
	return JsonResponse(result,safe=False)
def getAllFaculty(request):
	result=dict()
	result['faculty']=Faculty.objects.all().order_by('user__first_name')
	result['vsfaculty']=VisitingFaculty.objects.all().order_by('user__first_name')
	result['vs']
	result['instfac']='true'
	result['vsfac']='true'
	return JsonResponse(result,safe=False)
def getInstituteFaculty(request):
	result=dict()
	result['faculty']=Faculty.objects.all().order_by('user__first_name')
	result['instfac']='true'
	result['vsfac']='false'
	return JsonResponse(result,safe=False)
def getVisitingFaculty(request):	
	result=dict()
	result['vsfaculty']=VisitingFaculty.objects.all().order_by('user__first_name')
	result['instfac']='false'
	result['vsfac']='true'
	return JsonResponse(result,safe=False)
