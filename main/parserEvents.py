from bs4 import BeautifulSoup
import requests
import datetime
def parserEventsFunc():
    parsedDataEvents = []

    linkSpectacles = "https://www.afisha.ru/gelendzhik/schedule_theatre/"
    response= requests.get(linkSpectacles)
    html = BeautifulSoup(response.content, 'html.parser')
    items = html.select('.oP17O')
    keysMonth = {
        'января': 1,
        'февраля': 2,
        'марта': 3,
        'апреля': 4,
        'мая': 5,
        'июня': 6,
        'июля': 7,
        'августа': 8,
        'сентября': 9,
        'октября': 10,
        'ноября': 11,
        'декабря': 12
    }
    keysPlace = {
        'Городской дворец культуры': 'DK',
        'Горный парк Олимп': 'Olimp'
    }
    monthNow = int(datetime.date.today().strftime('%m'))
    dayNow = int(datetime.date.today().strftime('%d'))

    if len(items):
        for el in items:
            img = (((el.select(".QsWic.rIUFv > a > picture > img"))[0]).get('src'))
            title = (el.select('.CjnHd.y8A5E.nbCNS.yknrM')[0]).text
            type = (el.select('.S_wwn')[0]).text
            templist = ((el.select('._JP4u')[0]).text).split(', ')
            date, place = templist[0], templist[1]
            day = (date.split(' '))[0]
            month = keysMonth.get((date.split(' '))[1])
            if monthNow == month and day == dayNow:
                time = 'today'
            elif monthNow == month and (int(day) - dayNow) <= 7:
                time = '7days'
            elif monthNow == month:
                time = 'month'
            else:
                time = 'all'
            item = {
                'img': img,
                'title': title,
                'type': type,
                'date': date,
                'place': place,
                'time': time,
                'globalType': 'spectacles',
                "placeType": keysPlace.get(place)
            }
            parsedDataEvents.append(item)
    linkConcerts = "https://www.afisha.ru/gelendzhik/events/concerts/"
    response = requests.get(linkConcerts)
    html = BeautifulSoup(response.content, 'html.parser')
    items = html.select('.oP17O')
    if len(items):
        for el in items:
            img = (((el.select(".QsWic.rIUFv > a > picture > img"))[0]).get('src'))
            title = (el.select('.CjnHd.y8A5E.nbCNS.yknrM')[0]).text
            type = (el.select('.S_wwn')[0]).text
            templist = ((el.select('._JP4u')[0]).text).split(', ')
            date, place = templist[0], templist[1]
            day = (date.split(' '))[0]
            month = keysMonth.get((date.split(' '))[1])

            if monthNow == month and day == dayNow:
                time = 'today'
            elif monthNow == month and (int(day) - dayNow) <= 7:
                time = '7days'
            elif monthNow == month:
                time = 'month'
            else:
                time = 'all'
            item = {
                'img': img,
                'title': title,
                'type': type,
                'date': date,
                'place': place,
                'time': time,
                'globalType': 'concerts',
                'placeType': keysPlace.get(place),
            }
            parsedDataEvents.append(item)

    linkCinema = "https://www.afisha.ru/gelendzhik/events/movies/"
    response = requests.get(linkCinema)
    html = BeautifulSoup(response.content, 'html.parser')
    items = html.select('.oP17O')
    if len(items):
        for el in items:
            img = (((el.select(".QsWic.rIUFv > a > picture > img"))[0]).get('src'))
            title = (el.select('.CjnHd.y8A5E.nbCNS.yknrM')[0]).text
            templist = ((el.select('.S_wwn')[0]).text).split(', ')
            dateFilm, type = templist[0], templist[1]

            item = {
                'img': img,
                'title': title,
                'type': type,
                'date': dateFilm,
                'place': 'Кинотеатр "Радуга"',
                'placeType': 'Raduga',
                'globalType': 'cinema',
                'time' : 'all'
            }
            parsedDataEvents.append(item)
    return(parsedDataEvents)