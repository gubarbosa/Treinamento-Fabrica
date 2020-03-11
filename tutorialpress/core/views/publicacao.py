from rest_framework import viewsets

from tutorialpress.core.models import Publicacao
from tutorialpress.core.serializers import PublicacaoSerializer, PublicacaoDetailSerializer


class PublicacaoViewSet(viewsets.ModelViewSet):
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializer
    lookup_field = "id"

    def get_serializer(self):
        if self.action == 'list' or self.action == "retrieve":
            return PublicacaoDetailSerializer()
        else:
            return PublicacaoSerializer()
