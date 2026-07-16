# Importa a classe FastAPI e a classe HTTPException para tratar erros
from fastapi import FastAPI, HTTPException

# Cria a instância da aplicação FastAPI, que será usada para definir rotas e configurações
app = FastAPI()

# Define uma rota HTTP GET no caminho raiz "/"
@app.get("/")
def hello_world():
    """
    Função associada ao endpoint raiz.
    Retorna uma mensagem de boas-vindas em formato JSON.
    """
    return {"mensagem": "Olá, mundo! 🌍"}


# Lista fictícia de figurinhas (simulando um banco de dados)
FIGURINHAS = [
    {"id": 1, "nome": "Alan Turing", "categoria": "IA"},
    {"id": 2, "nome": "John McCarthy", "categoria": "IA"}
]


# Define uma rota HTTP GET no caminho "/figurinhas" para listar as figurinhas
@app.get("/figurinhas")
def listar_figurinhas():
    """
    Função associada ao endpoint /figurinhas.
    Retorna uma lista com duas figurinhas de exemplo.
    """
    return FIGURINHAS


# Define uma rota HTTP GET no caminho "/figurinhas/{figurinha_id}" para obter uma figurinha pelo ID
@app.get("/figurinhas/{figurinha_id}")
def obter_figurinha(figurinha_id: int):
    """
    Função associada ao endpoint /figurinhas/{figurinha_id}.
    Busca e retorna uma figurinha específica com base no ID fornecido na rota.
    Caso o ID não exista, lança uma exceção HTTP 404.
    """
    # Procura a figurinha na lista de figurinhas
    for figurinha in FIGURINHAS:
        if figurinha["id"] == figurinha_id:
            return figurinha
    
    # Se não encontrar, lança um erro HTTP 404 (Not Found)
    raise HTTPException(status_code=404, detail="Figurinha não encontrada")