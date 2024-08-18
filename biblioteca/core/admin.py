from django.contrib import admin

# Register your models here.
from core.models import Categoria, Autor, Livro
from datetime import date

# Criando categorias
ficcao = Categoria.objects.create(nome='Ficção')
ciencia = Categoria.objects.create(nome='Ciência')
# Criando autores
asimov = Autor.objects.create(nome='Isaac Asimov')
sagan = Autor.objects.create(nome='Carl Sagan')
# Criando livros
Livro.objects.create(titulo='Fundação', autor=asimov,
categoria=ficcao, publicado_em=date(1951, 6, 1))
Livro.objects.create(titulo='Cosmos', autor=sagan, categoria=ciencia,
publicado_em=date(1980, 10, 1))