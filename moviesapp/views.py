import json
from gettext import Catalog

from django.core.serializers import serialize
from django.http import JsonResponse

from moviesapp.models import Movie
from profileapp.models import Profile, MoviesList
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
# Create your views here.


def catalog(request,page_num=1):
    return render(request, 'moviesapp/catalog.html',{'page_num':page_num})


def catalog_sorting(request,page_num=1):

    sort_order = request.GET.get('sort_order')
    sorting_value = request.GET.get('sorting_value')

    if sort_order == 'asc':
        movies = Paginator(Movie.objects.filter(vote_count__gt=300).order_by(sorting_value), 100)
        if sorting_value == 'vote_count':
            movies = Paginator(Movie.objects.all().order_by(sorting_value), 100)
    elif sort_order == 'desc':
        movies = Paginator(Movie.objects.filter(vote_count__gt=300).order_by(f'-{sorting_value}'), 100)
        if sorting_value == 'vote_count':
            movies = Paginator(Movie.objects.all().order_by(f'-{sorting_value}'), 100)

    if page_num < 1:
        page_num = 1
    elif page_num > movies.num_pages:
        page_num = movies.num_pages

    serializer = serialize('json', movies.page(page_num))
    movies_json = json.loads(serializer)
    return JsonResponse([movies_json,{'current_page':page_num,'last_page':movies.num_pages}], safe=False)

def movie_detail(request,movie_id):

    movie = Movie.objects.filter(id=movie_id).first()
    status = MoviesList.objects.filter(film_id=movie_id).first()
    context ={
        'profile': Profile.objects.filter(user=request.user).first(),
        'movie': movie,
        'genres':movie.genres.all(),
        'status':status
    }
    return render(request,'moviesapp/movie_detail.html',context)

def add_to_list(request):

    user = request.user
    data = json.loads(request.body)
    film_status = data.get('film_status')
    movie_id = data.get('movie_id')
    movie_id = Movie.objects.get(id=movie_id)

    if request.method == 'POST':
        if film_status == 'delete':
            MoviesList.objects.get(film_id=movie_id).delete()
        else:
            MoviesList.objects.update_or_create(
                film_id=movie_id,
                user=user,
                defaults={
                    'list_status':film_status,
                }
            )
        return JsonResponse({'list_status':film_status},safe=False)
