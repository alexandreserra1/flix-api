from rest_framework import permissions  # Importa o módulo de permissões do Django REST Framework


class GlobalDefaultPermission(permissions.BasePermission):
    """
    Permissão que permite apenas usuários com permissões específicas de modelo acessarem os endpoints.
    """

    def has_permission(self, request, view):
        # Obtém o codename da permissão do modelo com base no método HTTP e na view
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )
        if model_permission_codename is None:
            return False  # Retorna False se não houver codename de permissão definido

        # Verifica se o usuário possui a permissão específica
        return request.user.has_perm(model_permission_codename)

    def __get_model_permission_codename(self, method, view):
        """
        Determina o codename da permissão do modelo apropriada para a view com base no método HTTP.
        """
        try:
            model = view.queryset.model  # Obtém o modelo associado à view
            model_name = model._meta.model_name  # Nome do modelo em minúsculas
            app_label = model._meta.app_label  # Nome da aplicação
            action = self.__get_action_suffix(method)  # Obtém o sufixo da ação com base no método
            return f"{app_label}.{model_name}_{action}"  # Formata o codename da permissão
        except AttributeError:
            return None  # Retorna None se a view não possuir um queryset

    def __get_action_suffix(self, method):
        """
        Mapeia métodos HTTP para ações de permissão padrão do Django.
        """
        method_actions = {
            'GET': 'view',      # Métodos de leitura
            'POST': 'add',      # Método de criação
            'PUT': 'change',    # Método de atualização completa
            'PATCH': 'change',  # Método de atualização parcial
            'DELETE': 'delete', # Método de deleção
            'HEAD': 'view',     # Métodos de cabeçalho
            'OPTIONS': 'view',  # Métodos de opções
        }
        return method_actions.get(method, '')  # Retorna o sufixo correspondente ou uma string vazia
