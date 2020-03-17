import pytest
from django.urls import reverse
from rest_framework import status

from tutorialpress.core.models import Categoria


@pytest.mark.django_db
def test_create_valid(api_client):
    # DADO dados de categoria válidos.
    dados_categoria = {"nome": "Categoria A"}

    # QUANDO a API é chamada para criar uma categoria.
    resp = api_client.post(reverse("categoria-list"), dados_categoria)

    # ENTÃO a resposta de sucesso deve conter os dados da categoria
    assert resp.status_code == status.HTTP_201_CREATED
    assert isinstance(resp.data["id"], int)

    # E ENTÃO a categoria deve existir no banco.
    assert Categoria.objects.get(pk=resp.data["id"]).nome == dados_categoria["nome"]


@pytest.mark.django_db
def test_create_invalid(api_client):
    # DADO dados de categoria inválidos.
    dados_categoria = {"campo_invalido": "123"}

    # QUANDO a API é chamada para criar uma categoria.
    resp = api_client.post(reverse("categoria-list"), dados_categoria)

    # ENTÃO a reposta de falha deve conter os erros de cada campo.
    assert resp.status_code == status.HTTP_400_BAD_REQUEST
    assert len(resp.data["nome"]) != 0

    # E ENTÃO a categoria não deve existir no banco.
    assert Categoria.objects.count() == 0


@pytest.mark.django_db
def test_retrieve_valid(api_client):
    categoria = Categoria.objects.create(nome="categoria1")
    resp = api_client.get(reverse("categoria-detail", args={categoria.id}))
    assert resp.status_code == status.HTTP_200_OK


# @pytest.mark.django_db
# def test_update(api_client):
#     categoria = Categoria.objects.update(nome="categoria1")
#     resp = api_client.put(reverse("categoria-detail", args={categoria.id}))
#     assert resp.status_code == status.HTTP_200_OK

# @pytest.mark.django_db
# def test_delete(api_client):
#     categoria = Categoria.objects.create(nome="categoria1")
#     resp = api_client.delete(reverse("categoria-detail", args={categoria.id}))
#     assert resp.status_code == status.HTTP_200_OK

@pytest.mark.django_db
batatapodre
