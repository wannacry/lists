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
