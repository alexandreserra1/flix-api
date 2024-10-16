from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


# Urls para autenticação JWT
urlpatterns = [
    
    # Token para gerar um par de tokens (access e refresh)
    path('authentication/token', TokenObtainPairView.as_view, name='token_obtain_pair'),
    
    # Token para renovar o token
    path('authentication/token/refresh', TokenRefreshView.as_view(token_type_prefix='refresh'), name='token_refresh'),
    
    # Token para validar o token
    path('authentication/token/verify', TokenVerifyView.as_view(token_type_prefix='access'), name='token_verify'),
]
