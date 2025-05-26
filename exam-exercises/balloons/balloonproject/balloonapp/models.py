from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Pilot(models.Model):
    choice = [
        ('J', 'Junior'),
        ('S', 'Senior'),
        ('E', 'Expert'),
    ]
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    total_hours = models.IntegerField()
    experience = models.CharField(choices=choice, max_length=1)

class Balloon(models.Model):
    type = models.CharField(max_length=100)
    name_of_company = models.CharField(max_length=100)
    max_passengers = models.IntegerField()

class Airline(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    europe_flight = models.BooleanField()

class AirlinePilot(models.Model):
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    date_of_joining = models.DateField()

    def __str__(self):
        return f"{self.pilot.name} - {self.airline.name}"

class Flight(models.Model):
    code = models.CharField(max_length=10, unique=True)
    flight_from = models.CharField(max_length=100)
    flight_to = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='flight_images/', blank=True, null=True)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return self.code