from django.urls import path
from django.views.generic.base import TemplateView, RedirectView
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth.views import LoginView
from . import views
from Alert_App.models import Marker, DeviceId
app_name = "AlertApp" 


urlpatterns = [
	path('',TemplateView.as_view(template_name="home.html"),name="home"),
	
	path('login/',LoginView.as_view( template_name="registration/login.html",
	extra_context={'device_ids': [ marker.deviceid.id_number for marker in Marker.objects.all() ] }  ) , name="login_page"),
	
	#path('login/',views.login_page ,name="login_page"),
	path('index/',views.index,name="index"),
	path('report/',views.report,name="report"),
	path('map/',views.map,name="map"),
	path("response/",views.response,name="response"),
	path("sentReport/",views.sendReport,name="sendReport"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# Potential page travel: Home > Login > Index > Report > Map > Home