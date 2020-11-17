import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# vamos inserir valores na nossa tabela 
cursor.execute("""
    INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES ('Outra_pessoa', 52, '1111111111', 'outra@email.com', '11-98765-4321', 'Sao Paulo', 'SP', '2014-06-08')
""")


# grava no DB
conn.commit()

conn.close()