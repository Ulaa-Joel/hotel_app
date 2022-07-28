from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Post

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already In Use')
                return redirect('')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already In Use')
                return redirect('')
            elif User.objects.filter(phonenumber=phonenumber).exists():
                messages.info(request, 'Mobile Number Already In Use')
                return redirect('')
            else:
                user = User.objects.create_user(username=username, email=email, phonenumber=phonenumber, password=password)
                user.save();
                return render(request, 'book.html',{})
        else:
            messages.info(request, 'Password not the same.')
            return redirect('')
    else:
        return render(request, 'index.html',{})

def base(request):
    return render(request, 'base.html',{})

def book(request):
    posts = Post.objects.all()
    return render(request, 'book.html', {'posts': posts})
