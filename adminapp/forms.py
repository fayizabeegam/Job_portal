from django import forms
from jobs.models import*

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


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = JobCategory
        fields = ['category','icon_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs.get('instance'):  # Editing an existing category
            self.fields['category'].required = False
            self.fields['icon_image'].required = False
        else:  # Adding a new category
            self.fields['category'].required = True  # Explicitly set to True
            self.fields['icon_image'].required = True  # Explicitly set to True