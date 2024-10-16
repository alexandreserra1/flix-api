from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name="reviews",
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliaçao nao pode ser inferior a 0 estrelas'),
            MaxValueValidator(5, 'Avaliaçao nao pode ser superior a 5 estrelas'),
        ],  # validador para garantir que o valor seja um numero entre 0 e 5
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.comment