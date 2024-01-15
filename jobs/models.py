from django.db import models
from django.utils import timezone
from accounts.models import User
# Create your models here..


class JobSeekerUpdateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='jobseeker_profile_pictures/', 
        blank=True, null=True, default='jobseeker_profile_pictures/default.jpg'
    )
   
    def get_profile_picture_url(self):
        if self.profile_picture:
            return self.profile_picture.picture.url
        else:
            return '/media/jobseeker_profile_pictures/default.jpg'

    def __str__(self):
        return self.user.username


class RecruiterUpdateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.CharField(max_length=100)
    company_description = models.TextField(blank=True, null=True)
    company_location = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=50, blank=True, null=True)
    established_year = models.PositiveIntegerField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='recruiter_profile_pictures/', 
        blank=True, null=True, default='recruiter_profile_pictures/default.jpg'
    )

    def get_profile_picture_url(self):
        if self.profile_picture:
            return self.profile_picture.picture.url
        else:
            return '/media/recruiter_profile_pictures/default.jpg'

    def __str__(self):
        return self.company_name
    

class JobListing(models.Model):
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100,default='default_category')
    required_qualifications = models.TextField()
    desired_qualifications = models.TextField(blank=True, null=True)
    responsibilities = models.TextField()
    application_deadline = models.DateField()
    salary_range = models.CharField(max_length=50, blank=True, null=True)
    EMPLOYMENT_TYPE = (
        ('1','Full time'),
        ('2','Part time'),
        ('3','Contract'),
        ('4','Internship')
    )
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPE)
    EMPLOYMENT_MODE = (
        ('1','On-site'),
        ('2','Remote'),
        ('3','Hybrid')
    )
    employment_mode = models.CharField(max_length=50,blank=True,null=True,choices=EMPLOYMENT_MODE)
    company_benefits = models.TextField(blank=True, null=True)
    how_to_apply = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE)
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE,related_name='applicants')
  
    resume = models.FileField(upload_to='applications/', blank=True, null=True)
    cover_letter = models.TextField(blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')
    
    def __str__(self):
        return self.job_seeker.user.username