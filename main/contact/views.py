from django.shortcuts import render
from django.http import HttpResponse

Help= ["Help Center"]
intro=["Welcome to our help Center"]

# Create your views here.
def contact_view(request):
	return render(request,"contact/cont.html",{

        'Help': Help,
        'intro': intro,

		})

	

