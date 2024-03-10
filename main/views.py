from django.shortcuts import render
from .models import Place, TypePlace, Star, Hotel, Geo, Event, Chill, Chill_Type, Price_Type, Event_type, Geo_type, Date_type, Beach, BeachType, BeachGeo, BeachCost
from .parserEvents import parserEventsFunc
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
from typing import List, Any


def wist(request):
    places = Place.objects.all()
    stars = Star.objects.all()

    hotels = stars = Hotel.objects.all()
    geo = Geo.objects.all()
    return render(request, 'wist.html', {'places':places, 'stars': stars,'hotels':hotels ,'geo':geo})

def events(request):
    date_type = Date_type.objects.all()
    geo_type = Geo_type.objects.all()
    events = Event.objects.all()
    event_type = Event_type.objects.all()
    return render(request, 'events.html', {'events':events, 'geo_type': geo_type,'date_type':date_type ,'events_type':event_type})


def beaches(request):
    beaches = Beach.objects.all()
    beachType = BeachType.objects.all()
    beachGeo = BeachGeo.objects.all()
    beachCost = BeachCost.objects.all()
   
    
    return render(request, 'beaches.html', {'beaches':beaches, 'beachType': beachType,'beachGeo':beachGeo,'beachCost':beachCost})

def chill(request):
    chills = Chill.objects.all()
    chill_type = Chill_Type.objects.all()
    price_type = Price_Type.objects.all()
    
    return render(request, 'chill.html', {'chills':chills, 'chill_type':chill_type,'price_type':price_type})
def exc(request):

    return render(request, 'exc.html', {})
def facts_panel(request):

    return render(request, 'facts_panel.html', {})
def top_panel(request):

    return render(request, 'top_panel.html', {})

# def save_hotels_to_database(request):
#         for hotel_data in hotelsParsedData:
#                 stars, created = Star.objects.get_or_create(code=hotel_data['codeStars'], defaults={'name': hotel_data['stars']})
#                 geoType, created = Geo.objects.get_or_create(code=hotel_data['codeGeoType'], defaults={'name': hotel_data['geo']})
                
#                 hotelTemp, created = Hotel.objects.get_or_create(code=hotel_data['code'], defaults={'name': hotel_data['typePlace']})

#                 Place.objects.create(name=hotel_data['name'], img = hotel_data['img'],star = stars, geolocation = hotel_data['geolocation'],distance = hotel_data['distance'],hotel = hotelTemp, geo = geoType)
#         return HttpResponse()    
eventsParsedData = parserEventsFunc()
def save_events_to_database(request):
    for event in eventsParsedData:
            date_type, created = Date_type.objects.get_or_create(code=event['time'], defaults={'name': event['time']})
            geo_type, created = Geo_type.objects.get_or_create(code=event['placeType'], defaults={'name': event['place']})
            global_type,created = Event_type.objects.get_or_create(code = event['globalType'], defaults={'name': event['globalType']})
            Event.objects.create(name=event['title'], img = event['img'],typeE = event['type'],date_type = date_type , dateEvent = event['date'],event_type = global_type, Geo = geo_type)
    return HttpResponse()    
     
       


