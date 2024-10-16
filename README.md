# Flix-API

## Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Uso](#uso)
- [Endpoints da API](#endpoints-da-api)
- [Serializers](#serializers)
  - [Função Principal](#função-principal)
  - [Validação e Cálculo de Dados](#validação-e-cálculo-de-dados)
  - [ModelSerializer](#modelserializer)
  - [Escolha entre Serializer e ModelSerializer](#escolha-entre-serializer-e-modelserializer)
  - [Boas Práticas](#boas-práticas)
- [Autenticação e Permissões](#autenticação-e-permissões)
  - [JWT](#jwt)
  - [Classes de Permissão](#classes-de-permissão)
  - [Configuração de Permissões Globais](#configuração-de-permissões-globais)
- [Agregações e Cálculos no Django ORM](#agregações-e-cálculos-no-django-orm)
  - [Método Avg com aggregate](#método-avg-com-aggregate)
- [Boas Práticas de Desenvolvimento](#boas-práticas-de-desenvolvimento)
- [Testes](#testes)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

---

## Visão Geral

**Flix-API** é uma API robusta desenvolvida com Django e Django REST Framework, projetada para gerenciar um catálogo de filmes. Ela oferece funcionalidades de criação, leitura, atualização e exclusão (CRUD) de filmes, além de endpoints para estatísticas detalhadas, como distribuição por gênero, avaliações e média de estrelas. A segurança e o controle de acesso são garantidos através de autenticação JWT e classes de permissão personalizadas.

---

## Funcionalidades

- **CRUD de Filmes**: Crie, liste, recupere, atualize e exclua filmes.
- **Estatísticas Avançadas**: Obtenha estatísticas sobre os filmes, como total de filmes, distribuição por gênero, número de avaliações e média de estrelas.
- **Autenticação JWT**: Segurança robusta utilizando JSON Web Tokens para autenticação.
- **Permissões Personalizadas**: Controle granular sobre o que cada usuário pode fazer na API.
- **Serializers Avançados**: Validação e transformação de dados eficiente usando serializers e ModelSerializers.
- **Agregações no Django ORM**: Cálculos eficientes diretamente no banco de dados utilizando métodos como `Avg` e `Count`.

---

## Tecnologias Utilizadas

- **Python 3.x**
- **Django 4.x**
- **Django REST Framework**
- **SQLite/PostgreSQL** *(escolha conforme sua configuração)*
- **JWT para Autenticação**
- **Git para Controle de Versão**

---

## Instalação

### Pré-requisitos

- Python 3.x instalado
- Git instalado

### Passos de Instalação

1. **Clone o Repositório:**

    ```bash
    git clone https://github.com/seu-usuario/flix-api.git
    cd flix-api
    ```

2. **Crie e Ative um Ambiente Virtual:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. **Instale as Dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure as Variáveis de Ambiente:**

    Crie um arquivo `.env` na raiz do projeto e adicione as variáveis necessárias, como `SECRET_KEY`, `DEBUG`, `DATABASE_URL`, etc.

    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    DATABASE_URL=sqlite:///db.sqlite3
    ```

5. **Aplicar Migrações:**

    ```bash
    python manage.py migrate
    ```

6. **Criar um Superusuário:**

    ```bash
    python manage.py createsuperuser
    ```

7. **Executar o Servidor de Desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

    A API estará disponível em `http://127.0.0.1:8000/`

---

## Uso

Após a instalação, você pode interagir com a API utilizando ferramentas como **Postman**, **Insomnia** ou diretamente pelo navegador.

### Autenticação

1. **Registro de Usuário:**

    Envie uma requisição POST para `/api/register/` com os dados do usuário.

2. **Login:**

    Envie uma requisição POST para `/api/token/` com as credenciais do usuário para obter os tokens JWT.

3. **Uso dos Tokens:**

    Inclua o token de acesso no cabeçalho `Authorization` das requisições protegidas:

    ```
    Authorization: Bearer <seu_token>
    ```

---

## Endpoints da API

### Filmes

- **Listar e Criar Filmes**

    - **URL:** `/api/movies/`
    - **Métodos:** `GET`, `POST`
    - **Permissões:** Usuários autenticados com permissões específicas.

- **Recuperar, Atualizar e Excluir um Filme**

    - **URL:** `/api/movies/<id>/`
    - **Métodos:** `GET`, `PUT`, `PATCH`, `DELETE`
    - **Permissões:** Usuários autenticados com permissões específicas.

- **Estatísticas dos Filmes**

    - **URL:** `/api/movies/stats/`
    - **Método:** `GET`
    - **Permissões:** Usuários autenticados com permissões específicas.
    - **Descrição:** Retorna estatísticas como total de filmes, distribuição por gênero, total de avaliações e média de estrelas.

### Autenticação

- **Obter Token JWT**

    - **URL:** `/api/token/`
    - **Método:** `POST`

- **Atualizar Token JWT**

    - **URL:** `/api/token/refresh/`
    - **Método:** `POST`

---

## Serializers

Os **Serializers** no Django REST Framework são responsáveis por converter dados complexos, como instâncias de modelos Django, em formatos nativos de Python que podem ser facilmente renderizados em JSON, XML, etc., e vice-versa.

### Função Principal

- **Conversão de Dados:** Convertem conjuntos de dados complexos em formatos nativos de Python.

    ```python
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'
    ```

### Validação e Cálculo de Dados

- **Validação:** Garantem que os dados de entrada atendam às regras definidas antes de salvar ou processar.

    ```python
    def validate_title(self, value):
        if 'badword' in value.lower():
            raise serializers.ValidationError("Título contém palavras proibidas.")
        return value
    ```

- **Regras e Validações Manuais:** Definidas manualmente para personalizar a validação dos dados.

    ```python
    def validate(self, data):
        if data['release_date'] > timezone.now().date():
            raise serializers.ValidationError("A data de lançamento não pode ser no futuro.")
        return data
    ```

- **Campos Calculados com `SerializerMethodField`:** Adicionam campos que não estão diretamente presentes no modelo, calculando seus valores dinamicamente.

    ```python
    class MovieSerializer(serializers.ModelSerializer):
        average_rating = serializers.SerializerMethodField()
        
        class Meta:
            model = Movie
            fields = '__all__'
        
        def get_average_rating(self, obj):
            return obj.reviews.aggregate(avg=Avg('stars'))['avg'] or 0
    ```

### ModelSerializer

**ModelSerializer** automatiza a criação de campos com base no modelo Django associado, reduzindo a quantidade de código manual necessário.

- **Definição Automática:** Gera campos, regras e validações com base nas definições do modelo.

    ```python
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'
    ```

- **Herança do Modelo:** Herda automaticamente todos os campos e comportamentos do modelo ao qual está associado.

- **Validações Personalizadas:**

    ```python
    def validate_title(self, value):
        if 'badword' in value.lower():
            raise serializers.ValidationError("Título contém palavras proibidas.")
        return value
    ```

### Escolha entre Serializer e ModelSerializer

- **Use `Serializer` quando:**
  - Precisa de controle total sobre os campos e a lógica de serialização.
  - Os dados não estão diretamente ligados a um modelo Django.

- **Use `ModelSerializer` quando:**
  - Deseja simplificar a criação de serializers baseados em modelos Django.
  - Aproveitar a automação de campos e validações.

### Boas Práticas

- **Evite Lógica Complexa nos Serializers:** Mantenha a lógica de negócios no modelo ou em outras camadas da aplicação.
- **Reutilização de Código:** Crie serializers base ou mixins para evitar duplicação.
- **Documentação e Manutenção:**
  - Adicione docstrings e comentários nos serializers.
  - Implemente testes para garantir que as validações e campos calculados funcionem conforme o esperado.

---

## Autenticação e Permissões

### JWT

**JSON Web Tokens (JWT)** são utilizados para autenticação segura. Eles permitem que o cliente armazene o token e o envie em cada requisição, garantindo que apenas usuários autenticados possam acessar certos endpoints.

**Configuração:**

1. **Instalação:**

    ```bash
    pip install djangorestframework-simplejwt
    ```

2. **Atualização do `settings.py`:**

    ```python
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),
    }
    ```