from django import forms
from jobs.models import JobSeekerUpdateProfile

class UpdateJobSeekerStatusForm(forms.ModelForm):
    class Meta:
        model = JobSeekerUpdateProfile
        fields = ['is_active']

        labels = {
            'is_active': 'Activate/Deactivate Job Seeker',
        }

        help_texts = {
            'is_active': 'Check to activate, uncheck to deactivate.',
        }

        widgets = {
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }