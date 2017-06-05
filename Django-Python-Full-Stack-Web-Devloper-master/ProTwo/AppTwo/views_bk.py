from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.

def index(request):
    return render(request,'AppTwo/index.html')

def users(request):
    user_dict = {'user_records':User.objects.all()}
    return render(request,'AppTwo/users.html',context=user_dict)
