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
 # foto = models.ImageField(upload_to='fotos/', blank=True, null=True)  # Exemplo de campo para foto
