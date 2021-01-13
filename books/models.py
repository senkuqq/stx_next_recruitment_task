from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    google_id = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    authors = models.ManyToManyField(Author, blank=True)
    published_date = models.CharField(max_length=20, blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    average_rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ratings_count = models.IntegerField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)
