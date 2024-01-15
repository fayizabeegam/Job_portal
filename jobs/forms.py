from django import forms
from .models import *


class JobseekerProfileUpdateForm(forms.ModelForm):
    resume = forms.FileField(
        label='Resume',
        required=False,
        widget=forms.FileInput(
            attrs={'placeholder': 'Upload Resume', 
                   'accept': 'application/pdf, application/msword'
                   }),
    )
    profile_picture = forms.ImageField(
        label='Profile Picture',
        required=False,
        widget=forms.FileInput(
            attrs={'placeholder': 'Profile Picture', 
                   'accept': 'image/jpg, image/png'
                   }),

    )
    def __init__(self, *args, **kwargs):
        super(JobseekerProfileUpdateForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.resume:
            self.fields['resume'].initial = self.instance.resume
            
        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'Title',
            }
        )
        self.fields['bio'].widget.attrs.update(
            {
                'placeholder': 'Bio',
            }
        )
        self.fields['skills'].widget.attrs.update(
            {
                'placeholder': 'Skills',
            }
        )
        self.fields['education'].widget.attrs.update(
            {
                'placeholder': 'Educational Details',
            }
        )
        self.fields['experience'].widget.attrs.update(
            {
                'placeholder': 'Experience',
            }
        )
        self.fields['phone_number'].widget.attrs.update(
            {
                'placeholder': 'Mobile',
            }
        )
        self.fields['address'].widget.attrs.update(
            {
                'placeholder': 'Address',
            }
        )
        self.fields['state'].widget.attrs.update(
            {
                'placeholder': 'State',
            }
        )
        self.fields['place'].widget.attrs.update(
            {
                'placeholder': 'Location',
            }
        )

    class Meta:
        model = JobSeekerUpdateProfile
        fields = [
            "title", "bio", "skills",
            "education","experience","resume","phone_number",
            "address","state","place","profile_picture"
        ]


class RecruiterProfileUpdateForm(forms.ModelForm):
    profile_picture = forms.ImageField(
        label='Profile Picture',
        required=False,
        widget=forms.FileInput(
            attrs={'placeholder': 'Profile Picture', 
                   'accept': 'image/jpg, image/png'
                   }),

    )
    def __init__(self, *args, **kwargs):
        super(RecruiterProfileUpdateForm, self).__init__(*args, **kwargs)

        self.fields['designation'].widget.attrs.update(
            {
                'placeholder': 'Designation',
            }
        )
        self.fields['company_name'].widget.attrs.update(
            {
                'placeholder': 'Company Name',
            }
        )
        self.fields['company_description'].widget.attrs.update(
            {
                'placeholder': 'Description',
            }
        )
        self.fields['company_location'].widget.attrs.update(
            {
                'placeholder': 'Location',
            }
        )
        self.fields['industry'].widget.attrs.update(
            {
                'placeholder': 'Industry',
            }
        )
        self.fields['established_year'].widget.attrs.update(
            {
                'placeholder': 'Established Year',
            }
        )
    class Meta:
        model = RecruiterUpdateProfile
        fields = [
            "designation","company_name","company_description",
            "company_location","industry","established_year",
            "profile_picture"
        ]


class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        exclude = ('recruiter', 'posted_at','status',)

    def is_valid(self):
        valid = super(JobPostingForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        job = super(JobPostingForm, self).save(commit=False)
        if commit:
            job.save()
        return job
    

class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['resume', 'cover_letter']

    def __init__(self, *args, job_id=None, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_id = job_id
        self.user = user

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.job_id:
            instance.job_listing_id = self.job_id
        if self.user:
            instance.job_seeker_id = self.user.id
        if commit:
            instance.save()
        return instance