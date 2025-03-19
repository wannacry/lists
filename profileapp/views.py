from django.shortcuts import render

def profile(request):
    return render(request,'profileapp/profile.html')

def profile_settings(request):
    return render(request,'profileapp/profile_settings.html')
