from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.managers import UserManager


GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other','Other')
)

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })
    fullname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, blank=True, null=True, default="")
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                                })

    username = models.CharField(max_length=30, unique=True, blank=False,
                                error_messages={
                                    'unique': "A user with that username already exists.",
                                })
    

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()


