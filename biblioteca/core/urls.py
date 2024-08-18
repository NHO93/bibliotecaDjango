from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.livro_list, name='livro_list'),
    path('livros/<int:id>/', views.livro_detail, name='livro_detail'),
]
