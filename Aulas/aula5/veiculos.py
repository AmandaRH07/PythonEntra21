class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class Veiculo:
    __passageiros = []

    def __init__(self, marca, combustivel, max_passageiros, ambiente, num_rodas):
        self.marca = marca
        self.combustivel = combustivel
        self.max_passageiros = max_passageiros
        self.ambiente = ambiente
        self.num_rodas = num_rodas

    def adicionar_passageiro(self, pessoa:Pessoa):
        self.__passageiros.append(pessoa)
        
    def remover_passageiro(self, pessoa:Pessoa):
        pass

    def get_passageiros(self)-> list:
        return self.__passageiros

if __name__ == "__main__":
    p = Pessoa("Bruno", 29, "022.121.434-33")
    v = Veiculo("Volksvagem", "Gasolina", 5, "Terra", 4)

    v.adicionar_passageiro(p)

    print(v.get_passageiros())


