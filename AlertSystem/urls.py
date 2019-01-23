from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView,TemplateView


urlpatterns = [
    path("user/",include("django.contrib.auth.urls") ),
    path('Alert_App/',include('Alert_App.urls'),name="AlertApp" ),
    path('admin/', admin.site.urls,name="admin"),
    path('',TemplateView.as_view(template_name="home.html"),name="home"),
    ]
