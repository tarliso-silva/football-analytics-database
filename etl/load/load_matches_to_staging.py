# ------------------------------------------------------------
# IMPORTAÇÃO DE BIBLIOTECAS
# ------------------------------------------------------------

import pandas as pd
import psycopg2
from pathlib import Path


# ------------------------------------------------------------
# CONFIGURAÇÃO
# ------------------------------------------------------------

# caminho do CSV bruto
DATASET_PATH = Path("datasets/raw/BRA.csv")


# ------------------------------------------------------------
# LEITURA DO CSV
# ------------------------------------------------------------

print("Lendo dataset...")

df = pd.read_csv(DATASET_PATH)


# ------------------------------------------------------------
# TRATAMENTO DE VALORES NULOS
# ------------------------------------------------------------

# converte NaN do pandas para None (NULL no PostgreSQL)
df = df.astype(object).where(pd.notnull(df), None)

print(f"Linhas encontradas no CSV: {len(df)}")


# ------------------------------------------------------------
# CONEXÃO COM O POSTGRESQL
# ------------------------------------------------------------

print("Conectando ao banco...")

conn = psycopg2.connect(
    host="ep-young-tree-ac215vw3-pooler.sa-east-1.aws.neon.tech",
    database="neondb",
    user="neondb_owner",
    password="npg_9qVOo0rKIzEs",
    port=5432,
    sslmode="require"
)

cursor = conn.cursor()


# ------------------------------------------------------------
# INSERÇÃO DOS DADOS
# ------------------------------------------------------------

print("Inserindo dados na tabela staging...")

for _, row in df.iterrows():

    cursor.execute("""
        INSERT INTO staging.football_data_matches
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s)
    """, tuple(row))


# ------------------------------------------------------------
# FINALIZAÇÃO
# ------------------------------------------------------------

conn.commit()

print("Carga concluída!")

cursor.close()
conn.close()