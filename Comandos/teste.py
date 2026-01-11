import pandas as pd
import sqlite3

# Caminhos
csv_path = "dados_ow.csv"
db_path = "base_overwatch.db"

# Conectar ao banco SQLite
conn = sqlite3.connect(db_path)

# Ler CSV
df = pd.read_csv(csv_path, sep = ";")

print(df.columns)

