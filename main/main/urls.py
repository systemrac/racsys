"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


from home.views import(
    home_view,
    )
from contact .views import(
    contact_view,
    )
from account.views import(
    account_view,
    )
from services.views import(
    services_view,
    )
from What_We_Do.views import(

    What_We_Do_view,

    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view, name= 'home'),
    path('contact/',contact_view,name='contact'),
    path('account/',account_view,name='account'),
    path('services/',services_view,name ='services'),
    path('What_We_Do/', include('What_We_Do.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
