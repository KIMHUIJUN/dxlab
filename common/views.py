from django.shortcuts import render
from .forms import UserForm

# Create your views here.

def signin(request):
    return render(request,'common/signin.html')

def signup(request):
    form = UserForm()
    return render(request,'common/signup.html', {'form':form})