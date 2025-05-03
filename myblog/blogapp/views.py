from django.shortcuts import render ,redirect
from.models import Adminlogin ,Enquiry
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
import datetime
def index(req):
    return  render(req,"index.html")


def home(req):
    return render(req,"home.html")

def login(req):
    return render(req,"login.html")


def admindashboard(req):
    return render(req,"admindashboard.html")


def customerdashboard(req):
    return render(req,'customerdashboard.html')

def signup(req):
    return render(req,"signup.html")

def contact(req):
    if req.method=="POST":
        name=req.POST['name']
        address=req.POST['address']
        emailaddress=req.POST['emailaddress']
        enquirytext=req.POST['enquirytext']
        enquirydate=datetime.datetime.today()
        enq=Enquiry(name=name,address=address,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)
        enq.save()
        msg="Your enquiry is submitted successfully"
        return render(req,"contact.html",{'msg':msg})   
    return render(req,"contact.html")




def aboutus(req):
    return render(req,"aboutus.html")

def customer(req):
    return render(req,'customer.html')

def cake(req):
    return render(req,'cake.html')


#        



