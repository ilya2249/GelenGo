from django.contrib import admin
from django.urls import path
from main import views
#from .views import save_hotels_to_database
from .views import save_events_to_database
urlpatterns = [
    path('', views.index, name='index'),
    path('wist', views.wist, name='wist'),
    path('chill', views.chill, name='chill'),
    path('exc', views.exc, name='exc'),
    path('facts_panel', views.facts_panel, name='facts_panel'),
    path('top_panel', views.top_panel, name='top_panel'),
    path('events', views.events, name='events'),
    path('beaches', views.beaches, name='beaches'),
#   path('save_data/', save_hotels_to_database, name='save_data'),
    path('save_data_events/', save_events_to_database, name='save_data_events'),
     path('excursions_faraon', views.excursions_faraon, name='excursions_faraon'),
     path('excursions_dolmens', views.excursions_dolmens, name='excursions_dolmens'),
     path('excursions_jeep', views.excursions_jeep, name='excursions_jeep'),
     path('excursions_safaripark', views.excursions_safaripark, name='excursions_safaripark'),
      path('excursions_aquaparks', views.excursions_aquaparks, name='excursions_aquaparks'),
       path('excursions_abrau_durso', views.excursions_abrau_durso, name='excursions_abrau_durso'),
        path('excursions_skala_parus', views.excursions_skala_parus, name='excursions_skala_parus'),
        path('excursions_diving', views.excursions_diving, name='excursions_diving'),
        path('excursions_olimp', views.excursions_olimp, name='excursions_olimp'),
      path('generate_excursion/', views.generate_excursion, name='generate_excursion')
      
 ]
