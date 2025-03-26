from django.urls import path

from . import views


app_name = 'moviesapp'

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:page_num>', views.catalog, name='catalog'),
    path('movie_detail/<int:movie_id>', views.movie_detail, name='movie_detail'),
]
