from django.urls import path

from . import views

urlpatterns = [
    path('', views.MovieList.as_view(), name='movie_list'),
]
