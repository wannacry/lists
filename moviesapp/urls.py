from django.urls import path

from . import views


app_name = 'moviesapp'

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('movieid/1', views.movie_detail, name='movieid'),
]
