from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import LoginForm, RegisterForm
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication,  TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token

User = get_user_model()

def signup_view(request):
    error = None
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('restaurant:book')
            except IntegrityError:
                error = 'Username already exists'
            except:
                print(request, user)
                error = 'Something went wrong'
        else:
            error = 'Passwords do not match'
    form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'error': error})

@api_view(['GET','POST'])
def login_view(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        un = request.POST['username']
        pw = request.POST['password']
        user = authenticate(username=un, password=pw)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user = user)
            response = HttpResponse("hello")
            response.set_cookie('token', token)
            return redirect('restaurant:book')
        else:
            error = "Invalid username or password."
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'error': error})

def logout_view(request):
    logout(request)
    return redirect('restaurant:home')