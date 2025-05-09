from django.db import models

# Codigo com erro: 
"""
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    # Problema: Limita o preço a até 999,999.99 pode ser insuficiente para produtos de alto valor
    
    categoria = models.CharField(max_length=50)
    # Problema: O campo de categoria é simples Em sistemas mais complexos seria melhor usar uma ForeignKey para um modelo de Categoria
"""

# Codigo Resolvido: 
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()  # Adicionado para armazenar uma descrição do produto
    # Melhoria: armazenar uma descrição completa do produto é importante para listas de produtos
    
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Alterado para permitir preços com até 8 dígitos inteiros e 2 decimais
    
    criado_em = models.DateTimeField(auto_now_add=True)  # Adicionado para armazenar a data de criação do produto automaticamente
    
    # Melhoria: Registra automaticamente a data de criação do produto

    def __str__(self):
        return self.nome