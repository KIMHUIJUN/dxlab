from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'insight/home.html', context)


