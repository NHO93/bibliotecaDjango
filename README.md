# Biblioteca Django

O objetivo do projeto é implementar um sistema de gerenciamento de biblioteca que permite a administração de livros, autores e categorias, utilizando Django ORM, Serializers manuais e Function-Based Views (FBVs).

## Funcionalidades

- **Modelos**: Gerenciamento de Livros, Autores e Categorias.
- **Operações de CRUD**: Criação, leitura, atualização e exclusão de dados usando o Django ORM.
- **Serializadores**: Implementação manual de Serializers para os modelos.
- **API RESTful**: Construção de uma API para manipulação de dados através de Function-Based Views.
- **Banco de Dados**: Configuração padrão com SQLite.

## Tecnologias Utilizadas

- **Django**: Framework web para o backend.
- **Django REST Framework**: Para implementação da API e Serializers.
- **SQLite**: Banco de dados relacional para persistência de dados.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/username/biblioteca-django.git
   cd biblioteca-django
   ```

2. Crie um ambiente virtual e instale as dependências:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Crie e aplique as migrações do banco de dados:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Inicie o servidor local:

   ```bash
   python manage.py runserver
   ```

## Utilização

- **Listar Livros**: Faça uma requisição GET para `/livros/`.
- **Criar Livro**: Envie uma requisição POST para `/livros/` com os dados do livro.
- **Detalhar Livro**: Realize uma requisição GET para `/livros/<id>/` com o ID do livro.
- **Atualizar Livro**: Envie uma requisição PUT para `/livros/<id>/` com os dados atualizados.
- **Excluir Livro**: Realize uma requisição DELETE para `/livros/<id>/` para excluir um livro específico.

## Serializers

O projeto utiliza serializadores manuais para manipulação de dados nos modelos de Categoria, Autor e Livro. Exemplo de um Serializer para Livros:

```python
class LivroSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField(max_length=200)
    autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all())
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    publicado_em = serializers.DateField()
```

## Testes

Utilize ferramentas como **Postman** para realizar testes nas seguintes rotas da API:

- Listar todos os livros: `GET /livros/`
- Criar um novo livro: `POST /livros/`
- Detalhar um livro específico: `GET /livros/<id>/`
- Atualizar um livro: `PUT /livros/<id>/`
- Deletar um livro: `DELETE /livros/<id>/`

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Este modelo pode ser adaptado conforme necessário para o seu projeto【4†source】.