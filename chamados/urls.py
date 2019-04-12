from django.urls import path
from .views import List_chamados, Cadastro_chamados

urlpatterns = [
    path('relatorio', List_chamados, name='List_chamados'),
    path('', Cadastro_chamados, name='Cadastro_chamados'),
]
