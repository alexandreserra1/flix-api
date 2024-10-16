from django.urls import path
from . import views #importa tudo o que estiver dentro de views, depois colocar um .views antes da importacao

urlpatterns = [
    path('genre-create-list/', views.GenreCreateListView.as_view(), name='genre-create-list'),
    path('genre-detail/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail'),
]
