from django.urls import include, path
from box.views import *
from rest_framework import routers

app_name = 'box'


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    
    path('', include(router.urls)),
]

