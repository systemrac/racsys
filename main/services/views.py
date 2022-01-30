from django.shortcuts import render
from django.http import HttpResponse

services= ["We are ten times ahead of Technology"]
head=["Our Services"]

# Create your views here.
def services_view(request):
	return render(request,"services/services.html",{

        'services' : services,
        'head': head,

		})