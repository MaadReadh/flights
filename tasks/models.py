from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.
class task (models.Model):
     title = models.CharField(max_length=50)
     content = models.CharField(max_length=50)
    

     