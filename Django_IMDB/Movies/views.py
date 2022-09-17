from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie
from .models import Review
from django.contrib.auth.decorators import login_required
from . import forms
from rest_framework import viewsets, permissions
from .serializers import MovieSerializer


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# Create your views here.
def welcome(request):
    return HttpResponse("testing - ok?")


def movie_gallery(request):
    # print(f"article\views - article_list")
    movies = Movie.objects.all().order_by('date')
    return render(request, 'Movies/homepage.html', {'movies': movies})


def movie_description(request, slug):
    # print(f"article\\views - article_detail: slug={slug}")
    movie = Movie.objects.get(slug=slug)
    reviews = Review.objects.all().filter(movie=movie)
    reviews_count = len(reviews)
    return render(request, "Movies/description.html", {'movie': movie, 'reviews': reviews, 'count': reviews_count})


@login_required(login_url="/accounts/login")
def review_create2(request):
    return render(request, 'Movies/review_create1.html')


@login_required(login_url="/accounts/login")
def review_create(request):
    if request.method == 'POST':

        form = forms.CreateReview(request.POST)

        # check whether it's valid:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            nextpage = request.POST.get('next', '/')
            return HttpResponseRedirect(nextpage)

    else:
        form = forms.CreateReview()

    return render(request, 'Movies/review_create.html', {'form': form})
