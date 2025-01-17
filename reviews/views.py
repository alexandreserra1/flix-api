from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission  # Importando a permissão customizada
# Create your views here.


class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # Apenas usuários autenticados podem ver, editar ou excluir reviews.
    permission_classes = (IsAuthenticated,GlobalDefaultPermission)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer