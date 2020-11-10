class Computador:
    #Construtor
    def __init__(self, marca, identificador):
        self.marca = marca
        self.identificador = identificador

    def __str__(self):
        pass
    
    def ligar(self):
        if self.identificador:
           return "Computador Inicializado"
        else:
            return "..."
