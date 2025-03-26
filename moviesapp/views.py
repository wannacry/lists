from profileapp.models import Profile
from django.shortcuts import render

# Create your views here.


def catalog(request):

    context ={
        'profile': Profile.objects.filter(user=request.user).first()
    }

    return render(request,'moviesapp/catalog.html',context)

def movie_detail(request):

    context ={
        'profile': Profile.objects.filter(user=request.user).first()
    }

    return render(request,'moviesapp/movie_detail.html',context)