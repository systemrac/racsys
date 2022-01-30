from django.http import HttpResponse
from django.shortcuts import render


company = ["creating systems","Web based applications","school systems"]
vission = ["Enhencing Technology"]
intro = ["The metaverse is the next evolution of social connection. Our company’s vision is to help bring the metaverse to life, so we are changing our name to reflect our commitment to this future."]

# Create your views here.
def home_view(request):
	return render(request,'home/home.html',{

		"company": company ,
		"vission": vission ,
		"intro": intro,
		})