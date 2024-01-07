from django.shortcuts import render
from .models import Place, TypePlace, Star, Hotel, Geo, Chill, Chill_Type, Price_Type

def index(request):
    return render(request, 'index.html')

def wist(request):
    places = Place.objects.all()
    stars = Star.objects.all()
    hotels = stars = Hotel.objects.all()
    geo = Geo.objects.all()
    return render(request, 'wist.html', {'places':places, 'stars': stars,'hotels':hotels ,'geo':geo})


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