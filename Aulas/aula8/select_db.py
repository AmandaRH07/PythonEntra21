import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM clientes;
""")

#fetchall pega o retorno do comando
for linha in cursor.fetchall():
    print(linha)

#print(cursor.fetchall()[1])
conn.close()