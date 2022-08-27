from django.urls import path
from . import views

app_name = 'Movies'

urlpatterns = [
    path('', views.movie_gallery, name='gallery'),
    path('create/', views.review_create, name='create'),
    path('create1/', views.review_create1, name='create1'),
    path('create2/', views.review_create2, name='create2'),
    path('<slug:slug>/', views.movie_description, name='description'),


]
