passageiros = []

class Veiculo():
    global passageiros

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

    def addPassageiro(self):
        add_Nome = input("Insira o nome: ")
        add_Idade = input("Insira a idade: ")
        add_CPF = input("Insira o cpf: ")
        super().__init__(add_Nome, add_Idade, add_CPF)
        #return nome, idade, cpf
    
    def removePassageiro(self, nome):
        remove_Passageiro = input("Insira o nome da pessoa a ser removida: ")
        if remove_Passageiro == nome:
            passageiros.remove(nome)

    def listarPassageiros(self):
        print("\nLista de Passageiros: ")
        for passageiro in passageiros:
            print(f"{passageiro.nome}")

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