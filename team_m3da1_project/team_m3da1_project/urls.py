from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('Plan_It_Teknoy.urls', namespace='Plan_It_Teknoy')), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
