from django.db import models


# Create your models here.

class Users(models.Model):
    uuid = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6)
    age = models.DateTimeField
    signature = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
