
from bs4 import BeautifulSoup
import requests
from .models import Hotel
def parserPlacesFunc():
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
        starChange = {
            1: 'Одна звезда',
            2: 'Две звезды',
            3: 'Три звезды',
            4: 'Четыре звезды',
            5: "Пять звезд",
            0: "Не указано"
    }
        link = 'https://ostrovok.ru/hotel/russia/gelendzhik/?page='+str(page)
        response = requests.get(link)
        html = BeautifulSoup(response.content, 'html.parser')
        items = html.select(".HotelList_card__Gk2_O")
        if (len(items)):
            for el in items:
                title = ((el.select(".HotelCard_wrapTitle__t742O > .HotelCard_title__cpfvk"))[0]).text
                geo = ((el.select(".HotelCard_address__AvnV2"))[0]).text
                distance = ((el.select(".HotelCard_distances__pVfDQ > .HotelCard_distance__CEiC3 > .HotelCard_distanceValue__TbHp_"))[0]).text
                stars = el.find_all(class_="Stars_star__jwPss HotelCard_star__xpZM1")
                countStars = len(stars)
                try:
                    gallery = (((el.select(".Gallery_image__H7GwU.HotelCard_image__NPyo1"))[0]).get('src'))
                except:
                    continue
                num,unit = split_string(distance)
                if unit == 'м':
                    num = num/1000
                    unit = 'км'
                if num < 1.5 and unit =='км':
                    geoType = 'center'
                else:
                    geoType = 'border'

                distance = num
                lenStars = countStars
                countStars = starChange.get(countStars)
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
                        "typePlace": 'Отели',
                        "geo": geoType,
                        'img': gallery,
                        'code':"hotels",
                        'codeStars': lenStars,
                        'codeGeoType':geoType              }

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
                        "typePlace": 'Апартаменты/квартиры',
                        "geo": geoType,
                        'img': gallery,
                        'code':"apartments",
                        'codeStars': lenStars,
                        'codeGeoType':geoType
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
                        "typePlace": 'Санатории',
                        "geo": geoType,
                        'img': gallery,
                        'code':"sanatoriums",
                        'codeStars': lenStars,
                        'codeGeoType':geoType
                        
                    }
                else:
                    newHotel = {
                        'name': title,
                        "distance": distance,
                        'geolocation': geo,
                        "stars": countStars,
                        "typePlace": 'Отели',
                        "geo": geoType,
                        'img': gallery,
                        'code':"hotels",
                        'codeStars': lenStars,
                        'codeGeoType':geoType
                    }
                hotelsParsedData.append(newHotel)
            page += 1
        else:
            break
            