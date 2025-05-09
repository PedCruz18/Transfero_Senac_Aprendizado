# produto/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produtos/', views.listar_produtos, name='listar_produtos'),
]
