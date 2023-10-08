from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from .models import Water
import requests

# Create your views here.
default_name = "sabarmati"
default_location = "ahmedabad"




def index(request):
    try:
        if request.method == "POST":
            name = request.POST["name"]
            location = request.POST["location"]
        else:
            name = request.GET["name"]
            location = request.GET["location"]
    except:
        name = default_name
        location = default_location
    river = get_object_or_404(Water,name=name,location=location)
    coord = str(river.location_url).split("@")[1].split(",")[:2]
    try:
        current_data = requests.get(f"http://api.weatherapi.com/v1/current.json?key=147bf9a6406546ac816183831230610&q={coord[0]},{coord[1]}&aqi=yes").json()["current"]
        temp = current_data["temp_c"]
        cond = current_data["condition"]["text"]
        wind = current_data["wind_kph"]
        wind_dir = current_data["wind_dir"]
        windspeed = str(wind) + " kmph " + str(wind_dir)
        print(windspeed)
    except Exception as e:
        print(e)
        temp = "--"
        cond = "--"
        windspeed = "--"
    try:
        aqi = requests.get(
            f"http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={coord[0]}&lon={coord[1]}&appid=545111624d624d6594ab346c91ce8543").json()
        # print(aqi)
        aqi = aqi["list"][0]["main"]["aqi"]
    except Exception as e:
        print(e)
        aqi = "--"



    water_quality = ""
    lines = []
    if river.line1: lines.append(river.line1)
    if river.line2: lines.append(river.line2)
    if river.line3: lines.append(river.line3)
    activities = [*river.activities.all()]
    act = ", ".join(map(lambda x:x.name,activities))

    print(act)
    species = [*river.species.all()]
    species = ", ".join(map(lambda x:x.name,species))

    return render(request,
                  "nasa1.html",
                  context={
                      "river": river,
                      # "dissolved_oxygen":river.dissolved_oxygen,
                      # "faceal_content":river.faceal_content,
                      # "metal_content":river.metal_content,
                      "species": species,
                      "temp": temp,
                      "windspeed": windspeed,
                      "condition": cond,
                      "aqi": aqi,
                      "warning": river.warning,
                      "lines": lines,
                      "activities": act
                  })

def search(request):
    return render(request,"filter.html", context={"rivers":Water.objects.all()})
def report(request):
    return HttpResponse("Hello")

# ROMX
