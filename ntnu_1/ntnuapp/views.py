from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from ntnuapp.models import AP
from nynuapp.serializers import APSerializer
from rest_framework import viewsets

class APViewSet(viewsets.ModelViewSet):
    queryset = AP.objects.all()
    serializer_class = APSerializer

    

def index(request):
	if request.user.is_authenticated:
	   name=request.user.username
	elif request.method == 'POST':
                
                name = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(username=name, password=password)
                if user is not None:
                        if user.is_active:
                                auth.login(request,user)
                                return redirect('/index/')
                                message = '登入成功！'
                        else:
                                message = '帳號尚未啟用！'
                else:
                        message = '登入失敗！'
	return render(request, "index.html", locals())
	
def logout(request):
	auth.logout(request)
	return redirect('/index/')

def dashboard(request):
        if request.user.is_authenticated:
                name=request.user.username
        else:
                return redirect('/index/')
        return render(request, "dashboard.html", locals())
def ap(request):
        if request.user.is_authenticated:
                name=request.user.username
        else:
                return redirect('/index/')
        return render(request, "ap.html", locals())
def users(request):
        if request.user.is_authenticated:
                name=request.user.username
        else:
                return redirect('/index/')
        return render(request, "users.html", locals())
def message(request):
        if request.user.is_authenticated:
                name=request.user.username
        else:
                return redirect('/index/')
        return render(request, "message.html", locals())
def system(request):
        if request.user.is_authenticated:
                name=request.user.username
        else:
                return redirect('/index/')
        return render(request, "system.html", locals())
