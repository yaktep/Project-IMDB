from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from django.contrib.auth.decorators import login_required
from . import forms


# from django.contrib.auth.decorators import login_required
# from . import forms


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
    return render(request, "Movies/description.html", {'movie': movie})


def review_create1(request):
    return render(request, 'Movies/review_create1.html')


@login_required(login_url="/accounts/login")
def review_create2(request):
    return render(request, 'Movies/review_create1.html')


@login_required(login_url="/accounts/login")
def review_create(request):
    form = None
    if request.method == "POST":
        form = forms.CreateReview(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('Movies:gallery')
        else:
            form = forms.CreateReview()
    return render(request, 'Movies/review_create.html', {
        'form': form,
        'user': request.user
    })

