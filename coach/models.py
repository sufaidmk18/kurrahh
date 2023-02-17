from ast import Mod
from email.headerregistry import Address
from email.policy import default
from turtle import position
from unittest.util import _MAX_LENGTH
from xmlrpc.client import Boolean
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Coach(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) :
        return self.user.username
class Student(models.Model):
    name=models.CharField( max_length=50)
    dob=models.DateField( auto_now=False, auto_now_add=False)
    #photo=models.FileField(upload_to=None, max_length=100)
    housename=models.CharField(max_length=50)
    post=models.CharField( max_length=50)
    place=models.CharField(max_length=50)
    panchayath=models.CharField(max_length=50)
    district=models.CharField( max_length=50)
    position=models.CharField(max_length=50)
    coach=models.ForeignKey(Coach, on_delete=models.CASCADE)
    
class Statistics(models.Model):
    Student=models.ForeignKey(Student, on_delete=models.CASCADE)
    bollcontronl=models.IntegerField(default=50)
    passaccuracy=models.IntegerField(default=50)
    stamina=models.IntegerField(default=50)
    speed=models.IntegerField(default=50)
    takles=models.IntegerField(default=50)
    shoot=models.IntegerField(default=50)

class Attendence(models.Model):
    Student=models.ForeignKey(Student, on_delete=models.CASCADE)
    present=models.BooleanField(default=False)
    date=models.DateField()

