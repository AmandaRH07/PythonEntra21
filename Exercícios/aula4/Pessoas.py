class Pessoa():
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class Pessoa1(Pessoa):
    def __init__(self, idade):
        super().__init__("Amanda", idade, "123.456.890-12")

class Pessoa2(Pessoa):
    def __init__(self, idade):
        super().__init__("Luana", idade, "098.765.432-11")