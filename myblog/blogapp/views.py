from django.shortcuts import render ,redirect
from.models import Adminlogin 
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
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
    return render(req,'contact.html')




def aboutus(req):
    return render(req,"aboutus.html")

def customer(req):
    return render(req,'customer.html')

def cake(req):
    return render(req,'cake.html')


#        



