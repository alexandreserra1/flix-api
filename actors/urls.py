from django.urls import path
from . import views

urlpatterns = [
    path('actor-create-list/', views.ActorCreateListView.as_view(), name='actor-create-list'),
    path('actor-detail/<int:pk>/', views.ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail'),
]