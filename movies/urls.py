from django.urls import path
from . import views

# url de movies
urlpatterns = [
    path('movie-create-list/', views.MovieCreateListView.as_view(),
         name='movie-create-list'),
    path('movie-detail/<int:pk>/',
         views.MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail'),
    path('movie-stats/', views.MovieStatsView.as_view(), name='movie-stats'),
]
