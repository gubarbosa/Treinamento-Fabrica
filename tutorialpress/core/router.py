from rest_framework import routers
from tutorialpress.core.views import PublicacaoViewSet, CategoriaViewSet

router = routers.SimpleRouter()
router.register("publicacoes", PublicacaoViewSet)
router.register("categorias", CategoriaViewSet)
