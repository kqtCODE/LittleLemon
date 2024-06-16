# from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, get_user_model
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action
from .forms import BookingForm
from .models import Menu, Booking
from .serializer import BookingSerializer
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from django.core import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import status
from django.core.exceptions import PermissionDenied

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

class BookingListView(ModelViewSet):  
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    template_name = 'bookings.html'

    def list(self, request) -> HttpResponse:
        print (request.user.is_authenticated)
        queryset = Booking.objects.all()
        serializer = BookingSerializer(queryset, many=True)
        if serializer.data:
            return render(request, 'bookings.html', {"bookings_list": serializer.data}) 
        else:
            raise PermissionDenied

# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

@csrf_exempt
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)
