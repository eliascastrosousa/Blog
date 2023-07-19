from django.urls import path
from .views import movies, tvshows

urlpatterns = [
    path('movies', movies , name="movies"),
    path('tvshows', tvshows, name="tvshows")
]
