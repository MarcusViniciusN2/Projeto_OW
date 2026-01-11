CREATE TABLE IF NOT EXISTS hero_info (
    hero_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    funcao TEXT NOT NULL,
    vida_total INTEGER,
    dano_primario_estimado INTEGER
);


