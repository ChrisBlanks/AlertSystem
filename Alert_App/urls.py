from django.urls import path

from . import views

app_name = "Alert_App" 
urlpatterns = [
    path('',views.index,name="index"),
]
