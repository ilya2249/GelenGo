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
    path('save_data_events/', save_events_to_database, name='save_data_events')
 ]
