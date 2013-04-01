from django.http import HttpResponse

def index(request):
	return HttpResponse("Moikka")

def project(request, project_id):
	return HttpResponse("You are looking at project %s." % project_id)
	
def task(request, task_id):
	return HttpResponse("You are looking at task %s." % task_id)

def reference(request, reference_id):
	return HttpResponse("You are looking at reference %s." % reference_id)
	
