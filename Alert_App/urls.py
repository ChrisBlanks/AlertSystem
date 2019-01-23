from django.urls import path
from django.views.generic.base import TemplateView, RedirectView

from . import views

app_name = "AlertApp" 
urlpatterns = [
	path('',TemplateView.as_view(template_name="home.html"),name="home"),
	path('index/',views.index,name="index"),
	path('report/',views.report,name="report"),
]

# Potential page travel: Home > Login > Index > Report > Map > Home