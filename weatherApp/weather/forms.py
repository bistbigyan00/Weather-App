from django import forms
from django.forms import TextInput
from .models import *

class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ['name']
        widgets = {'name':TextInput(attrs={'class':'input','placeholder':'City Name'})}
