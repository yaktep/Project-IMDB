from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'cast', 'director', 'writers', 'actors', 'poster', 'year', 'plot',
                  'running_time', 'user', 'slug']
