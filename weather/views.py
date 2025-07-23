# views.py
import requests
from django.shortcuts import render

def home(request):
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'Your API  Key'  # Replace with your actual API key
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather_data = {
                    'city': city,
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon']
                }
            else:
                error_message = data.get('message', 'City not found.')
        except requests.exceptions.RequestException:
            error_message = 'Could not connect to the weather service.'

    return render(request, 'home.html', {
        'weather': weather_data,
        'error': error_message
    })
