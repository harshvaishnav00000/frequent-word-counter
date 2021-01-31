from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class counter(models.Model):
    storedurl = models.CharField(max_length=500000, default="")
    value = models.CharField(max_length=500000, default="")
