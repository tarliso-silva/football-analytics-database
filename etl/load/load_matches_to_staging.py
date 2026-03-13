import pandas as pd
import psycopg2

# caminho do dataset
csv_path = "datasets/brazil_serie_a.csv"

# ler CSV
df = pd.read_csv(csv_path)

print("Linhas carregadas do CSV:", len(df))

# conexão com PostgreSQL (Neon)
conn = psycopg2.connect(
    host="ep-young-tree-ac215vw3-pooler.sa-east-1.aws.neon.tech",
    database="neondb",
    user="neondb_owner",
    password="npg_9qVOo0rKIzEs",
    port=5432,
    sslmode="require"
)

cursor = conn.cursor()

# inserir dados
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO staging.football_data_matches
        (country, league, season, date, time, home, away, hg, ag, res)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        row["Country"],
        row["League"],
        row["Season"],
        row["Date"],
        row["Time"],
        row["Home"],
        row["Away"],
        row["HG"],
        row["AG"],
        row["Res"]
    ))

conn.commit()

print("Dados carregados na staging!")

cursor.close()
conn.close()