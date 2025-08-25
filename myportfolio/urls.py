from django.urls import path
from .views import show,resume_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',show ),
    path('resume/',resume_views,name="resume")

   ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)