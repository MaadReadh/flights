import code
from tabnanny import verbose
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
      return f'{self.name}'
    class Meta:
      verbose_name = 'Country'
      verbose_name_plural ='Countries'
         

class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


    def __str__(self):
      return f'{self.name}'
    class Meta:
      verbose_name = 'City'
      verbose_name_plural ='Cities'


class Airport(models.Model):
    code = models.CharField(max_length=5)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city} ({self.code})"



class Flight(models.Model):

    origin = models.ForeignKey(Airport,related_name='origin_flight', on_delete=models.CASCADE)
    destination = models.ForeignKey(Airport,related_name='destination_flight', on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
   
    def __str__(self):
        return f"{self.origin} to {self.destination}, duration: {self.duration}" 




class Booking(models.Model):
    customer = models.CharField(max_length = 255)
    seat = models.IntegerField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first}{self.last}"    