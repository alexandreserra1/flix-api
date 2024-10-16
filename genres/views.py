from rest_framework import generics  # Importa os CRUD
from genres.models import Genre  # Importa o modelo Genre do aplicativo genres
from genres.serializers import GenreSerializer  # Serializers
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission  # Permissões customizadas



class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()  # Qual model é e quais objetos tem que retornar
    serializer_class = GenreSerializer
    # Apenas usuários autenticados podem ver, editar ou excluir gêneros.
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # Apenas usuários autenticados podem ver, editar ou excluir gêneros.
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
