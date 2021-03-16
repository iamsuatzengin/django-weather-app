from django.shortcuts import render
import urllib.request
import json

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=< your_api_key >').read()
        api = json.loads(api_url)

        data = {
            'city': city, 
            'description': api['weather'][0]['description'],
            'temp': api['main']['temp'],
            'feels_like': api['main']['feels_like'],
            'temp_min': api['main']['temp_min'],
            'temp_max': api['main']['temp_max'],
            'humidity': api['main']['humidity'],
            'wind_speed': api['wind']['speed'],
            'icon': api['weather'][0]['icon'],
        }
    else:
        city = None
        data = {}

    return render(request, 'index.html', {'data': data, 'city': city})