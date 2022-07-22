from django.db import models
from django.contrib import auth
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    sex = models.IntegerField()
    want_field = models.IntegerField()
    age = models.TextField()
    front_level = models.IntegerField()
    back_level = models.IntegerField()
    data_level = models.IntegerField()
