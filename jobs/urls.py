from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from jobs.views.jobseeker import *
from jobs.views.recruiter import *
from jobs.views.home import *


app_name = "jobs"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search', SearchView.as_view(), name='searh'),
   

    path('recruiter/dashboard', include([
       
        path('', DashboardView.as_view(), name='recruiter-dashboard'),
        path('all-applicants', ApplicantsListView.as_view(), name='recruiter-all-applicants'),
        path('applicants/<int:job_id>', ApplicantPerJobView.as_view(), name='recruiter-dashboard-applicants'),
        path('update-application-status/<str:action>/<int:applicant_id>/', ManageApplicatStatusView.as_view(), name='update-application-status'),
        path('recruiter/jobs/<int:job_id>/delete/',delete_job_view, name='recruiter-jobs-delete'),
    ])),


    path('recruiter-profile-add/', AddRecruiterProfileView.as_view(), name='recruiter-profile-add'),
    path('recruiter-profile-view/', RecruiterProfileDetailView.as_view(), name='recruiter-profile-view'),
    path('recruiter-profile-edit/', RecruiterProfileEditView.as_view(), name='recruiter-profile-edit'),
    path('search/jobseekers/', SearchJobSeekersView.as_view(), name='search-jobseekers'),
     
     

    path('apply/<int:job_id>/', ApplyJobView.as_view(), name='apply-job'),
    path('applied-jobs/', AppliedJobsListView.as_view(), name='applied-jobs'),
    path('jobs', JobListView.as_view(), name='jobs'),
    path('jobs/<int:id>', JobDetailsView.as_view(), name='jobs-detail'),
    path('recruiter/jobs/create', JobCreateView.as_view(), name='recruiter-jobs-create'),
    path('recruiter/jobs/<int:job_id>/edit', UpdateJobView.as_view(), name='recruiter-jobs-edit'),
    path('jobs', JobListView.as_view(), name='jobs'),


    
    path('jobseeker-profile-add/', AddProfileView.as_view(), name='jobseeker-profile-add'),
    path('jobseeker-profile-edit/', ProfileUpdateView.as_view(), name='jobseeker-profile-edit'),
    path('jobseeker-profile-view/', ProfileDetailView.as_view(), name='jobseeker-profile-view'),
   
     
     
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)