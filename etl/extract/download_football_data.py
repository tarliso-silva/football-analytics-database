import requests
from pathlib import Path

# URL do dataset (exemplo: Brasileirão 2023)
URL = "https://www.football-data.co.uk/new/BRA.csv"

# Pasta onde os datasets ficarão
DATASET_DIR = Path("datasets")
DATASET_DIR.mkdir(exist_ok=True)

# Caminho do arquivo
output_file = DATASET_DIR / "brazil_serie_a_2023.csv"

print("Baixando dataset...")

response = requests.get(URL)

with open(output_file, "wb") as f:
    f.write(response.content)

print("Download concluído:", output_file)