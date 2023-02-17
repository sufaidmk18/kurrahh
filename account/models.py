from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField()
    name=models.CharField( max_length=50)
    dob=models.DateField( auto_now=False, auto_now_add=False)
    #photo=models.FileField(upload_to=None, max_length=100)
    housename=models.CharField(max_length=50)
    post=models.CharField( max_length=50)
    place=models.CharField(max_length=50)
    panchayath=models.CharField(max_length=50)
    district=models.CharField( max_length=50)
    position=models.CharField(max_length=50)