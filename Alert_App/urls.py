from django.urls import path
from django.views.generic.base import TemplateView, RedirectView
from django.conf import settings
from django.conf.urls.static import static 

from . import views

app_name = "AlertApp" 
urlpatterns = [
	path('',TemplateView.as_view(template_name="home.html"),name="home"),
	path('index/',views.index,name="index"),
	path('report/',views.report,name="report"),
	path('map/',views.map,name="map"),
	path("response/",views.response,name="response"),
	path("sentReport/",views.sendReport,name="sendReport"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# Potential page travel: Home > Login > Index > Report > Map > Home