import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Cria a instância da aplicação FastAPI para configurar as rotas e o servidor
app = FastAPI()

# Define o caminho absoluto da pasta de imagens para garantir que o servidor localize a pasta em qualquer ambiente
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Configura os arquivos estáticos montando o diretório de imagens na rota "/imgs"
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# Lista contendo as figurinhas de exemplo com seus dados e a URL correspondente para a imagem estática
figurinhas = [
    {
        "id": 1,
        "nome": "Alan Turing",
            "categoria": "IA",
        "imagem_url": "/imgs/01-alan-turing.jpg"
    },
    {
        "id": 2,
        "nome": "John McCarthy",
        "categoria": "IA",
        "imagem_url": "/imgs/02-john-mccarthy.jpg"
    }
]


# Endpoint único GET "/figurinhas" que retorna a lista de figurinhas
@app.get("/figurinhas")
def listar_figurinhas():
    """
    Função associada ao endpoint /figurinhas.
    Retorna a lista de figurinhas contendo informações e caminhos de imagem.
    """
    return figurinhas

# Constante total do álbum
TOTAL_ALBUM = 25

# Função para calcular estatísticas do álbum a partir da lista de figurinhas
def estatisticas_album():
    """
    Calcula estatísticas do álbum a partir da lista de figurinhas.
    - coladas: número de figurinhas presentes.
    - faltam: quantidade restante para completar o álbum.
    """
    coladas = len(figurinhas)
    faltam = TOTAL_ALBUM - coladas
    return {"total_album": TOTAL_ALBUM, "coladas": coladas, "faltam": faltam}

# Endpoint GET "/figurinhas/total" que devolve as estatísticas do álbum
@app.get("/figurinhas/total")
def get_estatisticas():
    """Retorna as estatísticas do álbum de figurinhas."""
    return estatisticas_album()