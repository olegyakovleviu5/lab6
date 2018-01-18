from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic import ListView
from requests import request
from .models import  *
from django import forms
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def Main(request):
    par = {
        'header': 'Main page'
    }
    return render(request, 'MainPage.html', context=par)


class UserView(ListView):
    model = User_1
    template_name = 'User_list.html'
    context_object_name = 'User_list'


class TeamView(ListView):
    model = Team
    template_name = 'Team_list.html'
    context_object_name = 'Team_list'

class BetView(ListView):
    model = Bet
    template_name = 'Bet_list.html'
    context_object_name = 'Bet_list'


def User_registered(request):
    return render(request, 'registered.html')

def No_such_user(request):
    return render(request, 'nouser.html')


class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=5, label='Логин')
    password = forms.CharField(min_length=6, widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(min_length=6, widget=forms.PasswordInput, label='Повторите ввод')
    last_name = forms.CharField(label='Фамилия')
    first_name = forms.CharField(label='Имя')
    email = forms.EmailField(label='Email')
#
# def registration(request):
#     if request.method=='POST':
#         form = RegistrationForm(request.POST)
#         d=form.cleaned_data
#         if not form.is_valid():
#             if
#         elif form.is_valid():
#             return HttpResponseRedirect('/login')
#     else:
#         form = RegistrationForm()
#     return render(request, 'registration.html', {'form': form})



def registration_form(request):
    errors=[]
    # request.encoding = 'utf-8'
    if request.method=='POST':
        last_name = request.POST.get('last_name')
        if not last_name:
            errors.append('Введите Фамилию')

        first_name = request.POST.get('first_name')
        if not first_name:
            errors.append('Введите имя')

        Email = request.POST.get('Email')
        if not Email:
            errors.append('Введите Email')

        username=request.POST.get('username')
        if not username:
            errors.append('Введите логин')
        elif len(username) < 8:
            errors.append('Логин должен превышать 5 символов')
        if User.objects.filter(username=username).exists():
            errors.append('Данный логин занят')
        #
        password = request.POST.get('password')
        if not password:
            errors.append('Введите пароль')
        elif len(password) < 8:
            errors.append('Длина пароля должна превышать 6 символов')
        password_repeat = request.POST.get('password2')
        if password != password_repeat:
            errors.append('Пароли должны совпадать')

        if not errors:
            User.objects.create_user(username, Email, password)
            return HttpResponseRedirect('/registered')
    return render(request, 'registration.html',{'errors': errors})


class AuthForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

def Auth(request):
    errors = []
    if request.method=='POST':
        form = AuthForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/loggedin')
        else:
             errors.append("Нет такого пользователя")
    else:
        form = AuthForm()
    return render(request, 'UserLogin.html', {'errors': errors})


def logout_view(request):
    logout(request)
    return render(request, 'MainPage.html')

def loggedin_view(request):
    logout(request)
    return render(request, 'loggedin.html')
