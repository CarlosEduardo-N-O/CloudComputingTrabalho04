import pytest
import sys
import os

# Permite importar o app.py que está na pasta pai (api/)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


@pytest.fixture
def client():
    """Cria um cliente de teste para simular requisições HTTP."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# TESTE 1 — GET /ingressos deve retornar HTTP 200
def test_listar_ingressos_retorna_200(client):
    response = client.get("/ingressos")
    assert response.status_code == 200


# TESTE 2 — JSON retornado deve ter os campos obrigatórios
def test_estrutura_json_ingressos(client):
    response = client.get("/ingressos")
    dados = response.get_json()
    assert isinstance(dados, list)
    assert len(dados) > 0
    primeiro = dados[0]
    assert "id" in primeiro
    assert "evento" in primeiro
    assert "local" in primeiro
    assert "preco" in primeiro
    assert "disponivel" in primeiro


# TESTE 3 — ID inexistente deve retornar HTTP 404
def test_id_inexistente_retorna_404(client):
    response = client.get("/ingressos/9999")
    assert response.status_code == 404


# TESTE 4 — (autoria própria) Lista deve conter exatamente 10 ingressos
# Justificativa: garante que o arquivo JSON não foi corrompido ou alterado
# acidentalmente, assegurando a integridade do dataset da aplicação.
def test_total_de_ingressos_e_dez(client):
    response = client.get("/ingressos")
    dados = response.get_json()
    assert len(dados) == 10