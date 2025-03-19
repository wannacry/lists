from django.urls import path

from . import views

app_name = 'profileapp'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('settings/',views.profile_settings,name='profile_settings'),
]
