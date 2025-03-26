from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Market(models.Model):
    name = models.CharField(max_length=100)
    number_of_markets = models.IntegerField()
    date_opened = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    working_from = models.TimeField()
    working_to = models.TimeField()

    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    market = models.OneToOneField(Market, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.street} {self.number} {self.email}'

class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    EMBG = models.CharField(max_length=13, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.IntegerField()
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Product(models.Model):
    type_choice = {
        ("F","Food"),
        ("D","Drink"),
        ("B","Bakery"),
        ("C","Cosmetics"),
        ("H","Hygiene")
    }
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=type_choice)
    is_homemade = models.BooleanField()
    code = models.CharField(max_length=10, unique=True)

class MarketProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.market.name} - {self.product.name} {self.quantity}"