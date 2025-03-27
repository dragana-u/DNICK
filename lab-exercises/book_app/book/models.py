from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_published = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_pages = models.IntegerField()
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    available = models.BooleanField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Translator(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.name} {self.nationality}'

class TranslatorBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    translator = models.ForeignKey(Translator, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book.title} {self.translator.name}'

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} {self.book.title}'