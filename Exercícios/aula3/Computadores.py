class Computador:
    marca = "dell"
    modelo = "123"
    cor = "cinza"

    def __init__(self, marca, id):
        self.marca = marca
        self.id = id

    def ligar(self):
        print("Computador Inicializado")

