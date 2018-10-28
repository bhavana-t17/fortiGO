from django.shortcuts import render,redirect
from .models import UserLog
from django.contrib import messages
#from Truck import signup
# Create your views here.

def home(request):
	return render(request, 'Truck/base.html')
def signup(request):
	return render(request,'Truck/signup.html')

def register(request):
	print(request.POST)
	email = request.POST['email']
	password = request.POST['password']
	name = request.POST['name']
	pincode = request.POST['pincode']
	if UserLog.objects.filter(email = email):
		#messages.info(request,f'User Already Exists')
		return render(request,'Truck/signup.html',)
	userlog = UserLog.objects.create(email = email,password = password,name = name,pincode = pincode)
	print("You are Registered Successfully")
	return render(request,'Truck/base.html')
