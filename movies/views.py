from rest_framework import generics, views, response  # Importa classes genéricas de views e módulos de resposta do Django REST Framework
from django.db.models import Count, Avg  # Importa funções de agregação do Django ORM
from rest_framework.permissions import IsAuthenticated  # Importa a permissão que verifica se o usuário está autenticado
from .models import Movie  # Importa o modelo Movie da aplicação atual
from .serializers import MovieSerializer  # Importa o serializer para o modelo Movie
# Importando a permissão customizada
from app.permissions import GlobalDefaultPermission  # Importa a permissão customizada GlobalDefaultPermission
from reviews.models import Review  # Importa o modelo Review da aplicação reviews
from rest_framework import status  # Importa o módulo de status HTTP do Django REST Framework


class MovieCreateListView(generics.ListCreateAPIView):
    """
    View para listar todos os filmes ou criar um novo filme.
    Apenas usuários autenticados com permissões adequadas podem acessar.
    """
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)  # Define as classes de permissão
    queryset = Movie.objects.all()  # Define o queryset para recuperar todos os objetos Movie
    serializer_class = MovieSerializer  # Define o serializer a ser usado para validar e serializar os dados


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para recuperar, atualizar ou excluir um filme específico.
    Apenas usuários autenticados com permissões adequadas podem acessar.
    """
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)  # Define as classes de permissão
    queryset = Movie.objects.all()  # Define o queryset para recuperar todos os objetos Movie
    serializer_class = MovieSerializer  # Define o serializer a ser usado para validar e serializar os dados


# CRUD para retornar estatísticas das APIs, número de visualizações, estrelas, etc., e verificar a permissão do usuário antes disso
class MovieStatsView(views.APIView):
    """
    View para retornar estatísticas sobre os filmes, como total de filmes, distribuição por gênero, total de reviews e média de estrelas.
    Apenas usuários autenticados com permissões adequadas podem acessar.
    """
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)  # Define as classes de permissão
    # queryset não é necessário em uma APIView padrão, pode ser removido
    # queryset = Movie.objects.all()

    def get(self, request):
        """
        Método para lidar com requisições GET e retornar as estatísticas.
        """
        # Buscar o total de filmes
        total_movies = Movie.objects.count()  # Conta o número total de objetos Movie

        # Agrupar filmes por gênero e contar o número de filmes em cada gênero
        movies_by_genre = Movie.objects.values('genre__name').annotate(count=Count('id'))  
        # Retorna uma lista de dicionários com o nome do gênero e a contagem de filmes

        # Contar o total de reviews
        total_reviews = Review.objects.count()  # Conta o número total de objetos Review

        # Calcular a média de estrelas das reviews
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']
        # Retorna a média das estrelas das reviews, ou None se não houver reviews

        return response.Response(
            data={  # Corrigido de 'Data' para 'data' (deve ser minúsculo)
                'total_movies': total_movies,  # Total de filmes
                'movies_by_genre': movies_by_genre,  # Distribuição de filmes por gênero
                'total_reviews': total_reviews,  # Total de reviews
                'average_stars': round(average_stars, 1) if average_stars else 0,  # Média de estrelas arredondada para 1 casa decimal, ou 0 se não houver
            },  
            status=status.HTTP_200_OK  # Retorna o status HTTP 200 OK
        )
