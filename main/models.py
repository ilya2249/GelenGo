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
             
# Create your models here.
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

class Exc(models.Model):
    def __str__(self):
        return self.name 