from django.contrib import admin
from .models import MovieGenres,Country,Language,Movie
admin.site.register(MovieGenres)
admin.site.register(Country)
admin.site.register(Language)
admin.site.register(Movie)
