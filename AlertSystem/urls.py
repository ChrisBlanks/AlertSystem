from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic.base import RedirectView,TemplateView
from AlertSystem import settings

urlpatterns = [
    path("user/",include("django.contrib.auth.urls") ),
    path('AlertApp/',include('Alert_App.urls'),name="AlertApp" ),
    path('admin/', admin.site.urls,name="admin"),
	path("",RedirectView.as_view(url="AlertApp/")),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

