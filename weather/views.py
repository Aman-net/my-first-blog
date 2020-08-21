import requests
from django.shortcuts import render
from .models import City
from .forms import Cityform
from django.shortcuts import redirect


# Create your views here.


def show_weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    if request.method == "POST":
        form = Cityform(request.POST)
        form.save()

    form = Cityform()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r["main"]["temp"],
            'description': r["weather"][0]["description"],
            'icon': r["weather"][0]["icon"],
        }
        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/index.html', context)


def fb(request):
    return redirect("www.facebook.com/aman.soni.iitian")


def ig(request):
    return redirect("www.instagram.com/aman__soni_a.s")
