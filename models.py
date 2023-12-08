from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Userprofile(models.Model):
    # Casacade is to delete a user completely
    # User is taken from django.contrib.auth.models to apply to admin and
    # To get user profile open the shell
    # python3 manage.py shell
    # from django.contrib.auth.models import User
    # from userprofile.models import Userprofile
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
