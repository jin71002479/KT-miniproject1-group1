from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from config.settings import LOGIN_URL
from .models import User
from django.contrib.auth.decorators import login_required #로그인여부


def login_view(request):
    if request.method == "POST" :
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('main:index')
    return render(request, "userapp/login.html")

def login2_view(request):
    if request.method == "POST" :
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('main:index2')
    return render(request, "userapp/login2.html")



def logout_view(request):
    logout(request)
    return redirect("userapp:login")

def logout2_view(request):
    logout(request)
    return redirect("userapp:login2")
 


def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        fullname = request.POST["fullname"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        score  = request.POST["score"]

        user = User.objects.create_user(username,email,password)
        user.fullname = fullname
        user.phone= phone
        user.score = score
        user.save()

        return redirect("userapp:login")

    return render(request, "userapp/singup.html")


def signup2_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        fullname = request.POST["fullname"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        score  = request.POST["score"]

        user = User.objects.create_user(username,email,password)
        user.fullname = fullname
        user.phone= phone
        user.score = score
        user.save()

        return redirect("userapp:login2")

    return render(request, "userapp/singup2.html")    