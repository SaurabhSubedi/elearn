from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.db import IntegrityError
from django.contrib import messages


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')

    else:
        return redirect('login')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        result = authenticate(username=username, password=password)
        print(result)
        if result is not None:
            login(request, result)
            return redirect('home')
        else:
            messages.warning(request,"Please enter valid credentials")

    return render(request, 'login.html')


def signupUser(request):

    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            usersinfo = User.objects.all()
            for obj in usersinfo:
                if (obj.username == username):
                    messages.warning(request,"Username already exists")
                    return redirect('signup')
                elif (obj.email == email):
                    messages.warning(request,"Email already exists")
                    return redirect('signup')
                elif (password1 != password2):
                    messages.warning(request,"Passwords didnot match")
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    return redirect('login')

    except IntegrityError:
        return redirect('signup')


    return render(request, 'signup.html')


def logoutUser(request):
    logout(request)
    return redirect('login')

