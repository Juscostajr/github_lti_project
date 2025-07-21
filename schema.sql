CREATE TABLE IF NOT EXISTS github_vinculos (
    user_id TEXT NOT NULL,
    resource_link_id TEXT NOT NULL,
    github_url TEXT NOT NULL,
    data_envio TEXT,
    ultima_alteracao TEXT,
    PRIMARY KEY (user_id, resource_link_id)
);

CREATE TABLE IF NOT EXISTS github_alteracoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    resource_link_id TEXT NOT NULL,
    github_url TEXT NOT NULL,
    data_alteracao TEXT NOT NULL
);