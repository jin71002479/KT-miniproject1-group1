from turtle import Turtle
from django.db import models
from django.contrib.auth.models import AbstractUser
from sqlalchemy import true

class User(AbstractUser):

    student_id = models.CharField(max_length=10,)
    fullname = models.CharField(max_length=10,)
    phone = models.CharField(max_length=10,)
    score = models.IntegerField(null=True)
    count=models.IntegerField()