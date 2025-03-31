from django.db import models
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
 nome = models.CharField(max_length=50)
 sobrenome = models.CharField(max_length=50)
 cpf = models.CharField(max_length=11)
 telefone = models.CharField(max_length=20)
 email = models.EmailField()
 endereco = models.CharField(max_length=100)
 data_cadastro = models.DateTimeField(default=timezone.now)
 ativo = models.BooleanField(default=True)
 imagem = models.ImageField(blank=True, upload_to='imagens/%Y/%m')
 
 def __str__(self):
  return f'{self.nome} {self.sobrenome}'
 # foto = models.ImageField(upload_to='fotos/', blank=True, null=True)  # Exemplo de campo para foto

class Genero(models.Model):
 nome = models.CharField(max_length=50)
 data_cadastro = models.DateField(default=timezone.now)

 def __str__(self):
  return self.nome

class Filme(models.Model):
 nome = models.CharField(max_length=50)
 ano = models.DateField(default=timezone.now)
 estudio = models.CharField(max_length=50)
 # genero = models.CharField(max_length=50)
 genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, blank=True)
 sinopse = models.TextField()
 data_cadastro = models.DateField(default=timezone.now)

 def __str__(self):
  return self.nome


# Filme - Nome do Filme, ano de lançamento, estúdio, gênero, sinopse
# Genêro - nome, data de cadastro