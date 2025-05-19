from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Baker(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, null=True, blank=True)
    surname = models.CharField(max_length=25, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Cake(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='cakes/', null=True, blank=True)
    baker = models.ForeignKey(Baker, null=True, blank=True, on_delete=models.CASCADE, related_name='cakes')

    def __str__(self):
        return f"{self.name}"