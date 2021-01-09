""" 
construa um analisador das 5 principais combinações de mãos do poker.
Para isso utilize como base as classes descritas em:
https://penseallen.github.io/PensePython2e/18-heranca.html
considere como regra o poker fechado, em que a mão do jogador, já tem a combinação de 5 cartas :)

"""

#import exercises as cabecalho
import random
from collections import Counter

#cabecalho.cabecalho("poker")

lista_cartas = []
lista_naipes = []

class Carta:
    """Represents a standard playing Carta.
    
    Attributes:
      naipe: integer 0-3
      carta: integer 1-13
    """
                    #  0,     1,        2,       3
    naipe_string = ["Paus", "Ouros", "Copas", "Espadas"]
    cartas_string = [None, "As", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Valete", "Dama", "Rei"]

    def __init__(self, naipe=0, carta=2):
        self.naipe = naipe
        self.carta = carta

    def __str__(self):
        """Returns a human-readable string representation."""

        return '%s de %s' % (Carta.cartas_string[self.carta],
                             Carta.naipe_string[self.naipe])

    def __eq__(self, outro):
        # """Checks whether self and outro have the same carta and naipe.
        # returns: boolean
        # """
        # return self.naipe == outro.naipe and self.carta == outro.carta
        pass

    def __lt__(self, outro):
        # """Compares this Carta to outro, first by naipe, then carta.
        # returns: boolean
        # """
        # t1 = self.naipe, self.carta
        # t2 = outro.naipe, outro.carta
        # return t1 < t2
        pass


class Baralho:
    """Represents a baralho of Cartas.
    Attributes:
      Cartas: list of Carta objects.
    """
    
    def __init__(self):
        """Initializes the Baralho with 52 Cartas.
        """
        self.cartas = []
        for naipe in range(4):
            for carta in range(1, 14):
                carta = Carta(naipe, carta)
                self.cartas.append(carta)

    def __str__(self):
        """Returns a string representation of the baralho.
        """
        res = []
        for carta in self.cartas:
            res.append(str(carta))
        return '\n'.join(res)

    def add_Carta(self, Carta):
        """Adds a Carta to the baralho.
        Carta: Carta
        """
        self.cartas.append(Carta)

    def remove_Carta(self, Carta):
        """Removes a Carta from the baralho or raises exception if it is not there.
        
        Carta: Carta
        """
        self.cartas.remove(Carta)

    def pop_Carta(self, i=-1):
        """Removes and returns a Carta from the baralho.
        i: index of the Carta to pop; by default, pops the last Carta.
        """
        return self.cartas.pop(i)

    def shuffle(self):
        """Shuffles the Cartas in this baralho."""
        random.shuffle(self.cartas)

    def sort(self):
        """Sorts the Cartas in ascending order."""
        self.cartas.sort()

    def move_Cartas(self, hand, num):
        """Moves the given number of Cartas from the baralho into the Hand.
        hand: destination Hand object
        num: integer number of Cartas to move
        """
        for i in range(num):
            hand.add_Carta(self.pop_Carta())


class Mao(Baralho):
    """Represents a hand of playing Cartas."""
    
    def __init__(self, label=''):
        self.cartas = []
        self.label = label

    def cartas_mao(self):
        cartas_mao = []
        for carta_mao in self.cartas: 
            cartas_mao.append(carta_mao)
        return cartas_mao


    def valor_naipes(self):
        naipes = []
        for carta in self.cartas:
            naipes.append(carta.naipe)
        return naipes


    def repete_carta(self):
        cartas_mao = self.cartas_mao()

        lista_cartas = []
        for carta in cartas_mao:
            contador = cartas_mao.count(carta)
            if contador > 1:
                lista_cartas.append(contador)
        return sorted(lista_cartas)  


def analisa_combinacao(mao: object):
    repeticoes = mao.repete_carta()
    naipes = mao.valor_naipes()

    if repeticoes.count(2) == 1:
        print("Você fez um PAR")
    elif repeticoes.count(2) == 2:
        print("Você fez DOIS PARES")
    elif repeticoes.count(3) == 3:
        print("Você fez uma TRINCA")
    elif naipes.count(naipes[0]) == 5:
        print("Você fez um FLUSH")
    else:
        print("Você não fez nenhuma das combinações especiais :(")
   
                
def main():
    baralho = Baralho()
    baralho.shuffle()
    mao = Mao()
    baralho.move_Cartas(mao, 5)
    mao.sort()

    print(mao)
    analisa_combinacao(mao)


if __name__ == '__main__':
    main()
