from django.urls import path, include
from website import views

urlpatterns = [
    path('', views.weather, name="search" ),
    # path('weather/', views.weather_result, name="weather" ),
    path('store_weather_data/', views.store_weather_data, name="store_weather_data" ),
    path('weather-history/', views.weather_history, name='weather_history'),
]
