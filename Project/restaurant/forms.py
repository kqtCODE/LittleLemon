from django.forms import ModelForm
from .models import Booking
from django.contrib.auth import models
from django import forms


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"