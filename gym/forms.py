from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('bookingnumber', 'status',)
