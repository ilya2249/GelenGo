from django.db import models

class TypePlace(models.Model):
    name = models.CharField('Название', max_length=255)
    code = models.CharField('Код', max_length=255)
    
    def __str__(self):
        return self.name 


class Star(models.Model):
    name = models.CharField('Название', max_length=255)
    code = models.CharField('Код', max_length=255)
    def __str__(self):
        return self.name 


class Geo(models.Model):
    name = models.CharField('Название', max_length=255)
    code = models.CharField('Код', max_length=255)
    def __str__(self):
        return self.name 


class Hotel(models.Model):
    name = models.CharField('Название', max_length=255)
    code = models.CharField('Код', max_length=255)

    def __str__(self):
        return self.name 
             

class Place(models.Model):
    name = models.CharField('Название', max_length=255)
    text = models.TextField('Описание')
    img = models.ImageField('Карточки',upload_to="cards")
    geolocation = models.CharField('Геолокация', default=0, max_length = 255)
    distance = models.CharField('Дистанция от центра',max_length=255)
    type_place = models.ForeignKey(TypePlace, null=True, blank=True, on_delete=models.CASCADE)
    star =  models.ForeignKey(Star, null=True, blank=True, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, null=True, blank=True, on_delete=models.CASCADE)
    geo = models.ForeignKey(Geo, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name 

class Chill_Type(models.Model):
    name = models.CharField('Название', max_length=255)
    code = models.CharField('Код', max_length=255)
    def __str__(self):
        return self.name 


class Price_Type(models.Model):
    name = models.CharField('Название', max_length=255)
    code = models.CharField('Код', max_length=255)

    def __str__(self):
        return self.name 


class Chill(models.Model):
    name = models.CharField('Название', max_length=255)
    text = models.TextField('Описание')
    img = models.ImageField('Карточки',upload_to="cards",blank=True)
    price = models.CharField('Цена', default=0, max_length = 255)
    chill_type = models.ForeignKey(Chill_Type, null=True, blank=True, on_delete=models.CASCADE)
    price_type = models.ForeignKey(Price_Type, null=True, blank=True, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name 
class Date_type(models.Model):
    name = models.CharField('Название', max_length = 255)
    code = models.CharField('Код', max_length=255)
    def __str__(self):
        return self.name 
class Geo_type(models.Model):
    name = models.CharField('Название', max_length = 255)
    code = models.CharField('Код', max_length=255)
    def __str__(self):
        return self.name 
class Event_type(models.Model):
    name = models.CharField('Название', max_length = 255)
    code = models.CharField('Код', max_length=255)
    def __str__(self):
        return self.name 
class Event(models.Model):
    name = models.CharField('Название', max_length=255)
    text = models.TextField('Описание')
    img = models.ImageField('Карточки',upload_to="cards",blank=True)
    event_type = models.ForeignKey(Event_type, null=True, blank=True, on_delete=models.CASCADE)
    date_type = models.ForeignKey(Date_type, null=True, blank=True, on_delete=models.CASCADE)
    Geo = models.ForeignKey(Geo_type, null=True, blank=True, on_delete=models.CASCADE)
    dateEvent= models.CharField('Дата',default=0, max_length = 255)
    typeE = models.CharField('Название', max_length=255,default=0)
    
    def __str__(self):
        return self.name 

class MyModel(models.Model):
    unique_field = models.CharField(max_length=100, unique=True)
class Exc(models.Model):
    def __str__(self):
        return self.name 
class BeachGeo(models.Model):
    name = models.CharField('Название', max_length = 255)
    code = models.CharField('Код', max_length=255)
    def __str__(self):
        return self.name 
class BeachType(models.Model):
    name = models.CharField('Название', max_length = 255)
    code = models.CharField('Код', max_length=255)
    def __str__(self):
        return self.name
class BeachCost(models.Model):
    name = models.CharField('Название', max_length = 255)
    code = models.CharField('Код', max_length=255)
    def __str__(self):
        return self.name  
class Beach(models.Model):
    name = models.CharField('Название', max_length=255)
    text = models.TextField('Описание')
    img = models.ImageField('Карточки',upload_to="cards",blank=True)
    isAllowedIMG = models.ImageField('Купание запрещено',upload_to="cards",blank=True)
    lenght = models.CharField('Протяженность', max_length=255,default=0)
    width = models.CharField('Ширина', max_length=255,default=0)
    geolocation = models.CharField('Геолокация', max_length=255,default=0)
    beach_geo= models.ForeignKey(BeachType, null=True, blank=True, on_delete=models.CASCADE)
    beach_type = models.ForeignKey(BeachGeo, null=True, blank=True, on_delete=models.CASCADE)
    beach_type_cost = models.ForeignKey(BeachCost, null=True, blank=True, on_delete=models.CASCADE)
    sunloungersIMG = models.ImageField('Шезлонги',upload_to="cards",blank=True)
    coctelIMG = models.ImageField('Коктель',upload_to="cards",blank=True)
    showerIMG = models.ImageField('Душ',upload_to="cards",blank=True)
    sportIMG =  models.ImageField('Спорт',upload_to="cards",blank=True)
    gymIMG = models.ImageField('Gym',upload_to="cards",blank=True)
    def __str__(self):
        return self.name 