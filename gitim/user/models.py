from django.db import models
from random import randint


# Create your models here.

class Users(models.Model):
    GID = models.IntegerField(default=randint(0, 1000000000))
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6)
    signature = models.CharField(max_length=50, default='这个人并没有注意到个人简介这个功能，真遗憾')
    email = models.CharField(max_length=20)

    def __str__(self):
        return self.GID + self.name
