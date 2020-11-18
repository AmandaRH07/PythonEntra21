import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# adicionando uma nova coluna na tabela clientes
# ...  BOOLEAN DEFAULT TRUE  vão todos com o mesmo valor
cursor.execute("""
ALTER TABLE clientes
ADD COLUMN bloqueado BOOLEAN;
""")

conn.commit()

print('Novo campo adicionado com sucesso.')

conn.close()
