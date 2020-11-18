from Pessoas import Pessoa, NovaPessoa
import sqlite3

passageiros = []
teste = True
conn = sqlite3.connect("C:\Entra21_Python\Aulas\Exercicios\Aula4\Veiculos.db")

class Veiculo():
    global passageiros
    global menu

    def __init__(self, fabricante, qtd_rodas, combustivel, qtd_lugares, cor ):
        self.fabricante = fabricante
        self.qtd_rodas = qtd_rodas
        self.combustivel = combustivel
        self.qtd_lugares = qtd_lugares
        self.cor = cor
        
    def buzina(self):
        return "..."

    def ocopacao(self):
        return "..."

    def addPassageiro(self,pessoa:Pessoa):
        self.pessoa = pessoa
        #self.passageiros.append(pessoa)
        teste = False
        
    def removePassageiro(self):
        remove_Passageiro = input("Insira o nome da pessoa a ser removida: ")
        for passageiro in passageiros:
            if remove_Passageiro == passageiro:
                passageiros.remove(passageiro)
        teste = False

    def listarPassageiros(self):
        print("\nLista de Passageiros: ")
        for passageiro in passageiros:
            print(f"{passageiro}")
        teste = False

class Carro(Veiculo):
    def __init__(self,fabricante):
        super().__init__(fabricante, "4", "Diesel", "5", "Preto")

    def buzina(self):
        return "beeeep"

    def ocupacao(self):
        return "o carro está com 3 lugares ocupados "

class Moto(Veiculo):
    def __init__(self, qtd_lugares):
        super().__init__("Honda",qtd_lugares, "Gasolina", "2", "Prata")

    def buzina(self):
        return "bepbep"

    def ocupacao():
        return "a moto está com 1 lugar ocupado "

class Bicicleta(Veiculo):
    def __init__(self,cor):
        super().__init__("Caloy", "2","Não se aplica", "1", cor)

############ BANCO DE DADOS ############
cursor = conn.cursor()

try:
    cursor.execute(""" 
    CREATE TABLE veiculos(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        fabricante TEXT NOT NULL,
        qtd_rodas TEXT NOT NULL,
        combustivel TEXT NOT NULL,
        qtd_lugares TEXT NOT NULL,
        cor  TEXT NOT NULL
    );
    """)
    print("Tabela criada")
except:
    print("Tabela já foi criada")

cursor.execute("""
INSERT INTO veiculos (fabricante, qtd_rodas, combustivel, qtd_lugares, cor )
VALUES ("Fiat", "4", "Diesel", "5", "Preto" )
""")
conn.commit()

cursor.execute("""
SELECT * FROM veiculos;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()