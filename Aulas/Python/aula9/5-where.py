import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM clientes
WHERE id = ?;
""", (1,))
# pode usar [1] para retornar lista, ao invés de (1,) que retorna tupla

print(cursor.fetchone())

cursor.execute("""
SELECT * FROM clientes
WHERE idade > ?;
""", (21,))

print(cursor.fetchall())

# % para procurar por palavra%
# Ex: %Belo = cidade que termina em Belo
# Belo% = cidade que começa com belo
cursor.execute("""
SELECT * FROM clientes
WHERE cidade like '%Belo%';
""")

print(cursor.fetchall())

conn.close()