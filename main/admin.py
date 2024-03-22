from django.contrib import admin
from .models import Place, TypePlace, Star, Hotel, Geo, Chill,Chill_Type,Price_Type,Event,Event_type, Geo_type, Date_type, Beach, BeachType, BeachGeo, BeachCost, TypeGeoRest, TypeKitchen, TypesRests, Restaurant
# Register your models here.

admin.site.register(Place)
admin.site.register(TypePlace)
admin.site.register(Star)
admin.site.register(Geo)
admin.site.register(Chill)
admin.site.register(Chill_Type)
admin.site.register(Price_Type)
admin.site.register(Event)
admin.site.register(Event_type)
admin.site.register(Geo_type)
admin.site.register(Date_type)
admin.site.register(Hotel)
admin.site.register(BeachType)
admin.site.register(BeachGeo)
admin.site.register(Beach)
admin.site.register(BeachCost)
admin.site.register(TypesRests)
admin.site.register(TypeKitchen)
admin.site.register(Restaurant)
admin.site.register(TypeGeoRest)