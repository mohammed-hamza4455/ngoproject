from django.http import JsonResponse
from .models import Project

def project_list(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)
