import sqlite3
import os

DATABASE_NAME = 'Banco_de_dados.db'
DATABASE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), DATABASE_NAME)

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute(""" 
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
                 
        ) 
    """)
    conn.commit()
    conn.close