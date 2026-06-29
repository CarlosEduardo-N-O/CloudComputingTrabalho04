from flask import Flask, jsonify
import json
import os

app = Flask(__name__)


def carregar_dados():
    """Lê o arquivo JSON externo com os dados dos ingressos."""
    caminho = os.path.join(os.path.dirname(__file__), "data", "ingressos.json")
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


@app.route("/status")
def status():
    """Rota de saúde da API."""
    return jsonify({
        "nome": "API de Ingressos para Eventos",
        "versao": "1.0.0",
        "status": "online"
    }), 200


@app.route("/ingressos")
def listar_ingressos():
    """Retorna todos os ingressos disponíveis."""
    dados = carregar_dados()
    return jsonify(dados), 200


@app.route("/ingressos/<int:id>")
def buscar_ingresso(id):
    """Retorna um ingresso específico pelo ID."""
    dados = carregar_dados()
    ingresso = next((item for item in dados if item["id"] == id), None)
    if ingresso is None:
        return jsonify({"erro": "Ingresso não encontrado"}), 404
    return jsonify(ingresso), 200


if __name__ == "__main__":
    app.run(debug=True)
