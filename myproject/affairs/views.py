# from urllib import request
from django.shortcuts import render
from .models import myuser, students, Track
from .forms import Loginform, insertstudentForm, updatestudentForm, updatestudentForm2
from django.views.generic import ListView, CreateView

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import myuser
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.contrib.auth import authenticate, login, logout


def register(req):
    if(req.method == 'GET'):
        return render(req, 'register.html')
    else:
        print(req.POST)
        myuser.objects.create(
            name=req.POST['username'], password=req.POST['password'])
        return HttpResponseRedirect('/login')

        # students = myuser.objects.all()
        # redirect to login view
        # return render(req, 'login.html', context)
        # return redirect('/login', {'users': user})


def login(request):
    context = {}
    if(request.method == 'GET'):

        return render(request, 'login.html', context)
    else:

        username = request.POST['username']
        password = request.POST['password']

        user = myuser.objects.filter(username=username, password=password)

        user = authenticate(username=username, password=password)
        user = request.session['username'] = username
        if(user is not None and user is not None):
            request.session['username'] = username
            login(request, user)
            return render(request, 'home.html', context)
        else:
            context['errormsg'] = 'invlaid'
            return render(request, 'login.html', context)


def home(request):
    context = {}
    context['users'] = myuser.objects.all()
    return render(request, 'home.html', context)


def insert(request):
    if (request.method == 'GET'):
        return render(request, 'login.html')
    else:
        myuser.objects.create(
            name=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        user = myuser.objects.all()
        return redirect('/home', {'users': user})


def delete(request, id):
    data = myuser.objects.get(id=id)
    # if request.method == "POST":
    data.delete()
    return redirect('/login')


def update(request, id):
    data = myuser.objects.get(id=id)

    if request.method == "POST":

        data.email = request.POST.get('email')
        data.password = request.POST.get('password')
        data.save()
        return redirect("/login")
    else:

        return render(request, 'Register.html', {'users': data})


def search(request):
    if (request.method == 'GET'):
        return render(request, 'home.html')
    else:
        name = request.POST['username']
        context = {}
        context['studs'] = students.objects.filter(name__icontains=name)
        return render(request, 'search.html', context)


def mylogout(request):
    request.session['username'] = None
    return redirect('/login')


class myuserList(ListView):
    model = myuser


class trackList(ListView):
    model = Track


def selectAll(request):
    context = {}
    context['studs'] = students.objects.all()
    return render(request, 'selectAll.html', context)
