from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from models import urls as models_urls

urlpatterns = [
	path('', views.home, name="home"),
	path('models/', include(models_urls)),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)