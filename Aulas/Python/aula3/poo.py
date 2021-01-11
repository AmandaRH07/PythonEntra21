# Criando uma classe
class Cachorro:
    # atributo de classe
    especie = "Canis familiaris"

    # inicialização da classe
    def __init__(self, nome, idade):
        # atributos de instancia
        self.nome = nome
        self.idade = idade

    # alterando a descrição    
    #def __str__(self):
    #    return f"{self.nome} tem {self.idade} anos de idade"

    def emitir_som(self):
        print("Woof Woof")
    
if __name__ == "__main__":     
    c = Cachorro("Bilu", 10)
    print(c)

    # objeto cachorro?
    print(isinstance(c, Cachorro))

    c.emitir_som()