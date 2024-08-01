from django.db import models
from django.db.models import CharField
# Create your models here.

class userprofile(models.Model):
    fullname=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    DOB=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    email = models.EmailField(max_length=255, blank=True, null=True)
    mobilenumber = models.CharField(max_length=20)
    education = models.CharField(max_length=200)
    skills = models.CharField(max_length=200,blank=True, null=True)




def __str__(self):
    return '{}'.format(self.fullname)

