from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from . import models
from Manager import models
from Manager import forms
import datetime


# Create your views here.
def login(request):
    if request.session.get('is_login', None):
        return redirect("/index/")
    form = forms.UserLogin()
    if request.method == "GET":
        return render(request, "login.html", {"form": form})
    else:
        form = forms.UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data["users"]
            passwd = form.cleaned_data["passwd"]
            chkuser = models.UserAgent.objects.filter(username=username, passwd=passwd)
            if chkuser:
                request.session['is_login'] = True
                request.session['user_name'] = username
                login_info = "登陆成功"
                return render(request, "index.html", {"msg": datetime.datetime.now(), "login_info": login_info})
            else:
                msg = "用户名或密码错误"
                return render(request, "login.html", {"form": form, "msg": msg})
        else:
            msg = "用户名或密码不符合规范"
            return render(request, "login.html", {"form": form, "msg": msg})


def index(request):
    time = datetime.datetime.now()
    return render(request, 'index.html', {"msg": time})


def logout(request):
    request.session.flush()
    return redirect("/index/")


def register(request):
    form = forms.UserReg()
    if request.method == "GET":
        return render(request, "register.html", {"form": form})
    else:
        form = forms.UserReg(request.POST)
        if form.is_valid():
            username = form.cleaned_data["users"]
            passwd1 = form.cleaned_data["passwd"]
            passwd2 = form.cleaned_data["passwdconfirm"]
            email = form.cleaned_data["email"]
            if models.UserAgent.objects.filter(email = email):
                return render(request, "register.html", {"form": form, "error_msg": "邮箱已被注册"})
            if models.UserAgent.objects.filter(username = username):
                return render(request, "register.html", {"form": form, "error_msg": "用户名已被注册"})
            if passwd1 == passwd2:
                new_user = models.UserAgent.objects.create()
                new_user.username = username
                new_user.passwd = passwd1
                new_user.email = email
                new_user.save()
                return render(request, "register.html", {"form": form})
            else:
                return render(request, "register.html", {"form": form, "error_msg": "两次密码输入不一致"})
        else:
            return render(request, "register.html", {"form": form, "error_msg": "信息输入错误"})

def addEvent(request):
    form =forms.AddData()
    if not request.session.get('is_login',None):
        return render(request,"addEvent.html",{"error_msg":"您未登录，无权进行此操作!","is_login":False})
    else:
        return render(request,"addEvent.html",{"is_login":True,"form":form})
