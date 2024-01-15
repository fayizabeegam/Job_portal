from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from jobs.views.jobseeker import *
from jobs.views.recruiter import *
from jobs.views.home import *
from .views import *

app_name = "adminapp"

urlpatterns = [

    path('admin-home/', AdminHomeView.as_view(), name='admin-home'),

    path('jobseekers-list/', JobSeekerListView.as_view(), name='admin-jobseeker-list'),
    path('recruiters-list/',RecruitersListView.as_view(),name='admin-recruiter-list'),

    path('admin-jobseeker-profile-view/<int:user_id>/', admin_jobseeker_profile_view, name='admin-jobseeker-profile-view'),
    path('admin-recruiter-profile-view/<int:user_id>/', admin_recruiter_profile_view, name='admin-recruiter-profile-view'),

    # path('update-jobseeker-status/<int:user_id>/', update_jobseeker_status, name='update-jobseeker-status'),

    path('applied-jobs/<int:user_id>/', AppliedJobsListView.as_view(), name='applied-jobs'),




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)