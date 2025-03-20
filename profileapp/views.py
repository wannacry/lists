from django.shortcuts import render
from allauth.mfa.models import Authenticator
from lists.settings import MFA_SUPPORTED_TYPES
from allauth.mfa.utils import is_mfa_enabled
from .models import Profile


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
