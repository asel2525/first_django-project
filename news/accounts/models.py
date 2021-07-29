from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    class UserType(models.TextChoices):
        ADMIN = 'admin'
        EDITOR ='editor'
        ORDINARY = 'ordinary'

    role = models.CharField(max_length=10, choices=UserType.choices, default=UserType.ORDINARY)
    
