from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    header = models.ImageField(default='default.jfif', blank=True)
    genre = models.CharField(max_length=100)
    sub_header = models.ImageField(default='default.jfif', blank=True)
    cast = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    actors = models.CharField(max_length=100)
    poster = models.ImageField(default='default.jfif', blank=True)
    year = models.CharField(max_length=100)
    plot = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.title
