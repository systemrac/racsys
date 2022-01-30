from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def account_view(request):
	
	return render(request,'account/acc.html')

def My_User(request):

	return HttpResponse('this is the admin logout')
	