#parent and child classes
class Animal:
    def __init__(self, habitat, classe):
        self.habitat = habitat
        self.classe = classe

    def som(self):
        return "???"

# Cachorro herda de animal --> cachorro é automaticamente um animal assim
class Cachorro(Animal):
    def __init__(self, habitat, cor_pelo):
        self.cor_pelo = cor_pelo
        #especificar quem quer usar o init
        #super utiliza o método de outra classe
        super().__init__(habitat, "Mamifero")

    def som(self):
        return "AU AU"

class Cachorro_do_mato(Cachorro):
    pass

class Lagarto(Animal):
    def __init__(self, habitat):
        super().__init__(habitat, "Réptil")

    # def som(self):
    #     return "???"

class Pato(Animal):
    def __init__(self, habitat):
        # tipo public e private
        self.__atributo_secreto = "O pato tem quantas patas?"
        super().__init__(habitat, "Ave")

    def som(self):
        return "Quack"
    
    def contar_segredo(self):
        return self.__atributo_secreto

#encapsulamento
pato = Pato("Lagoa")
print(pato.som())
print(pato.contar_segredo())

#polimorfismo
cachorro = Cachorro("Doméstico", "Marrom")
lagarto = Lagarto("Floresta")

zoologico = [pato, cachorro, lagarto]

for animal in zoologico:
    print(f"O {type(animal).__name__} faz {animal.som()}")
