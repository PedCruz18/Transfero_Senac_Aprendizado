from django.contrib import admin
from sistema import models

@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
 list_display = ('id', 'nome', 'sobrenome', 'email', 'ativo',)
 
# Aqui fica o registro do filme
@admin.register(models.Filme)
class FilmeAdmin(admin.ModelAdmin):
 list_display = ('id', 'nome', 'ano', 'estudio', 'genero',)

# Aqui fica o registro do Gênero
@admin.register(models.Genero)
class GeneroAdmin(admin.ModelAdmin):
 list_display =('id', 'nome',)