"""untitled8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import loggedin_view,logout_view,No_such_user,Auth,Main,User_registered, UserView,TeamView,BetView,registration_form

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', Main ),
    url(r'^users$', UserView.as_view(), name='users'),
    url(r'^teams$', TeamView.as_view(), name='teams'),
    url(r'^bets$', BetView.as_view(), name='bets'),
    url(r'^registration$', registration_form, name='registration'),
    url(r'^registered$', User_registered, name='registered'),
    url(r'^ulogin$', Auth, name='ulogin'),
    url(r'^nouser$', No_such_user, name='nouser'),
    url(r'^logout$', logout_view, name='logout'),
    url(r'^loggedin$', loggedin_view, name='loggedin'),
   # url('^', include('django.contrib.auth.urls'))
]
