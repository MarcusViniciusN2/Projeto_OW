import pandas as pd
import sqlite3

csv_path = "dados_ow.csv"
db_path = "base_overwatch.db"

conn = sqlite3.connect(db_path)

df = pd.read_csv(csv_path, sep = ";")

df.to_sql(
    "hero_info",
    conn,
    if_exists="append",  # append para não sobrescrever
    index=False
)

conn.close()

print("✅ Dados importados com sucesso!")
