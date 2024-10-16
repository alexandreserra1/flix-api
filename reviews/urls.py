from django.urls import path
from . import views

#url de reviews
urlpatterns = [
    path('review-create-list/', views.ReviewCreateListView.as_view(), name='review-create-list'),
    path('review-detail/<int:pk>/', views.ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail'),
]