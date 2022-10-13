import random

from django.shortcuts import render

# Create your views here.
from .models import *
from django.shortcuts import render
from .forms import QuestionForm
def index(request):
    context = {}
    request.session['number_list'] = []
    request.session['question_answer'] = []
    request.session['count_check'] = 0
    print(request.session.session_key)
    print(request.session['number_list'])
    return render(request, 'insight/home.html', context)


def detailp(request):
    context = {}

    return render(request, 'insight/detailpage.html', context)


def test(request, *args, **kwargs):

    question_list = Question.objects.order_by('id')


    number_list = request.session['number_list']
    question_answer_list = request.session['question_answer']
    count = request.session['count_check']
    count += 1
    while True:
        number = random.randrange(0, len(question_list))
        if number in number_list:
            continue
        else:
            break

    question_answer = question_list[number].answer
    number_list.append(number)
    question_answer_list.append(int(question_answer))
    request.session['number_list'] = number_list
    request.session['question_answer'] = question_answer_list
    request.session['count_check'] = count
    context = {'question': question_list[number]}

    if request.method == 'POST':
        user_input_answer = request.POST.get('answer')
        print(question_answer_list[len(question_answer_list)-2], ':', user_input_answer)
        if int(question_answer_list[len(question_answer_list)-2]) == int(user_input_answer):
            print("정답")
        else:
            print('오답')

    print(len(number_list))
    if count > 2:
        request.session['count_check'] = 0
        return render(request, 'insight/home.html', context)

    return render(request, 'insight/test.html', context)
def end(request):
    return render(request,'insight/end_page.html')
def suggestion(request):
    return render(request,'insight/suggestion_page.html')
def test_page(request):
    return render(request,'insight/test_page.html')



