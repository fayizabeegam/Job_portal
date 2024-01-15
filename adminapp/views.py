from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from typing import Any
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from jobs.models import *
from .forms import *


class AdminHomeView(View):
    template_name = 'admin/admin_home.html'  

    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Admin Home',
        }
        return render(request, self.template_name, context)


def is_admin(user):
    return user.is_authenticated and user.is_staff

class JobSeekerListView(ListView):
    """
        List all jobseekers
    """
    model = JobSeekerUpdateProfile
    template_name = 'admin/jobseeker_list.html'
    context_object_name = 'jobseekers'

    def get_queryset(self):
        return JobSeekerUpdateProfile.objects.all()
    

@user_passes_test(is_admin, login_url=reverse_lazy('accounts:login'))
def admin_jobseeker_profile_view(request, user_id ):
    """
        Retrieve the user profile based on the provided user_id
    """
    jobseeker_profile = get_object_or_404(JobSeekerUpdateProfile, user_id=user_id)
    return render(request, 'admin/jobseeker_profile_details.html', {'jobseeker_profile': jobseeker_profile})

# @user_passes_test(is_admin, login_url=reverse_lazy('accounts:login'))
# def update_jobseeker_status(request, user_id):
#     """
#        Deactivate jobseeker account
#     """
#     jobseeker_profile = get_object_or_404(JobSeekerUpdateProfile, user_id=user_id)

#     if request.method == 'POST':
#         form = UpdateJobSeekerStatusForm(request.POST)
#         if form.is_valid():
#             jobseeker_profile.is_active = form.cleaned_data['is_active']
#             jobseeker_profile.save()

#             return JsonResponse({'message': 'Status updated successfully'})
#         else:
#             return JsonResponse({'error': 'Invalid form data'}, status=400)

#     # Handle GET requests if needed
#     return JsonResponse({'error': 'Invalid request method'}, status=400)



class AppliedJobsListView(View):
    """
      Applied jobs of each jobseeker
    """
    template_name = 'admin/jobseeker_applied_jobs.html'
    def get(self, request, *args, **kwargs):
        # Get the job seeker ID from the URL parameters
        job_seeker_id = self.kwargs.get('user_id')

        # Get applied jobs for the specified job seeker
        applied_jobs = JobApplication.objects.filter(job_seeker_id=job_seeker_id).distinct()

        context = {'applied_jobs': applied_jobs}
        return render(request, self.template_name, context)



class RecruitersListView(ListView):
    """
        List all recruiters
    """
    model = RecruiterUpdateProfile
    template_name = 'admin/recruiter_list.html'
    context_object_name = 'recruiters'

    def get_queryset(self):
        return RecruiterUpdateProfile.objects.all()
    

@user_passes_test(is_admin, login_url=reverse_lazy('accounts:login'))
def admin_recruiter_profile_view(request, user_id ):
    """
       Retrieve the user profile based on the provided user_id
    """
    recruiter_profile = get_object_or_404(RecruiterUpdateProfile, user_id=user_id)
    return render(request, 'admin/recruiter_profile_details.html', {'recruiter_profile': recruiter_profile})