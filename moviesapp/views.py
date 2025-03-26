from gettext import Catalog

from moviesapp.models import Movie
from profileapp.models import Profile
from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.


def catalog(request,page_num=1):

    movies = Paginator(Movie.objects.filter(vote_count__gt=300).order_by('-vote_average'),100)
    if page_num<1:
        page_num=1
    elif page_num>movies.num_pages:
        page_num = movies.num_pages

    context ={
        'profile': Profile.objects.filter(user=request.user).first(),
        'catalog': movies.page(page_num),
        'current_page':page_num,
        'last_page': movies.num_pages,
    }
    return render(request,'moviesapp/catalog.html',context)

def movie_detail(request,movie_id):

    movie = Movie.objects.filter(id=movie_id).first()
    context ={
        'profile': Profile.objects.filter(user=request.user).first(),
        'movie': movie,
        'genres':movie.genres.all()
    }

    return render(request,'moviesapp/movie_detail.html',context)