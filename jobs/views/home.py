import requests,re,random
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
from bs4 import BeautifulSoup


class HomeView(ListView):
    # model = JobListing
    # template_name = 'home.html'
    # context_object_name = 'jobs'
    # ordering = ['-posted_at']
    
    # def get_queryset(self):
    #     queryset = self.model.objects.order_by(*self.ordering)
    #     return queryset[:6]
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     trendings = self.model.objects.filter(posted_at__month=timezone.now().month).order_by(
    #                                                                          '-posted_at')[:3]
    #     context['trendings'] = trendings
    #     return context
    model = JobCategory
    template_name = 'home.html'
    context_object_name = 'categories'
    ordering = ['category']  # Sort categories alphabetically
    paginate_by = 8  # Show 5 categories per page

    def get_context_data(self, **kwargs):
        """Add categories and trending categories if needed."""
        context = super().get_context_data(**kwargs)
        
        # Get first 5 categories for home page
        context['home_categories'] = JobCategory.objects.order_by(*self.ordering)[:5]

        context['blogs'] = self.get_blogs()
        
        return context
    
    def get_blogs(self):
        url = "https://www.naukri.com/blog/"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            blog_elements = soup.find_all("article", class_="post-card")

            blogs = []
            base_url = "https://www.naukri.com"

            for blog in blog_elements:
                title_tag = blog.find("h2")
                link_tag = blog.find("a", class_="post-card-image-link")
                desc_tag = blog.find("p")
                date_tag = blog.find("time")
                
                # Extract background-image URL
                image_div = blog.find("div", class_="post-card-image")
                image_url = None

                if image_div and "style" in image_div.attrs:
                    style_attr = image_div["style"]
                    match = re.search(r'url\((.*?)\)', style_attr)
                    if match:
                        image_url = match.group(1).strip('"').strip("'")

                title = title_tag.text.strip() if title_tag else "No Title"
                link = link_tag["href"] if link_tag else "#"
                desc = desc_tag.text.strip() if desc_tag else "No description available"
                date = date_tag.text.strip() if date_tag else "Unknown Date"

                # Ensure absolute URL for blog link
                if link.startswith("/"):
                    link = base_url + link

                # Use placeholder if image is missing
                if not image_url:
                    image_url = "default-blog-image.jpg"

                blogs.append({
                    "title": title,
                    "link": link,
                    "desc": desc,
                    "date": date,
                    "image": image_url,
                })
            
            # Shuffle blogs to display different ones each time
            random.shuffle(blogs)
            return blogs[:3]  # Show only 4 blogs
        return []
        
class MoreCategoriesView(ListView):
    model = JobCategory
    template_name = 'admin:add_categories.html'  
    context_object_name = 'categories'
    ordering = ['category']
    paginate_by = 10  # Show 10 categories per page

    def dispatch(self, request, *args, **kwargs):
        """Redirect superusers to the admin category page."""
        if request.user.is_superuser:
            return redirect('adminapp:add-category')  # Redirect to admin category management
        return super().dispatch(request, *args, **kwargs)


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