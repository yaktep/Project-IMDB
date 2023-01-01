from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Movies'

router = routers.DefaultRouter()
router.register('movies', views.MovieView)

urlpatterns = [
    path('', include(router.urls)),
    path('gallery', views.movie_gallery, name='gallery'),
    path('create/', views.review_create, name='create'),
    path('create2/', views.review_create2, name='create2'),
    path('<slug:slug>/', views.movie_description, name='description'),
]
