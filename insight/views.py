import random

from django.shortcuts import render

# Create your views here.
from .models import *
from django.shortcuts import render

def index(request):
    context = {}
    request.session['number_list'] = []
    print(request.session.session_key)
    print(request.session['number_list'])
    return render(request, 'insight/home.html', context)




def detailp(request):
    context = {}

    return render(request, 'insight/detailpage.html', context)


def test(request):

    question_list = Question.objects.order_by('id')
    print(request.session.session_key)

    number_list = request.session['number_list']
    print(number_list)
    while True:
        number = random.randrange(0, len(question_list))
        if number in number_list:
            continue
        else:
            break

    number_list.append(number)
    request.session['number_list'] = number_list

    context = {'question': question_list[number]}

    return render(request, 'insight/test.html', context)









