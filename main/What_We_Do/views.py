from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def What_We_Do_view(request):

	return render(request,'en/us.html')


def journey(request):
	return render(request,'en/What_We_Do.html')

