from django.shortcuts import render, redirect
from .forms import WeatherForm
from .models import WeatherData
from credentials import *
from datetime import datetime
import urllib.request
import requests
import json





def weather(request):
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            city, current_weather, hourly_forecast = form.get_weather_data()
            context = {'city': city, 'current_weather': current_weather, 'hourly_forecast': hourly_forecast}
            return render(request, 'website/weather.html', context)
    else:
        form = WeatherForm()
    return render(request, 'website/search.html', {'form': form})

def store_weather_data(request):
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            temperature = form.cleaned_data['temperature']
            feels_like = form.cleaned_data['feels_like']
            humidity = form.cleaned_data['humidity']
            weather_data = WeatherData(city=city, temperature=temperature, feels_like=feels_like, humidity=humidity)
            weather_data.save()
            return redirect(weather_history)
    return redirect(weather)

def weather_history(request):
    data = WeatherData.objects.all()
    context = {'data': data}
    return render(request, 'website/weather_history.html', context)


