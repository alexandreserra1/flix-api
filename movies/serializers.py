from rest_framework import serializers
from django.db.models import Avg
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    # campo calculado / campo apenas de leitura / calcula com base no rate dos usuarios
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        # Mostra todos os relacionamentos (filmes com generos e atores)
        depth = 1

        def get_rate(self, obj):  # colocar o get na frente para ele entender
            # metodo AVG do django, ja calcula a media do campo / Agrega um campo extra pra mim (por isso o aggregate)
            rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
            if rate:
                return round(rate, 1)  # retorna com uma casa decimal

            return None  # se não houver reviews, retorna None

        # colocar o validate nno começo para ele entender
        def validate_release_data(self, value):
            if value.year < 1900:
                raise serializers.ValidationError('Filme muito antigo.')
            return value

        def validate_resume(self, value):
            if len(value) > 500:
                raise serializers.ValidationError('Resumo muito grande.')
            return value
