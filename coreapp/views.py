from django.contrib.auth.models import User
from django.shortcuts import render
from profileapp.models import Profile

def core(request):


    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
        return render(request, 'coreapp/main.html',{'profile':profile})
    return render(request, 'coreapp/main.html')
