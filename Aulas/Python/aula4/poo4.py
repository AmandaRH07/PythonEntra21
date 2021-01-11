class Animal:
    """
        Essa classe representa todos os animais do universo!
    """
    def __init__(self):
        """
            Essa classe inicializa um animal!
            Não é necessário parametro porque blablablaba.....
        """
        pass

    def __str__(self):
        return "Este é um animal!"

    def som():
        """
        Esse método apresenta o barulho do bichinho!
        """

class Pokemon(Animal):
    def __init__(self):
        pass
   

animal = Animal()
print(animal.__doc__)
print(animal.som.__doc__)
print(animal.__module__)

print(Pokemon.__bases__)
print(Pokemon.__name__)