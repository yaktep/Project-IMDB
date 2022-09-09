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
    writers = models.CharField(max_length=100, default='anonymus')
    actors = models.CharField(max_length=100)
    poster = models.ImageField(default='default.jfif', blank=True)
    year = models.CharField(max_length=100)
    plot = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    running_time = models.IntegerField(default=0)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=100, default='Film Title')
    in_short = models.CharField(max_length=100)
    in_long = models.TextField()
    score = models.IntegerField()
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, blank=True, null=False, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title
