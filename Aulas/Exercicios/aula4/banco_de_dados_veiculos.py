import sqlite3

conn = sqlite3.connect("C:\Entra21_Python\Aulas\Exercicios\Aula4\Veiculos.db")
cursor = conn.cursor()

try:      
    cursor.execute("""
    ALTER TABLE veiculos
    ADD COLUMN meio_locomocao TEXT;
    """)
    conn.commit()
    print("Colunas criadas com sucesso")
    conn.close()
except:
    print("Alteração já foi feita, ou deu erro")

def atualiza_informacoes(id_veiculos, nome, modelo, ano, placa, proprietario,
    num_portas, km_rodado, qtd_passageiros, motor, meio_locomocao):
    cursor.execute("""
    UPDATE veiculos
    SET nome = ?, modelo = ?, ano = ?, placa = ?,proprietario = ?, 
    num_portas = ?, km_rodado = ?, qtd_passageiros = ?, motor = ?, 
    meio_locomocao = ?
    WHERE id = ?
    """, (nome, modelo, ano, placa, proprietario, num_portas, 
    km_rodado, qtd_passageiros, motor, meio_locomocao, id_veiculos,))
    conn.commit()

atualiza_informacoes("Siena", "Sedan", "2017", "ABC-1234", "Amanda",
                        4, 0, 2, "1.0", "Carro",5)
print("teset")
conn.close()

# cursor.execute("""
# ALTER TABLE veiculos
# ADD COLUMN nome TEXT;
# """)
# cursor.execute("""
# ALTER TABLE veiculos
# ADD COLUMN modelo TEXT;
# """)
# cursor.execute("""
# ALTER TABLE veiculos
# ADD COLUMN ano TEXT;
# """)
# cursor.execute("""
# ALTER TABLE veiculos
# ADD COLUMN placa TEXT;
# """)    
#  cursor.execute("""
# ALTER TABLE veiculos
# ADD COLUMN proprietario TEXT;
#  """)
# cursor.execute("""
# ALTER TABLE veiculos
# ADD COLUMN num_portas INTEGER;
# """)
# cursor.execute("""
# ALTER TABLE veiculos
# ADD COLUMN km_rodado INTEGER;
# """)
# cursor.execute("""
# ALTER TABLE veiculos
# ADD COLUMN qtd_passageiros INTEGER;
# """)
# cursor.execute("""
# ALTER TABLE veiculos
# ADD COLUMN motor TEXT;
# """)
# cursor.execute("""
# ALTER TABLE veiculos
# ADD COLUMN meio_locomocao TEXT;
# """)
