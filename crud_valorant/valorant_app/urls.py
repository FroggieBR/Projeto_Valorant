from rest_framework.routers import DefaultRouter
from .views import MapaViewSet, PersonagemViewSet, ArmaViewSet, PartidaViewSet

router = DefaultRouter()
router.register(r'mapas', MapaViewSet)
router.register(r'personagens', PersonagemViewSet)
router.register(r'armas', ArmaViewSet)
router.register(r'partidas', PartidaViewSet)

urlpatterns = router.urls