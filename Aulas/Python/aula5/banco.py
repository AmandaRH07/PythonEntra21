from veiculos import Pessoa

class Banco():
    def __init__(self):
        pass

class NuConta(Banco):
    def __init__(self):
        super().__init__()

class Viacredi(Banco):
    def __init__(self):
        super().__init__()

class Conta():
    def __init__(self, banco:Banco, pessoa: Pessoa):
        pass


if __name__ == "__main__":
    while True:
        valor = int(input(
            """Digite a operação desejada
            1 - Cadastrar Pessoa
            2 - Cadastrar Conta
            3 - Visualizar Saldo
            4 - Fazer um depósito
            5 - Sair\n"""))

        if(valor == 5):
            print("Agradecemos a sua visita!")
            break
