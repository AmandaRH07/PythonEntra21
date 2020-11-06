class Xicara:
    capacidade = "250"
    acompanhamento = "Adocante"
    cor = "vermelha"

    def __init__(self, bebida, ml, acompanhamento):
        self.bebida = bebida
        self.ml = ml
        self.acompanhamento = acompanhamento

    def tipoBebida(self):
        print("Café")

if __name__ == "__main__":
   x = Xicara("Chá", 150, "Acúcar")
   print(x)

   print(isinstance(x, Xicara))
