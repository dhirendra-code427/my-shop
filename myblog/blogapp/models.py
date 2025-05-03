from django.db import models
import datetime
from django.utils.timezone import now

# Create your models here.

class Adminlogin(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class Enquiry(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=50)
    address=models.TextField()
    emailaddress=models.CharField(max_length=50)
    enquirytext=models.TextField()
    enquirydate=models.CharField(max_length=30)
