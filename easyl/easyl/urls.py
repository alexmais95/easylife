from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


from box.views import *

router = routers.DefaultRouter()
router.register(r'box', BoxViewSet, basename='box')


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
    path('api/v1/', include(router.urls)),
    path('api/v1/client/', ClientApiView.as_view(), name='add_client' ),
    path('api/v1/client/<int:pk>', ClientApiView.as_view(), name='client' ),
    path('api/v1/userbox/', UserBoxlist.as_view(), name='user_box'),
    path('api/v1/operation/', OperationVievList.as_view(), name='operation'),
    path('api/v1/coin/', CoinVievList.as_view(), name='coin')
    
    
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




