from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')   

def update(request):
    return render(request,'update.html')

def welcome(request):
    return render(request,'welcome.html') 

def base(request):
    return render(request,'base.html') 

def table(request):
    return render(request,'table.html')    

def form_data(request):
    if request.method== 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        Company_name= request.POST['company']
        Email_name= request.POST['Email']
        Phone_number= request.POST['Phone']
        Password= request.POST['Password']
        if Person.object.filter(Phone_number=Phone_number).exists():
            messages.error(request,"phone number already exists")
            return redirect('/')
        elif Person.objects.filter(Email_name=Email_name).exists():
            messages.error(request,"Email id already exists")    