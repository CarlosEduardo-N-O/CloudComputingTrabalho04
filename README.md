# API de Ingressos para Eventos

API REST desenvolvida como Trabalho Final da disciplina de Cloud Computing — UNIDAVI.

## Tecnologias
- Python 3.11
- Flask
- pytest
- GitHub Actions (CI)

## Pré-requisitos
- Python 3.11 instalado
- pip disponível no terminal

## Como executar localmente

### 1. Clone o repositório
git clone https://github.com/seu-usuario/ingressos-api.git
cd ingressos-api

### 2. Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  (Windows)

### 3. Instale as dependências
pip install -r requirements.txt

### 4. Execute a API
python api/app.py

A API estará disponível em: http://localhost:5000

## Rotas disponíveis

| Método | Rota               | Descrição                        |
|--------|--------------------|----------------------------------|
| GET    | /status            | Retorna status da aplicação      |
| GET    | /ingressos         | Lista todos os ingressos         |
| GET    | /ingressos/{id}    | Retorna um ingresso pelo ID      |

## Como executar os testes
pytest api/tests/ -v

## Estrutura de diretórios
ingressos-api/
├── api/
│   ├── app.py
│   ├── data/
│   │   └── ingressos.json
│   └── tests/
│       └── test_api.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── requirements.txt
└── README.md