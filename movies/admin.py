from django.contrib import admin
from .models import Movie

@admin.register(Movie)
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'resume', 'genre', 'id')

    def __str__(self):
        return self.title
    
