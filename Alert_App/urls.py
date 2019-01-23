from django.urls import path
from django.views.generic.base import TemplateView, RedirectView

from . import views

app_name = "AlertApp" 
urlpatterns = [
    path('',views.index,name="index"),
	path('report/',views.report,name="report"),
]

#For regular expression:
# r = raw string ;  ^ = matches the start of a string
# (\d+) = matches all numbers for one or more expressions 
# $ = matches the end