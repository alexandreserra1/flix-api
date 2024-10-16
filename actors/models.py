from django.db import models

# fazer uma variavel/constante que dita o que deve ser escrito
NATIONALITY_CHOICES =(
    ('BR', 'Brasil'),
    ('EUA', 'Estados Unidos'),
    ('FR', 'França'),
    ('ESP', 'Espanha'),
    ('ING', 'Inglaterra'),
    ('JAP', 'Japão'),
    ('CHI', 'Chile'),
    ('ARG', 'Argentina'),
    ('ITA', 'Italia'),
    ('DEU', 'Alemanha'),
)
class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null= True, blank=True)
    nationality = models.CharField(
        choices=NATIONALITY_CHOICES,
        default='BR',
        max_length=100,
        null= True,
        blank=True
    )

    def __str__(self):
        return self.name