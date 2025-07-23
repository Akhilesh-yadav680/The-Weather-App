import requests
from django.shortcuts import render

def weather_view(request):
    weather_data = None

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'Your api key'  # Replace with your actual API key
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': city.title(),
                'description': data['weather'][0]['description'].title(),
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
            }
        else:
            weather_data = {'error': 'City not found'}

    return render(request, 'weather_app/index.html', {'weather_data': weather_data})
