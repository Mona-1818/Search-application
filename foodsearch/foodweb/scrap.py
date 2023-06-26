import csv 
import json
import urllib.request 
from django.core.management.base import BaseCommand  
from .models import menus, resturants

class Command(BaseCommand):
    def handle(self, *args, **options):
        url = 'https://python-exercise.s3.ap-south-1.amazonaws.com/restaurants_small.csv'
        response = urllib.request.urlopen(url)
        reader = csv.reader(response.read().decode('utf-8').splitlines()) 
    
        for i in reader:  
            if i[0] == "id":
                continue 
            else:
                y = i[4].split(",")
                resturants.objects.create(hotel_id= i[0], hotel_name=i[1], hotel_location=i[2], hotel_langitude=y[0], hotel_longitude=y[1]) 

                    
                try:
                    x = json.loads(i[3]) 
                    for j, k in x.items():
                        hotel = resturants.objects.get( hotel_id= i[0])
                        menus.objects.create(hotel_id= hotel, food= j, price= k)
                        
                except json.JSONDecodeError as e: 
                    continue