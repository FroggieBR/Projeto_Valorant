from django.contrib import admin
from .models import Mapa, Personagem, Arma, Partida

@admin.register(Mapa)
class MapaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'imagem')
    search_fields = ('nome', 'descricao')
    list_filter = ('nome',)

@admin.register(Personagem)
class PersonagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'funcao', 'sexo', 'origem', 'imagem')
    search_fields = ('nome', 'origem', 'habilidades')
    list_filter = ('funcao', 'sexo')

@admin.register(Arma)
class ArmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'descricao', 'imagem')
    search_fields = ('nome', 'descricao')
    list_filter = ('tipo',)

@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = ('data', 'hora', 'placar_time_1', 'placar_time_2', 'mapa')
    search_fields = ('mapa__nome',)
    list_filter = ('data', 'mapa')

