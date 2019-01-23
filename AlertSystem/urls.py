from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView,TemplateView


urlpatterns = [
    path("user/",include("django.contrib.auth.urls") ),
    path('AlertApp/',include('Alert_App.urls'),name="AlertApp" ),
    path('admin/', admin.site.urls,name="admin"),
	path("",RedirectView.as_view(url="AlertApp/")),
    ]
