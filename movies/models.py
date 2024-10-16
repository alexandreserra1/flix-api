from django.db import models
from genres.models import Genre
from actors.models import Actor

# Create your models here.


class Movie(models.Model):
    
    title = models.CharField(max_length=500)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,  # protege os registros do banco de dados
        related_name="movies"  # ve todos os generos que o filme esta ligado
    )
    release_date = models.DateField(
        null=True, blank=True)  # data de lançamento
    # ligar o ator a varios filmes ou vice-versa
    actors = models.ManyToManyField(Actor, related_name='moveis')
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
