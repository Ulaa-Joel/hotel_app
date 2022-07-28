from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    room_price = models.CharField(max_length=20)
    

# class Feature(models.Model):
#     name = models.CharField(max_length=100)
#     details = models.CharField(max_length=500)