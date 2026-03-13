# biblioteca usada para fazer requisições HTTP
import requests

# biblioteca para trabalhar com caminhos de arquivos de forma segura
from pathlib import Path


# ------------------------------------------------------------
# CONFIGURAÇÃO DO PIPELINE
# ------------------------------------------------------------

# lista de competições que queremos baixar
# o site football-data usa códigos padronizados para cada liga
#
# exemplos:
# BRA = Brasileirão
# E0  = Premier League
# SP1 = La Liga
# I1  = Serie A
# D1  = Bundesliga
COMPETITIONS = [
    "BRA"
]

# URL base usada pelo site para disponibilizar os CSVs
BASE_URL = "https://www.football-data.co.uk/new/{}.csv"


# ------------------------------------------------------------
# PREPARAÇÃO DA PASTA DE DESTINO
# ------------------------------------------------------------

# definimos a pasta onde os datasets brutos serão armazenados
DATASET_DIR = Path("datasets/raw")

# cria a pasta caso ela ainda não exista
DATASET_DIR.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# DOWNLOAD DOS DATASETS
# ------------------------------------------------------------

# percorre cada competição definida na lista
for competition in COMPETITIONS:

    # monta a URL do dataset usando o código da competição
    url = BASE_URL.format(competition)

    # define o nome do arquivo que será salvo
    # exemplo final: datasets/raw/BRA.csv
    output_file = DATASET_DIR / f"{competition}.csv"

    print(f"Baixando dataset da competição: {competition}")

    # faz a requisição HTTP para baixar o arquivo
    response = requests.get(url)

    # salva o conteúdo do CSV no arquivo local
    with open(output_file, "wb") as f:
        f.write(response.content)

    print(f"Arquivo salvo em: {output_file}")