from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView, ListView, UpdateView, DetailView
)
from django.views import View
from jobs.decorators import user_is_recruiter
from jobs.forms import *
from jobs.models import *


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class AddRecruiterProfileView(CreateView):
    """
        Recruiter can add their profile
    """
    model = RecruiterUpdateProfile
    form_class = RecruiterProfileUpdateForm
    template_name = 'jobs/recruiter/recruiter_profile_add.html'
    success_url = reverse_lazy('jobs:recruiter-profile-view')

    def form_valid(self, form):
        # Set the user for the recruiter profile being created
        form.instance.user = self.request.user
        messages.success(self.request, 'Profile created successfully.')
        return super().form_valid(form)


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class RecruiterProfileDetailView(DetailView):
    """
         Recruiter can view their profile
    """
    model = RecruiterUpdateProfile
    template_name = 'jobs/recruiter/recruiter_profile_view.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return RecruiterUpdateProfile.objects.get(user=self.request.user)
    

@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class RecruiterProfileEditView(UpdateView):
    """
    Recruiter can edit their profile
    """
    model = RecruiterUpdateProfile
    form_class = RecruiterProfileUpdateForm
    template_name = 'jobs/recruiter/recruiter_profile_edit.html'
    success_url = reverse_lazy('jobs:recruiter-profile-view')

    def get_object(self, queryset=None):
        return RecruiterUpdateProfile.objects.get(user=self.request.user)

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        messages.success(self.request, 'Profile updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error updating profile. Please check the form.')
        return super().form_invalid(form)



@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class DashboardView(ListView):
    """
       Recruiter can see the posted job in their dashboard
    """
    model = JobListing
    template_name = 'jobs/recruiter/dashboard.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return self.model.objects.filter(recruiter_id=self.request.user.id)
    

class JobCreateView(CreateView):
    """
       Recruiter can post new jobs
    """
    template_name = 'jobs/create.html'
    form_class = JobPostingForm
    extra_context = {
        'title': 'Post New Job'
    }
    success_url = reverse_lazy('jobs:recruiter-dashboard')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        if self.request.user.is_authenticated and self.request.user.role != 'recruiter':
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.recruiter_id = self.request.user.id
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        

class UpdateJobView(UpdateView):
    """
      Recruiter can update the posted jobs
    """
    model = JobListing
    form_class = JobPostingForm
    template_name = 'jobs/edit.html'
    success_url = reverse_lazy('jobs:recruiter-dashboard')

    def get_object(self, queryset=None):
        job_id = self.kwargs.get('job_id')
        return get_object_or_404(JobListing, id=job_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job_id = self.kwargs.get('job_id')
        job_listing = get_object_or_404(JobListing, id=job_id)
        context['job_listing'] = job_listing
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
    

def delete_job_view(request, job_id):
    """
       Recruiter can delete the jobs
    """
    job = get_object_or_404(JobListing, id=job_id, recruiter=request.user)

    try:
        job.delete()
        redirect_url = reverse('jobs:recruiter-dashboard')
        return JsonResponse({'success': 'Job deleted successfully', 'redirect_url': redirect_url})
    except Exception as e:
        return JsonResponse({'error': f'Error deleting job: {str(e)}'})
    
    
@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(user_is_recruiter, name='dispatch')
class ApplicantPerJobView(ListView):
    """ 
       Recruiter can see the applicants per a job
    """
    model = JobApplication
    template_name = 'jobs/recruiter/applicants.html'
    context_object_name = 'applicants'
    paginate_by = 1

    def get_queryset(self):
        return JobApplication.objects.filter(job_listing_id=self.kwargs['job_id']).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = JobListing.objects.get(id=self.kwargs['job_id'])
        return context


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(user_is_recruiter, name='dispatch')
class ApplicantsListView(ListView):
    """
       List all applicants
    """
    model = JobApplication
    template_name = 'jobs/recruiter/all-applicants.html'
    context_object_name = 'applicants'

    def get_queryset(self):
        return self.model.objects.filter(job_listing__recruiter=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recruiter'] = self.request.user
        return context


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class ManageApplicatStatusView(View):
    """
      Recruiter can manage the applicantions from applicants
    """
    def post(self, request, *args, **kwargs):
        action = self.kwargs.get('action')
        applicant_id = self.kwargs.get('applicant_id')
        applicant = get_object_or_404(JobApplication, id=applicant_id)

        # Check if the applicant is associated with the current user's job
        if applicant.job_listing.recruiter != request.user:
            messages.error(request, "You don't have permission to perform this action.")
            return redirect('jobs:recruiter-all-applicants')

        # Update the status based on the action
        if action == 'accept':
            applicant.status = 'Accepted'
            messages.success(request, f"{applicant.job_seeker} has been accepted for the job.")
        elif action == 'reject':
            applicant.status = 'Rejected'
            messages.success(request, f"{applicant.job_seeker} has been rejected for the job.")
        else:
            messages.error(request, "Invalid action.")

        applicant.save()
        return redirect('jobs:recruiter-all-applicants')