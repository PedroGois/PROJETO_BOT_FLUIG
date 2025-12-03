import sqlite3

def init_db():
    conn = sqlite3.connect("data/chamados.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS enviados (
            id_chamado TEXT PRIMARY KEY
        )
    """)
    conn.commit()
    conn.close()

def ja_enviado(id_chamado):
    conn = sqlite3.connect("data/chamados.db")
    c = conn.cursor()
    c.execute("SELECT * FROM enviados WHERE id_chamado = ?", (id_chamado,))
    r = c.fetchone()
    conn.close()
    return r is not None

def marcar_como_enviado(id_chamado):
    conn = sqlite3.connect("data/chamados.db")
    c = conn.cursor()
    c.execute("INSERT INTO enviados VALUES (?)", (id_chamado,))
    conn.commit()
    conn.close()