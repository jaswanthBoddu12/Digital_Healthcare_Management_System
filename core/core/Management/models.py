from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True,null=True)
    bio=models.TextField(null=True,blank=True)
    gender=models.CharField(max_length=20,null=True)
    is_staff = models.BooleanField(default=False)
    is_paitent = models.BooleanField(default=False)
    Mobile=models.CharField(max_length=10,null=True,blank=True)
    dob = models.DateField(max_length=8,null=True,blank=True)
    bloodgroup = models.CharField(max_length=14, blank=True, null=True)
    address=models.TextField(blank=True, null=True)
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.username

class Record(models.Model):
    patientname=models.ForeignKey(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=10)
    dob = models.DateField(max_length=8,null=True,blank=True)
    bloodgroup = models.CharField(max_length=14, blank=True, null=True)
    prescription=models.TextField()
    Doctorname=models.CharField(max_length=40)
    Record_id=models.UUIDField(max_length=8,default=uuid.uuid4)