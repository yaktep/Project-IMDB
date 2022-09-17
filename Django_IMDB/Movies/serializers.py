from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'cast', 'director', 'writers', 'actor', 'poster', 'year', 'plot', 'date',
                  'running_time', 'slug']
