from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import UpdateView , CreateView, DetailView
from jobs.forms import *
from jobs.models import *
from django.contrib import messages





@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class AddProfileView(CreateView):
    """
       Jobseekers can add their profiles
    """
    model = JobSeekerUpdateProfile
    form_class = JobseekerProfileUpdateForm
    template_name = 'jobs/jobseeker/add_profile.html'
    success_url = reverse_lazy('jobs:jobseeker-profile-view')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Profile created successfully.')
        return super().form_valid(form)


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class ProfileDetailView(DetailView):
    """
       Jobseekers can view their profile
    """
    model = JobSeekerUpdateProfile
    template_name = 'jobs/jobseeker/view_profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_object_or_404(JobSeekerUpdateProfile, user=self.request.user)
    
    

@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class ProfileUpdateView(UpdateView):
    """
       Jobseekers can update their profile
    """
    model = JobSeekerUpdateProfile
    form_class = JobseekerProfileUpdateForm
    template_name = 'jobs/jobseeker/edit_profile.html'
    success_url = reverse_lazy('jobs:jobseeker-profile-view')
    
    def get_object(self, queryset=None):
        return JobSeekerUpdateProfile.objects.get(user=self.request.user)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.instance = self.get_object()
        return form



