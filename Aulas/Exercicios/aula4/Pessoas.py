class Pessoa():
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class NovaPessoa(Pessoa):
    def __init__(self, nome,idade,cpf):
        super().__init__(nome, idade, cpf)
