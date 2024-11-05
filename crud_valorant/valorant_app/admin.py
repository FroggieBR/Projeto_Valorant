from django.contrib import admin
from .models import Mapa, Personagem, Arma, Partida

# Registre seus modelos no admin aqui
@admin.register(Mapa)
class MapaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']  # Adicione os campos que você deseja visualizar no admin

@admin.register(Personagem)
class PersonagemAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'habilidade']  # Adicione os campos que você deseja visualizar no admin

@admin.register(Arma)
class ArmaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo']  # Adicione os campos que você deseja visualizar no admin

@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'mapa', 'resultado']  # Adicione os campos que você deseja visualizar no admin
