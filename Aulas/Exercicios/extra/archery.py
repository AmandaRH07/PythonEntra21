# Crie uma classa arco, com as caracteristicas básicas de um arco
# Utilizando herança, crie pelo menos mais 3 classes de arco com suas respectivas caracteristicas

# Referências
# https://gearjunkie.com/archery-bow-types-hunting-bowhunting
# https://scottisharchery.org.uk/get-started/archery-bow-types

# Super Bonus: Crie uma classe para cada parte do arco e altere a classe pai arco, utilizando cada parte para cria-la

class Arco:
    def __init__(self, riser, peso):
        self.riser = riser
        self.peso = peso

class Recurve(Arco):
    def __init__(self, arco:Arco, par_membros_fixados):
        self.par_membros_fixados = par_membros_fixados
        super().__init__(arco, "Tem par de membros fixados")
        #super().__init__(arco1, "leve", par_membros_fixados)

    def mostrar(self):
        return f"{self.riser}, {self.peso}, {self.par_membros_fixados}"

class Longbow(Arco):
    def __init__(self, arco:Arco, funcionalidade):
        self.funcionalidade = funcionalidade
        super().__init__(arco, "Caça")

    def mostrar(self):
         return f"{self.riser}, {self.peso}, {self.funcionalidade}"


class Compound(Arco):
    def __init__(self, arco:Arco, precisao):
        self.precisao = precisao
        super().__init__(arco, "longa distância")

    def mostrar(self):
         return f"{self.riser}, {self.peso}, {self.precisao}"

if __name__ == "__main__":
    #recurve = Recurve("madeira","Tem par de membros fixados")
    recurve = Recurve("madeira","leve")
    print(recurve.mostrar())

    longbow = Longbow("madeira", "quanto maior mais pesado é")
    print(longbow.mostrar())

    compound= Compound("materiais compostos", "muito leve")
    print(compound.mostrar())
    
