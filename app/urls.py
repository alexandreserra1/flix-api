from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/', include('genres.urls')), #tudo o que tiver dentro de genres que contem url, importa.
            #v1 seria o versionamento
    
    # URLs para atores
    path('api/v1/', include('actors.urls')),
        
    # URLs para filmes
    path('api/v1/', include('movies.urls')),
    
    # URLs para reviews
    path('api/v1/', include('reviews.urls')),
    
    # URLs para autenticação
    path('api/v1/', include('authentication.urls')),
]
