import pandas as pd
import sqlite3

# Caminhos
csv_path = "dados_ow.csv"
db_path = "base_overwatch.db"

# Conectar ao banco SQLite
conn = sqlite3.connect(db_path)

# Ler CSV
df = pd.read_csv(csv_path, sep = ";")

# Inserir no banco
df.to_sql(
    "hero_info",
    conn,
    if_exists="append",  # append para não sobrescrever
    index=False
)

# Fechar conexão
conn.close()

print("✅ Dados importados com sucesso!")
