from typing import List, Any
import sqlite3
from bs4 import BeautifulSoup
import requests
from .models import Hotel
sanatoriums = []
sanatoriums_geo = []
sanatoriums_distance = []
sanatoriums_stars = []

hotels = []
hotels_geo = []
hotels_distance = []
hotels_stars = []

apartments = []
apartments_geo = []
apartments_distance = []
apartments_stars = []
page = 1
hotelsParsedData = []


def split_string(s):
    num = ''
    unit = ''

    for char in s:
        if char.isdigit() or char == '.':
            num += char
        else:
            unit += char

    return float(num), unit


while True:

    link = 'https://ostrovok.ru/hotel/russia/gelendzhik/?page='+str(page)
    response = requests.get(link)
    html = BeautifulSoup(response.content, 'html.parser')
    items = html.select(".HotelCard_mainInfo__pNKYU")
    if (len(items)):
        for el in items:
            title = ((el.select(".HotelCard_wrapTitle__t742O > .HotelCard_title__cpfvk"))[0]).text
            geo = ((el.select(".HotelCard_address__AvnV2"))[0]).text
            distance = ((el.select(".HotelCard_distances__pVfDQ > .HotelCard_distance__CEiC3 > .HotelCard_distanceValue__TbHp_"))[0]).text
            stars = el.find_all(class_="Stars_star__jwPss HotelCard_star__xpZM1")
            countStars = len(stars)
            num,unit = split_string(distance)
            if unit == 'м':
                num = num/1000
                unit = 'км'
            if num < 1.5 and unit =='км':
                geoType = 'center'
            else:
                geoType = 'border'


            if (title.split(' '))[0] == 'Отель' or (title.split(' '))[0] == 'Гостевой' or (title.split(' '))[0] == 'Гостиница':
                hotels.append(title)
                hotels_distance.append(distance)
                hotels_geo.append(geo)
                hotels_stars.append(countStars)
                newHotel = {
                    'name': title,
                    "distance": distance,
                    'geolocation': geo,
                    "stars": countStars,
                    "typePlace": 'hotel',
                    "geo": geoType                }

            elif (title.split(' '))[0] == 'Апартаменты' or (title.split(' '))[0] == 'Апарт-Отель' or (title.split(' '))[0] == 'Квартира':
                apartments.append(title)
                apartments_distance.append(distance)
                apartments_geo.append(geo)
                apartments_stars.append(countStars)
                newHotel = {
                    'name': title,
                    "distance": distance,
                    'geolocation': geo,
                    "stars": countStars,
                    "typePlace": 'apartment',
                    "geo": geoType
                }
            elif (title.split(' '))[0] == 'Пансионат' or (title.split(' '))[0] == 'Санаторий':
                sanatoriums.append(title)
                sanatoriums_distance.append(distance)
                sanatoriums_geo.append(geo)
                sanatoriums_stars.append(countStars)
                newHotel = {
                    'name': title,
                    "distance": distance,
                    'geolocation': geo,
                    "stars": countStars,
                    "typePlace": 'sanatorium',
                    "geo": geoType
                    
                }
            else:
                newHotel = {
                    'name': title,
                    "distance": distance,
                    'geolocation': geo,
                    "stars": countStars,
                    "typePlace": 'hotel',
                    "geo": geoType
                }
            hotelsParsedData.append(newHotel)
        page += 1
    else:
        break

for hotel_data in hotelsParsedData:
    hotel = Hotel(name=hotel_data['name'], distance = hotel_data['distance'], type_place=hotel_data['typePlace'], geolocation=hotel_data['geo'])
    hotel.save()