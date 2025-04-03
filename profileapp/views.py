import json

from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render
from allauth.mfa.models import Authenticator
from lists.settings import MFA_SUPPORTED_TYPES
from allauth.mfa.utils import is_mfa_enabled

from moviesapp.models import Movie
from .models import Profile, MoviesList


def profile(request):
    context = {
        'profile' : Profile.objects.filter(user=request.user).first()
    }
    return render(request,'profileapp/profile.html',context)


def profile_settings(request):
    context = {
        'MFA_SUPPORTED_TYPES':MFA_SUPPORTED_TYPES,
        'authenticator':is_mfa_enabled(request.user,[Authenticator.Type.TOTP]),
        'profile': Profile.objects.filter(user=request.user).first(),
    }
    return render(request,'profileapp/profile_settings.html',context)

def list(request):

    movies_list = MoviesList.objects.filter(user=request.user)
    context = {
        'profile': Profile.objects.filter(user=request.user).first(),
        'movies_list':movies_list,
    }
    return render(request,'profileapp/lists.html',context)

def lists_choise(request):

    status = request.GET.get('lists_status')
    movies_list = MoviesList.objects.filter(user=request.user)
    if status != 'all':
        movies_list = MoviesList.objects.filter(user=request.user,list_status=status)
    movie_detail_list=[]
    for i in movies_list:
        movie_detail_list.append({'id':i.film_id.id,'title':i.film_id.title,'runtime':i.film_id.runtime,'release_date':i.film_id.release_date,
                                  'date_added':i.date_added,'imdb_rating':i.film_id.imdb_rating,'vote_average':i.film_id.vote_average,
                                  'status':i.list_status})

    return JsonResponse(movie_detail_list,safe=False)