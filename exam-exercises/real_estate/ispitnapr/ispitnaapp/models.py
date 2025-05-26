from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class RealEstate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    date_published = models.DateField()
    image = models.ImageField(upload_to='real_estate_images/')
    is_reserved = models.BooleanField()
    is_sold = models.BooleanField()

    def __str__(self):
        return self.name

class Agent(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    link_to_linkedin = models.URLField()
    number_sales = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.surname}"

class AgentRealEstate(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.agent.name} - {self.real_estate.name}"

class Characteristic(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class RealEstateCharacteristic(models.Model):
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.real_estate.name} - {self.characteristic.name}"
