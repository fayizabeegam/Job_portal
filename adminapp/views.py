from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.db.models import F
from django.shortcuts import get_object_or_404,redirect
from django.http import HttpResponse, JsonResponse
from typing import Any
from django.shortcuts import render
from django.views import View
from django.views.generic import*
from django.views.generic.list import MultipleObjectMixin
from jobs.models import *
from .forms import *
from django.contrib import messages


class AdminHomeView(View):
    template_name = 'admin/admin_home.html'  

    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Admin Home',
        }
        return render(request, self.template_name, context)


def is_admin(user):
    return user.is_authenticated and user.is_staff


class AddCategories(CreateView):
    model = JobCategory
    form_class = AddCategoryForm
    template_name = "admin/add_categories.html"
    context_object_name = 'categories'
    success_url = reverse_lazy('adminapp:add-category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = JobCategory.objects.all()  # Add categories to context
        return context

    def form_valid(self, form):
        # Save the category
        messages.success(self.request, 'Category added successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Handle errors
        messages.error(self.request, 'Error adding category.')
        return super().form_invalid(form)

class EditCategory(UpdateView):
    model = JobCategory
    form_class = AddCategoryForm
    template_name = "admin/add_categories.html"
    success_url = reverse_lazy('adminapp:add-category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = JobCategory.objects.all()
        context['editing'] = True  # Flag for editing mode
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Category updated successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error updating category.')
        return super().form_invalid(form)


class DeleteCategory(DeleteView):
    model = JobCategory
    template_name = "admin/add_categories.html"  # Create a delete confirmation template
    success_url = reverse_lazy('adminapp:add-category')

    def post(self, request, *args, **kwargs):
        category = self.get_object()

        # Delete associated job listings first
        JobListing.objects.filter(category=category).delete()
        messages.success(self.request, 'Category and associated jobs deleted successfully!')

        # Now, call the parent class's post method to handle the actual deletion
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return redirect('adminapp:add-category') # or a dedicated delete confirmation page



class JobSeekerListView(ListView):
    """
        List all jobseekers
    """
    model = JobSeekerUpdateProfile
    template_name = 'admin/jobseeker_list.html'
    context_object_name = 'jobseekers'
    paginate_by = 5

    def get_queryset(self):
        return JobSeekerUpdateProfile.objects.all().order_by('id')
        # return User.objects.filter(role='jobseeker').order_by('id')
    

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


class AppliedJobsListView(ListView):
    """
        Admin can see the applied jobs of jobseeker
    """
    model = JobApplication
    template_name = 'jobs/applied_jobs_list.html'
    context_object_name = 'applied_jobs'
    paginate_by = 5  # Set the number of items per page

    def get_queryset(self):
        # Get applied jobs for the specified job seeker
        job_seeker_id = self.kwargs.get('user_id')
        return JobApplication.objects.filter(job_seeker_id=job_seeker_id).distinct()


class RecruitersListView(ListView):
    """
        List all recruiters
    """
    model = RecruiterUpdateProfile
    template_name = 'admin/recruiter_list.html'
    context_object_name = 'recruiters'
    paginate_by = 5

    def get_queryset(self):
        return RecruiterUpdateProfile.objects.all()
    

@user_passes_test(is_admin, login_url=reverse_lazy('accounts:login'))
def admin_recruiter_profile_view(request, user_id ):
    """
       Retrieve the user profile based on the provided user_id
    """
    recruiter_profile = get_object_or_404(RecruiterUpdateProfile, user_id=user_id)
    return render(request, 'admin/recruiter_profile_details.html', {'recruiter_profile': recruiter_profile})


class AdminRecruiterDashboardView(ListView):
    model = JobListing
    template_name = 'admin/admin_recruiter_dashboard.html'
    context_object_name = 'jobs'
    paginate_by = 5

    def get_queryset(self):
        # Retrieve the recruiter ID from the URL parameters
        recruiter_id = self.kwargs.get('recruiter_id')
        recruiter_user = get_object_or_404(User, id=recruiter_id)
        # Filter jobs based on the recruiter ID
        return self.model.objects.filter(recruiter=recruiter_user).order_by(F('posted_at').desc())

    