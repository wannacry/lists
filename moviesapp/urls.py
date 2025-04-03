from django.urls import path

from . import views


app_name = 'moviesapp'

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:page_num>/', views.catalog, name='catalog'),

    path('catalog_sorting/', views.catalog_sorting, name='catalog_sorting'),
    path('catalog_sorting/<int:page_num>/', views.catalog_sorting, name='catalog_sorting'),

    path('movie_detail/<int:movie_id>', views.movie_detail, name='movie_detail'),
    path('add_to_list/', views.add_to_list, name='add_to_list'),
]
