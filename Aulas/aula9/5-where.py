import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM clientes
WHERE id = ?;
""", (1,))

print(cursor.fetchone())

cursor.execute("""
SELECT * FROM clientes
WHERE idade > ?;
""", (21,))

print(cursor.fetchall())

cursor.execute("""
SELECT * FROM clientes
WHERE cidade like '%Belo%';
""")

print(cursor.fetchall())

conn.close()