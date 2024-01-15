from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from .views import *
app_name = "accounts"

urlpatterns = [
    path('jobseeker-register', JobseekerRegisterView.as_view(), name='jobseeker-register'),
    path('recruiter-register', RecruiterRegisterView.as_view(), name='recruiter-register'),
    
    path('logout', LogoutView.as_view(), name='logout'),
    path('login', LoginView.as_view(), name='login'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
