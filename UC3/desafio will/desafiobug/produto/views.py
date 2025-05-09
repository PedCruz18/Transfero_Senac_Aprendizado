# produto/views.py
from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

# Codigo com problema
"""
def cadastrar_produto(request):
    form = ProdutoForm(request.POST)  # O formulário é colocado diretamente com request.POST pode gerar problemas se não for um POST válido!
    if form.is_valid():
        form.save()
        return redirect('listar_produto')  # Redireciona após salvar mas o nome da view está errado ('listar_produto' ao invés de 'listar_produtos') o s no final importa.
    return render(request, 'cadastro.html', {'form': form})  # Renderiza a página com o formulário mas o nome do template pode não corresponder

def listar_produto(request):
    produtos = produto.objects.all()  # Erro: 'produto' está com a primeira letra minúscula O nome correto é 'Produto'
    return render(request, 'listar.html', {'produtos': produtos})  # O nome do template pode ser inconsistente com o nome de verdade

"""

# Codigo Resolvido
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('listar_produtos')  
    else:
        form = ProdutoForm() 

    return render(request, 'produto/cadastrar_produto.html', {'form': form})


def listar_produtos(request):
    produtos = Produto.objects.all() 
    return render(request, 'produto/listar_produtos.html', {'produtos': produtos})
