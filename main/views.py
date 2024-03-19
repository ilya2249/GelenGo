from django.shortcuts import render
from .models import Place, TypePlace, Star, Hotel, Geo, Event, Chill, Chill_Type, Price_Type, Event_type, Geo_type, Date_type, Beach, BeachType, BeachGeo, BeachCost
from .parserEvents import parserEventsFunc
from django.http import HttpResponse
from django.http import JsonResponse
from .neuralNetwork import excursion_neural_network_func
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
def excursions_faraon(request):

    return render(request, 'excursions_faraon.html', {})
def excursions_diving(request):

    return render(request, 'excursions_diving.html', {})
def excursions_skala_parus(request):

    return render(request, 'excursions_skala_parus.html', {})
def excursions_abrau_durso(request):

    return render(request, 'excursions_abrau_durso.html', {})
def excursions_dolmens(request):
    return render(request, 'excursions_dolmens.html', {})
def excursions_jeep(request):

    return render(request, 'excursions_jeep.html', {})
def excursions_aquaparks(request):

    return render(request, 'excursions_aquaparks.html', {})
def excursions_olimp(request):

    return render(request, 'excursions_olimp.html', {})
def excursions_safaripark(request):

    return render(request, 'excursions_safaripark.html', {})
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

restaurants = [
    {
        'title': 'Château de Talu',
        'img': 'https://img02.rl0.ru/afisha/1064x1064i/s2.afisha.ru/mediastorage/84/3e/086bcaa607ba42f3a6f19fee3e84.jpg',
        'kitchenType': 'Французская кухня',
        'restType': 'Ресторан',
        'geo': 'Фадеева, 52а',
        'opentill': 'Открыто до 23:00'
    },
    {
        'title': 'Club House',
        'img': 'https://img02.rl0.ru/afisha/1064x1064i/s4.afisha.ru/mediastorage/82/44/e72b4897ad084ad0ab89cce04482.jpg',
        'kitchenType': 'Ресторан',
        'restType': 'Ресторан',
        'geo': 'Стартовая, 1',
        'opentill': 'Открыто до 23:00'
    },
    {
        'title': 'Edison',
        'img': 'https://img04.rl0.ru/afisha/1064x1064i/s.afisha.ru/mediastorage/87/d4/406554e7968547398b6aada2d487.jpg',
        'kitchenType': '',
        'restType': 'Гастропабы',
        'geo': 'Красногвардейская, 36а',
        'opentill': 'Открыто до 23:00'
    },
    {
        'title': 'La bottega',
        'img': 'https://img04.rl0.ru/afisha/1064x1064i/s2.afisha.ru/mediastorage/b4/a9/cf2ecedb34704b65a1b7d0a4a9b4.jpg',
        'kitchenType': '',
        'restType': 'Кафе',
        'geo': 'Ленина, 5',
        'opentill': 'Открыто до 22:00'
    },
    {
        'title': 'Portofino',
        'img': 'https://img04.rl0.ru/afisha/1064x1064i/s2.afisha.ru/mediastorage/ff/e6/2715d08451fe42879b650225e6ff.jpg',
        'kitchenType': 'Итальянская кухня',
        'restType': 'Ресторан',
        'geo': 'Халтурина, 30, литера 2',
        'opentill': 'Открыто до 23:00'
    },
    {
        'title': 'Rony Oyster',
        'img': 'https://img03.rl0.ru/afisha/1064x1064i/s1.afisha.ru/mediastorage/c7/d2/0dab3be8f9244faba70f9cb5d2c7.jpg',
        'kitchenType': 'Рыбные рестораны',
        'restType': 'Ресторан',
        'geo': 'Лермонтовский б-р, 18',
        'opentill': 'Открыто до 23:00'
    },
    {
        'title': 'Sky Bar Атмосфера',
        'img': 'https://img04.rl0.ru/afisha/1064x1064i/s5.afisha.ru/mediastorage/f9/19/f7bf054357d94b61a8af5ef619f9.jpg',
        'kitchenType': '',
        'restType': 'Бары',
        'geo': 'Шмидта, 1, отель «Атмосфера», 4 этаж',
        'opentill': 'Открыто до 00:00'
    },
    {
        'title': 'Subway',
        'img': 'https://img04.rl0.ru/afisha/1064x1064i/www.afisha.ru/uploads/images/e/5d/e5d86af70ea54259a2b3747a5f028e55.jpg',
        'kitchenType': '',
        'restType': 'Фастфуд',
        'geo': 'Первомайская, 6',
        'opentill': 'Открыто до 23:00'
    },
    {
        'title': 'Геленджик',
        'img': 'https://img03.rl0.ru/afisha/1064x1064i/s5.afisha.ru/mediastorage/a7/25/92cc81e026bb4026a5821cea25a7.jpg',
        'kitchenType': '',
        'restType': 'Кафе',
        'geo': 'Мира, 21, корп. 4',
        'opentill': 'Открыто до 00:00'
    },
    {
        'title': 'Горыныч',
        'img': 'https://img04.rl0.ru/afisha/1064x1064i/s1.afisha.ru/mediastorage/e4/39/bc6a7b74cc0d4dd4ad5c1e0d39e4.jpg',
        'kitchenType': 'Стейки',
        'restType': 'Ресторан',
        'geo': 'Революционная, 2/1',
        'opentill': 'Открыто до 23:00'
    },
    {
        'title': 'Дача',
        'img': 'https://img03.rl0.ru/afisha/1064x1064i/s5.afisha.ru/mediastorage/63/0b/1d0aef4b52c6458788b6b0330b63.jpg',
        'kitchenType': 'Ресторан',
        'restType': 'Ресторан',
        'geo': 'Херсонская, 9, гостиничный комплекс «Дача»',
        'opentill': 'Открыто до 00:00'
    },
    {
        'title': 'Джимми Чу',
        'img': 'https://img03.rl0.ru/afisha/1064x1064i/s4.afisha.ru/mediastorage/9c/d5/5521fd9dd84244b5865cbcead59c.jpg',
        'kitchenType': 'Паназиатская кухня',
        'restType': 'Ресторан',
        'geo': 'Крымская, 3, корп. 2',
        'opentill': 'Открыто до 23:00'
    },
    {
        'title': 'Долина Лефкадия',
        'img': 'https://img03.rl0.ru/afisha/1064x1064i/s2.afisha.ru/mediastorage/36/9e/7375d886a5034ac3b26440399e36.jpg',
        'kitchenType': '',
        'restType': 'Винотеки',
        'geo': 'Мира, 21, корп. 3',
        'opentill': 'Открыто до 00:00'
    },
    {
        'title': 'Доминго',
        'img': 'https://www.afisha.ru/_next/static/media/placeholder-with-logo-blue.b66f7037.png',
        'kitchenType': 'Ресторан',
        'restType': 'Ресторан',
        'geo': 'Халтурина, 11',
        'opentill': 'Открыто до 23:00'
    },
    {
        'title': 'ЗОЖ и провокация',
        'img': 'https://img03.rl0.ru/afisha/1064x1064i/s.afisha.ru/mediastorage/7a/4d/d3ba0bf1ac9045d3b22c6dd44d7a.jpg',
        'kitchenType': 'Здоровое питание',
        'restType': 'Ресторан',
        'geo': 'Мира, 23в',
        'opentill': 'Открыто до 21:00'
    },
    {
        'title': 'Краснодарский парень',
        'img': 'https://www.afisha.ru/_next/static/media/placeholder-with-logo-pink.7d298f3f.png',
        'kitchenType': 'Бургеры',
        'restType': 'Ресторан',
        'geo': 'Островского, 23',
        'opentill': 'Открыто до 22:00'
    },
    {
        'title': 'Лагуна',
        'img': 'https://img04.rl0.ru/afisha/1064x1064i/s.afisha.ru/mediastorage/cd/4a/bbf22fe7473f446bbdca60104acd.jpg',
        'kitchenType': 'Рестораны у воды',
        'restType': 'Ресторан',
        'geo': 'Лермонтовский б-р, 8а',
        'opentill': 'Открыто до 23:00'
    },
    {
        'title': 'Любокофе',
        'img': 'https://www.afisha.ru/_next/static/media/placeholder-with-logo-blue.b66f7037.png',
        'kitchenType': '',
        'restType': 'Кофейни',
        'geo': 'Ленина, 1',
        'opentill': 'Открыто до 23:00'
    },
    {
        'title': 'Маринад',
        'img': 'https://img02.rl0.ru/afisha/1064x1064i/s3.afisha.ru/mediastorage/20/4c/5753422266e1479db6474d9a4c20.jpg',
        'kitchenType': 'Ресторан',
        'restType': 'Ресторан',
        'geo': 'Шмидта, 1, отель «Атмосфера»',
        'opentill': 'Открыто до 00:00'
    },
    {
        'title': 'Маяк — Рассвет',
        'img': 'https://img04.rl0.ru/afisha/1064x1064i/s5.afisha.ru/mediastorage/30/50/3938d32ca3d5475f92d297695030.jpg',
        'kitchenType': '',
        'restType': 'Бары',
        'geo': 'Революционная, 48',
        'opentill': 'Открыто до 22:00'
    },
    {
        'title': 'Мистраль',
        'img': 'https://img02.rl0.ru/afisha/1064x1064i/s.afisha.ru/mediastorage/69/f8/6dc21f80160945809f2c263bf869.jpg',
        'kitchenType': 'Рестораны у воды',
        'restType': 'Ресторан',
        'geo': 'Революционная, 53, Metropol Grand Hotel Gelendzhik',
        'opentill': 'Открыто до 20:00'
    },
    {
        'title': 'Мясо и вино',
        'img': 'https://img01.rl0.ru/afisha/1064x1064i/s.afisha.ru/mediastorage/2c/d2/f33cc629c8734ffabea39fc4d22c.jpg',
        'kitchenType': 'Стейки',
        'restType': 'Ресторан',
        'geo': 'Революционная, 21а',
        'opentill': 'Открыто до 23:00'
    },
    {
        'title': 'На круче',
        'img': 'https://img02.rl0.ru/afisha/1064x1064i/www.afisha.ru/uploads/images/3/fd/3fd9de6fa9f54e8c8aff560856ecbb0d.jfif',
        'kitchenType': 'Рыбные рестораны',
        'restType': 'Ресторан',
        'geo': 'Черноморская наб., 8',
        'opentill': 'Открыто до 23:00'
    },
    {
        'title': 'На крыше',
        'img': 'https://img01.rl0.ru/afisha/1064x1064i/s4.afisha.ru/mediastorage/99/6f/7dedae8f89b44f61a1ec558c6f99.jpg',
        'kitchenType': '',
        'restType': 'Кафе',
        'geo': 'Горького, 8, 2 этаж',
        'opentill': 'Открыто до 00:00'
    },
    {
        'title': 'Петрович',
        'img': 'https://img02.rl0.ru/afisha/1064x1064i/www.afisha.ru/uploads/images/8/c8/8c861104d6eb41249498d70cbe61e32b.PNG',
        'kitchenType': '',
        'restType': 'Пабы',
        'geo': 'Витебская, 14/1',
        'opentill': 'Открыто до 23:00'
    },
    {
        'title': 'Причал 93',
        'img': 'https://img01.rl0.ru/afisha/1064x1064i/s5.afisha.ru/mediastorage/b1/ea/a7477b52d331486c80b17a27eab1.jpg',
        'kitchenType': 'Ресторан',
        'restType': 'Ресторан',
        'geo': 'Революционная, 47',
        'opentill': 'Открыто до 23:00'
    },
    {
        'title': 'Сицилия',
        'img': 'https://img03.rl0.ru/afisha/1064x1064i/www.afisha.ru/uploads/images/5/f9/5f982632717e4edba0d5bed638c4a16b.PNG',
        'kitchenType': 'Пицца',
        'restType': 'Ресторан',
        'geo': 'Крымская, 3, корп. 2',
        'opentill': 'Открыто до 23:00'
    },
    {
        'title': 'Табрис',
        'img': 'https://img03.rl0.ru/afisha/1064x1064i/s4.afisha.ru/mediastorage/b0/ae/512b3310f0a94fa18b81e9c5aeae.jpg',
        'kitchenType': 'Иранская кухня',
        'restType': 'Ресторан',
        'geo': 'Халтурина, 40',
        'opentill': 'Открыто до 23:00'
    },
    {
        'title': 'У Анны',
        'img': 'https://img01.rl0.ru/afisha/1064x1064i/s2.afisha.ru/mediastorage/9c/42/76b748b365e44362b32b3d6d9c42.jpg',
        'kitchenType': '',
        'restType': 'Кафе',
        'geo': 'Туапсинская, 41',
        'opentill': 'Открыто до 23:00'
    },
    {
        'title': 'Центральная улица',
        'img': 'https://img01.rl0.ru/afisha/1064x1064i/s2.afisha.ru/mediastorage/61/4c/66e8578c1f1445489dd7d4d8a4c6.jpg',
        'kitchenType': '',
        'restType': 'Кафе',
        'geo': 'Ленина, 2',
        'opentill': 'Открыто до 00:00'
    },
    {
        'title': 'Чайхана №1',
        'img': 'https://img03.rl0.ru/afisha/1064x1064i/s5.afisha.ru/mediastorage/28/6e/431c7f21ab9c46d7afbe20d46e28.jpg',
        'kitchenType': 'Узбекская кухня',
        'restType': 'Ресторан',
        'geo': 'Красногвардейская, 27',
        'opentill': 'Открыто до 23:00'
    }
]
def generate_excursion(request):
    if request.method == 'POST':
        value1 = request.POST.get('value1')
        value2 = request.POST.get('value2')
        value3 = request.POST.get('value3')
        value4 = request.POST.get('value4')

       

        excursion_url = excursion_neural_network_func(value1,value2,value3,value4)  # Пример URL страницы с экскурсией

        return JsonResponse({'excursion_url': excursion_url})
    else:
        return JsonResponse({'error': 'Метод запроса не поддерживается'})