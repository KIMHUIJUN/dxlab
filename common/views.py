

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserCreationForm
from django.http import HttpResponse

# def signup(request):
#     if request.method == "POST":
#
#         form = UserCreationForm(request.POST)
#         print(form)
#         print(form)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('email')
#             print(username)
#             raw_password = form.cleaned_data.get('password1')
#             print(raw_password)
#             user = authenticate(username=username, password=raw_password)  # 사용자 인증
#             login(request, user)  # 로그인
#             return redirect('index')
#     else:
#         form = UserCreationForm()
#
#     return render(request, 'common/signup.html', {'form': form})

def signup(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You are already authenticated as " + str(user.email))

    context = {}
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email = email , password = raw_password)
            login(request, account)
            return redirect('index')
        else:
            context["usercreation_form"] = form
    else:
        form = UserCreationForm()
        context["usercreation_form"] = form
    return render(request, 'common/signup.html', context)