from rest_framework import serializers
from .models import Mapa, Personagem, Arma, Partida

class MapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapa
        fields = [
            "nome",
            "descricao",
            "imagem",
        ]
    
class PersonagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personagem
        fields = [
            "nome",
            "habilidades",
            "funcao",
            "sexo",
            "origem",
            "imagem",
        ]

class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = [
            "nome",
            "tipo",
            "descricao",
            "imagem",
        ]

class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partida
        fields = [
            "placar_time_1",
            "placar_time_2",
            "data",
            "hora",
            "mapa",
            "personagem",
        ]