from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Assist(models.Model):
    project = models.CharField(max_length=100)
    manufacture = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    due = models.CharField(max_length=100)
    details = models.CharField(max_length=5000)
