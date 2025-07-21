import sqlite3
from config import Config
from datetime import datetime
from models.github_link import GithubLink
from typing import Optional

def get_github_link(user_id: int, resource_link_id: int) -> Optional[GithubLink]:
    conn = sqlite3.connect(Config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT github_url FROM github_vinculos WHERE user_id=? AND resource_link_id=?", (user_id, resource_link_id))
    row = cursor.fetchone()
    conn.close()
    return row

def save_github_link(user_id:int , resource_link_id: int, url: str):
    conn = sqlite3.connect(Config.DB_PATH)
    cursor = conn.cursor()
    now = datetime.now().isoformat()
    cursor.execute("INSERT OR REPLACE INTO github_vinculos (user_id, resource_link_id, github_url, data_envio, ultima_alteracao) VALUES (?, ?, ?, ?, ?)",
                   (user_id, resource_link_id, url, now, now))
    cursor.execute("INSERT INTO github_alteracoes (user_id, resource_link_id, github_url, data_alteracao) VALUES (?, ?, ?, ?)",
                   (user_id, resource_link_id, url, now))
    conn.commit()
    conn.close()