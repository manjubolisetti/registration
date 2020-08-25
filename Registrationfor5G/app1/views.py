from django.shortcuts import render
from .models import RegisterModel
from django.db.utils import IntegrityError
# Create your views here.
def register(request):
    return render(request,"register.html")
def savedetails(request):
    first_name=request.POST['fname']
    last_name = request.POST['lname']
    mobileno = request.POST['mobilenumber']
    email = request.POST['email']
    try:
        RegisterModel(First_name=first_name,Last_name=last_name,Mobile_number=mobileno,email=email).save()
        return render(request, "register.html", {'data': "Registered Successfully"})
    except IntegrityError:
        return render(request,"register.html",{"data1":"User already exist"})

