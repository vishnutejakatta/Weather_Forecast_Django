from django.shortcuts import render
import requests
# Create your views here.
API_KEY = '9de0e659fe8aea0f8c0c6d48abdbec4d'


def get_zipcode_weather(request):
    try:
        if request.method == 'POST':
            country_name = request.POST['country_name']
            zip_code = request.POST['zipcode']
            url = 'http://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}&units=metric'.format(zip_code, country_name, API_KEY)
            data = requests.get(url).json()
            area = data['name']
            temperature = data['main']['temp']
            description = data['weather'][0]['description'].title()
            wind_speed = data['wind']['speed']
            icon = data['weather'][0]['icon']
            cloudiness = data['clouds']['all']
            return render(request, 'City/result.html', {
                'temperature': temperature,
                'description': description,
                'area': area,
                'wind_speed': wind_speed,
                'icon': icon,
                'cloudiness': cloudiness,
            })
    except:
        return render(request, 'HomeSite/404.html')
    return render(request, 'ZipCode/zipcode_form.html')
