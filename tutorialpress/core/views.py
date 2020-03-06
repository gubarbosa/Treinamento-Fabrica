from rest_framework import serializers, viewsets

from tutorialpress.core.models import Publicacao


class PublicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacao
        fields = ["id", "titulo", "conteudo", "is_publicada"]


class PublicacaoViewSet(viewsets.ModelViewSet):
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializer
