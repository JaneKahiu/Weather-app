from django.shortcuts import render
import json #load json data to python dictionary
import urllib.request # request to make a request to the api
from django.conf import settings

# Create your views here.

def get_weather_data(city, country_code=None):
    api_key = 'be51f1e44ba55365d037fdbea046bd65'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
   
    # Construct the URL with city and optional country code
    if country_code:
        url = f'{base_url}?q={city},{country_code}&appid={api_key}&units=metric'
    else:
        url = f'{base_url}?q={city}&appid={api_key}&units=metric'
    #fetch data
    try:
        response = urllib.request.urlopen(url).read()
        weather_data = json.loads(response)
        return weather_data
    except urllib.error.HTTPError as e:
        return None # handle error eg city not found
def weather_view(request):
    city = request.GET.get('city')    
    country_code =request.GET.get('country_code')


    if city:
        weather_data = get_weather_data(city, country_code)
        if weather_data:
            context = {
                'city': city,
                'country_code': country_code,
                'weather_data': weather_data
            }
        else:
            context = {
                'error': "City not found. Please enter a valid city and country code."
            }
    else:
        context = {
            'error': "Please enter a city name and optionally a country code to get the weather information."
        }

    return render(request, 'weather.html', context)
    


