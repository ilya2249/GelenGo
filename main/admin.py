from django.contrib import admin
from .models import Place, TypePlace, Star, Hotel, Geo, Chill,Chill_Type,Price_Type
# Register your models here.

admin.site.register(Place)
admin.site.register(TypePlace)
admin.site.register(Star)
admin.site.register(Hotel)
admin.site.register(Geo)
admin.site.register(Chill)
admin.site.register(Chill_Type)
admin.site.register(Price_Type)