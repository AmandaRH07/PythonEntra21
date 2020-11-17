#sqlite3 já faz parte do python :D
import sqlite3

# isso cria o banco, caso não exista!
conn = sqlite3.connect('clientes.db')


# para fazermos nossas operações, sempre precisaremos de um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        cpf     VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        fone TEXT,
        cidade TEXT,
        uf VARCHAR(2) NOT NULL,
        criado_em DATE NOT NULL
);
""")

print('Tabela criada com sucesso.')
# isso fecha a conexão
conn.close()