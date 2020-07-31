from django.urls import path

from . import views

urlpatterns = [
    path('', views.MovieList.as_view(), name='movie_list'),
    path('filter/', views.FilterMoviesView.as_view(), name='filter'),
    path('json-filter/', views.JsonFilterMoviesView.as_view(), name='json_filter'),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('actors/<str:slug>/', views.ActorView.as_view(), name='actor_detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
]
