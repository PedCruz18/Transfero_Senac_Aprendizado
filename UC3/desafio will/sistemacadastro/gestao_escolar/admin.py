from django.contrib import admin
from .models import Professor, Aluno, Turma

# Registra os modelos para aparecerem no admin
@admin.register(Professor)
class AdminProfessor(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'status_ativo')
    list_filter = ('ativo',)
    search_fields = ('nome', 'sobrenome', 'email')
    
    def status_ativo(self, obj):
        return "✅ Ativo" if obj.ativo else "❌ Inativo"
    status_ativo.short_description = 'Status'

@admin.register(Aluno)
class AdminAluno(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'status_ativo')
    list_filter = ('ativo',)
    search_fields = ('nome', 'sobrenome', 'email')
    
    def status_ativo(self, obj):
        return "✅ Ativo" if obj.ativo else "❌ Inativo"
    status_ativo.short_description = 'Status'

@admin.register(Turma)
class AdminTurma(admin.ModelAdmin):
    list_display = ('id', 'nome', 'status_ativa')
    list_filter = ('ativa',)
    search_fields = ('nome',)
    
    def status_ativa(self, obj):
        return "✅ Ativa" if obj.ativa else "❌ Inativa"
    status_ativa.short_description = 'Status'