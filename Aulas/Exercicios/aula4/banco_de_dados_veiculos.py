import sqlite3

conn = sqlite3.connect("C:\Entra21_Python\Aulas\Exercicios\Aula4\Veiculos.db")
cursor = conn.cursor()

def add_colunas(parametro):
    try:      
        cursor.execute(f"""
        ALTER TABLE veiculos
        ADD COLUMN "{parametro}" TEXT;
        """)
        conn.commit()
        print("Colunas criadas com sucesso")
        conn.close()
    except:
        print("Alteração já foi feita, ou deu erro")

# add_colunas("nome")
# add_colunas("modelo")
# add_colunas("ano")
# add_colunas("placa")
# add_colunas("proprietario")
# add_colunas("num_portas")
# add_colunas("qtd_passageiros")
# add_colunas("motor")
# add_colunas("meio_locomocao")

id_veiculos = 0
def atualiza_informacoes(id_veiculos, nome, modelo, ano, placa, proprietario, num_portas, qtd_passageiros, motor, meio_locomocao):
    cursor.execute("""
    UPDATE veiculos
    SET nome = ?, modelo = ?, ano = ?, placa = ?,proprietario = ?, num_portas = ?, qtd_passageiros = ?, motor = ?, 
    meio_locomocao = ?
    WHERE id = ?
    """, (nome, modelo, ano, placa, proprietario, num_portas, qtd_passageiros, motor, meio_locomocao,id_veiculos))
    conn.commit()

atualiza_informacoes(1,"Siena", "Sedan", "2017", "ABC-1234", "Amanda","4", "2", "1.0", "Carro")
conn.close()