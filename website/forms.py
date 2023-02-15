from django import forms
import requests
from credentials import *


class WeatherForm(forms.Form):
    # coordinates = forms.CharField(label='Enter Latitude and Longitude', max_length=50)
    coordinates = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Latitude, Longitude'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['coordinates'].widget.attrs.update({'class': 'search-bar'})
    
    def get_weather_data(self):
        coordinates = self.cleaned_data['coordinates']
        lat, lon = coordinates.split(',')
        # Mapbox API 
        mapbox_access_token = MAPBOXKEY
        mapbox_url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{lon},{lat}.json?access_token={mapbox_access_token}'
        mapbox_response = requests.get(mapbox_url)
        mapbox_data = mapbox_response.json()
        city = mapbox_data['features'][0]['place_name']
        
        #OpenWeatherMap API 
        owm_access_token = OPENAPIKEY
        owm_url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,daily&units=metric&appid={owm_access_token}'
        owm_response = requests.get(owm_url)
        
        owm_data = owm_response.json()
        current_weather = owm_data['current']
        hourly_forecast = owm_data['hourly'][:24]
        
        
        return city, current_weather, hourly_forecast
