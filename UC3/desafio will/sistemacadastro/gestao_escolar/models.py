from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    salario = models.DecimalField(max_digits=10, decimal_places=2) # - casas decimais (importante para cenvados .o. ) (wll ganha 200 por mes)
    data_cadastro = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    ativo = models.BooleanField(default=True)
    def __str__(self):
     return self.nome  # corrinfdo o  " object 1" jango não entende aquik por padrão

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    data_cadastro = models.DateField()
    ativa = models.BooleanField(default=True)
    
    def __str__(self):
       return self.nome  # corrinfdo o  " object 1"

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    data_cadastro = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True) # -> se for deletadso sera colocada como NUll (importante) - imoprta do modulo turmas, turmas criadas
    data_nascimento = models.DateField()
    ativo = models.BooleanField(default=True)
    def __str__(self):
     return self.nome  # corrinfdo o  " object 1" -> django não entende aquik por padrão
