from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class JobseekerRegistrationForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(JobseekerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['fullname'].label = "Full Name"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

        self.fields['username'].widget.attrs.update(
            {
                'placeholder': 'Enter Username',
            }
        )
        
        self.fields['fullname'].widget.attrs.update(
            {
                'placeholder': 'Enter Full Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )

    class Meta:
        model = User
        fields = [ 'username','fullname', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "jobseeker"
        if commit:
            user.save()
        return user


class RecruiterRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RecruiterRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['fullname'].label = "Full name"
        self.fields['email'].label = "Email"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

        self.fields['username'].widget.attrs.update(
            {
                'placeholder': 'Enter Username',
            }
        )
        self.fields['fullname'].widget.attrs.update(
            {
                'placeholder': 'Enter Full Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )

    class Meta:
        model = User
        fields = ['username','fullname', 'email', 'password1', 'password2']
       

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "recruiter"
        if commit:
            user.save()
        return user



class UserLoginForm(forms.Form):
    username_or_email = forms.CharField(
        label="Username",
        max_length=254,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}),
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self, *args, **kwargs):
        username_or_email = self.cleaned_data.get("username_or_email")
        password = self.cleaned_data.get("password")

        if username_or_email and password:
            # Try to authenticate with both username and email
            self.user = authenticate(username=username_or_email, password=password)
            
            if self.user is None:
                # If authentication with username fails, try with email
                self.user = authenticate(email=username_or_email, password=password)

            if self.user is None:
                raise forms.ValidationError("Invalid login credentials.")
            
            if not self.user.is_active:
                raise forms.ValidationError("User is not active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user


