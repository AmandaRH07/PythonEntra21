#sqlite3 já faz parte do python :D
import sqlite3

# isso cria o banco, caso não exista!
conn = sqlite3.connect('super_cliente.db')


# para fazermos nossas operações, sempre precisaremos de um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.executescript("""
CREATE TABLE cidades (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	cidade TEXT UNIQUE,
	uf VARCHAR(2)
);
CREATE TABLE pessoas (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	sobrenome TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	cidade_id INTEGER,
	criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,

	FOREIGN KEY (cidade_id) REFERENCES cidades(id)
);
""")
print('Tabelas criadas com sucesso.')

cursor.execute("""
    INSERT INTO cidades (cidade, uf)
        VALUES ("Plumenau","SC")
""")

cursor.execute("""
    INSERT INTO pessoas (nome, sobrenome, email, cidade_id)
        VALUES ("Bruno","Sadoski","bruno@gmail.com",1)
""")

#join junta os dados de tabelas dierentes
cursor.execute("""
    SELECT * FROM pessoas INNER JOIN cidades ON pessoas.cidade_id = cidades.id
""")
print(cursor.fetchall())

# isso fecha a conexão
conn.close()