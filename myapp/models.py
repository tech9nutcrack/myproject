from operator import mod
from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    address = models.TextField()