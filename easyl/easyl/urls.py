"""
URL configuration for easyl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from box.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    
    path('api_schema/', get_schema_view(
        title='API Schema', 
        description='Guide for the REST API'), 
        name='schema_url'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}), 
        name='swagger-ui'),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += router.urls
