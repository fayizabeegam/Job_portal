from django.shortcuts import get_object_or_404,render,redirect
from django.db.models import Q
from django.http import Http404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
from django.utils import timezone
from django.utils.decorators import method_decorator
from jobs.decorators import user_is_jobseeker
from django.views.generic import ListView, DetailView
from jobs.forms import ApplyJobForm
from jobs.models import *


class HomeView(ListView):
    model = JobListing
    template_name = 'home.html'
    context_object_name = 'jobs'
    ordering = ['-posted_at']
    
    def get_queryset(self):
        queryset = self.model.objects.order_by(*self.ordering)
        return queryset[:6]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trendings = self.model.objects.filter(posted_at__month=timezone.now().month).order_by(
                                                                             '-posted_at')[:3]
        context['trendings'] = trendings
        return context
        


class SearchView(ListView):
    """
       Jobseekers can search jobs based on location and title
    """
    model = JobListing
    template_name = 'jobs/search.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        location_query = self.request.GET.get('location', '')
        title_query = self.request.GET.get('title', '')
        query = Q(location__icontains=location_query) & Q(title__icontains=title_query)
        return self.model.objects.filter(query)  
                                         

# class JobCategoryListView(ListView):
#     model = JobCategory
#     template_name = 'jobs/job_categories.html'
#     context_object_name = 'categories'

    
class JobListView(ListView):
    """
       List the posted jobs
    """
    model = JobListing
    template_name = 'jobs/jobs.html'
    context_object_name = 'jobs'
    paginate_by = 5
    ordering = ['-posted_at']  

    def get_queryset(self):
        return super().get_queryset()


class JobDetailsView(DetailView):
    """
       Jobseekers and recruiters can see the job details
    """
    model = JobApplication
    template_name = 'jobs/details.html'
    context_object_name = 'job'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        obj = get_object_or_404(JobListing, id=self.kwargs.get(self.pk_url_kwarg))
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("Job doesn't exists")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
    

@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
@method_decorator(user_is_jobseeker, name='dispatch')
class ApplyJobView(View):
    """
       jobseekers can apply the jobs
    """
    def get(self, request, job_id):
        form = ApplyJobForm(job_id=job_id, user=request.user)
        return render(request, 'jobs/apply_job.html', {'form': form, 'job_id': job_id})

    def post(self, request, job_id):
        form = ApplyJobForm(request.POST, request.FILES, job_id=job_id, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('jobs:jobs-detail', id=job_id)
        else:
            return render(request, 'jobs/apply_job.html', {'form': form, 'job_id': job_id})




@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class AppliedJobsListView(ListView):
    model = JobApplication
    template_name = 'jobs/applied_jobs_list.html'
    context_object_name = 'applied_jobs'
    paginate_by = 5  

    def get_queryset(self):
        # Get applied jobs for the current user
        return JobApplication.objects.filter(job_seeker=self.request.user).distinct()