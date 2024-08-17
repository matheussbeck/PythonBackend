import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "meubanco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

def criar_tabela(conexao,cursor):
    cursor.execute ('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VACHAR(100), email VARCHAR(150))')
    conexao.commit()


def inserir_registro(conexao,cursor,nome,email):
    data = (nome,email)
    cursor.execute (f"INSERT INTO clientes(nome,email) VALUES(?,?)",data)
    conexao.commit()


def atualizar_registro(conexao,cursor,nome,email,id):
    data = (nome,email,id)
    cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?;', data)
    conexao.commit()


def excluir_registro(conexao,cursor,id):
    data = (id,)
    cursor.execute('DELETE FROM clientes WHERE id=?;', data)
    conexao.commit()


def inserir_lote_registros(conexao,cursor,dados):
    cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?,?)', dados)
    conexao.commit()


def mostrar_registro(conexao,cursor,id):
    try:
        cursor.execute('SELECT * FROM clientes WHERE id=?',dados)
        return cursor.fetchone()
    

def mostrar_todos_alfabetico(cursor):
    return cursor.execute('SELECT * FROM clientes ORDER BY nome DESC;')



cursor.execute('SELECT * FROM clientes WHERE id = 1')

clientes = mostrar_todos_alfabetico(cursor)
for cliente in clientes:
    print(dict(cliente))

cliente = mostrar_registro(cursor, 2)
print(dict(cliente))
print(cliente["id"])
