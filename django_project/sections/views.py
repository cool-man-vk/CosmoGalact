from time import strftime
from django.shortcuts import render
from django.http import HttpResponse
import json
import requests 
from datetime import timedelta
from datetime import datetime
from pprint import pprint

# Create your views here.
def homeview(request):
    return render(request,"sections/navbar.html") 

def asteriod_data(request):
    if request.method == 'POST':
        start_date = request.POST['start_date']
        now = datetime.now()
        end_date = now.strftime("%Y-%m-%d")
        api_key = "V6jh1xQFJTFuBwbwhkSt2peSp3knqipCy2c31PgQ"
        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}"
        r = requests.get(url) 
        data = r.json()
        neo = data['near_earth_objects']
        for asteriods in neo[start_date]:
                name = asteriods['name']
                id = asteriods['id']
                nasa_url = asteriods['nasa_jpl_url']
                
        print(name)
        
        # for asteroid in all_asteriods:
        #     if asteriod['is_potentially_hazardous_asteroid']:
        #         is_pha = asteriods['is_potentially_hazardous_asteroid']
        #         break 

        # for asteroid in all_asteriods:
        #     if asteriod['absolute_magnitude_h']:
        #         luminosity = asteriods['absolute_magnitude_h']
        #         break 
        
        # for asteroid in all_asteriods:
        #     if asteriod['absolute_magnitude_h']:
        #         luminosity = asteriods['absolute_magnitude_h']
        #         break 
        context = {
                'astInfo' : asteriods ,
                'asteriod_name' : name ,
                'asteroid_id' : id ,
                'asteroid_url' : nasa_url ,
                # 'isPha' : is_pha ,
                # 'luminosity': luminosity 
        }
        return render(request,"sections/asteriods.html",context) 
    else: 
        return render(request,"sections/asteriods.html")
