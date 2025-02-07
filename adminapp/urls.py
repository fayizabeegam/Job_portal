from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from jobs.views.jobseeker import *
from jobs.views.recruiter import *
from jobs.views.home import *
from .views import *
from . import views

app_name = "adminapp"

urlpatterns = [

    path('admin-home/', AdminHomeView.as_view(), name='admin-home'),

    path('add-categories/', AddCategories.as_view(), name='add-category'),
    path('edit-category/<int:pk>/', views.EditCategory.as_view(), name='edit-category'), 
    path('delete-category/<int:pk>/', views.DeleteCategory.as_view(), name='delete-category'), 

    
    path('jobseekers-list/', JobSeekerListView.as_view(), name='admin-jobseeker-list'),
    path('recruiters-list/',RecruitersListView.as_view(),name='admin-recruiter-list'),

    path('admin-jobseeker-profile-view/<int:user_id>/', admin_jobseeker_profile_view, name='admin-jobseeker-profile-view'),
    path('admin-recruiter-profile-view/<int:user_id>/', admin_recruiter_profile_view, name='admin-recruiter-profile-view'),
    path('admin-recruiter-dashboard/<int:recruiter_id>/', AdminRecruiterDashboardView.as_view(), name='admin-recruiter-dashboard'),
    

    path('applied-jobs/<int:user_id>/', AppliedJobsListView.as_view(), name='applied-jobs'),




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)