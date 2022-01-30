from django.urls import path
from What_We_Do import  views


urlpatterns=[
     path(' What_We_Do_view/',views. What_We_Do_view, name=' What_We_Do_view'),
     path('journey/',views.journey, name='journey'),

    
]