from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def sys_home(request):
	return HttpResponse('welcome to systemX home page')