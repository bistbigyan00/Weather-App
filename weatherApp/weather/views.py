from django.shortcuts import render,redirect
from .forms import *
from .models import *

import requests

# Create your views here.
def index(request):
    #predefined app-key from imap
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=cf47a004699b5fb89aa01ae3a1969503"

    #save the form
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            #cleaned_data is data which has passed valid test from above
            new_city = form.cleaned_data['name']
            r = requests.get(url.format(new_city)).json()
            #r['cod'] is predefined code for valid cities
            if r['cod'] == 200:
                form.save()

    #send always empty form to the page even after saving
    form = CityForm()

    #grab all the cities to display the weather
    cities = City.objects.all().order_by('-id')

    #grab the weather details of all cities so that we can show
    #make an empty list and store all city weather
    cities_weather = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        cities_weather.append(city_weather)


    context = {'cities_weather':cities_weather,'form':form}
    return render(request,'weather/weather.html',context)

def delete_city(request,pk):
    city = City.objects.get(id=pk)
    city.delete()
    return redirect('/')
