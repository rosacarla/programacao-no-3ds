import sqlite3
import json

def conectar():
    conn = sqlite3.connect("clientes.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            codigo TEXT PRIMARY KEY,
            dados TEXT
        )
    """)
    return conn

def salvar_cliente(cliente):
    conn = conectar()
    dados_json = json.dumps(cliente.to_dict())
    conn.execute("REPLACE INTO clientes (codigo, dados) VALUES (?, ?)", (cliente.codigo, dados_json))
    conn.commit()
    conn.close()

def buscar_cliente(codigo):
    conn = conectar()
    cursor = conn.execute("SELECT dados FROM clientes WHERE codigo = ?", (codigo,))
    row = cursor.fetchone()
    conn.close()
    return json.loads(row[0]) if row else None

def apagar_cliente(codigo):
    conn = conectar()
    conn.execute("DELETE FROM clientes WHERE codigo = ?", (codigo,))
    conn.commit()
    conn.close()
