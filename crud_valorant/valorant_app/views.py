from rest_framework.viewsets import ModelViewSet
from .serializers import *

# Create your views here.

class MapaViewSet(ModelViewSet):
    queryset = Mapa.objects.all()
    serializer_class = MapaSerializer

class PersonagemViewSet(ModelViewSet):
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer

class ArmaViewSet(ModelViewSet):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer

class PartidaViewSet(ModelViewSet):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer