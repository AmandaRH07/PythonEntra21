# Crie uma classe chamada Mario; ele terá inicialmente um atributo power que estará vazio, e dois métodos: jump e use_power
# Utilizando Herança, crie ao menos 5 classes que representará os power ups de mario
# Exemplo: classe fire_flower: o metodo use_power retornara uma bola de fogo!!!
# Obs: Cada power up, muda determinadas caracteristicas do personagem, você pode implementa-las também :D

# Super Bonus: Faça um menu que nos permita testar os poderes do Mario :D
# Referencia: https://www.mariowiki.com/List_of_power-ups 

# Hyper Bonus: faça uma classe inimigo; utilizando herença construa classes como goomba, koopa, bowser;
# Ultra Hyper Super Mega Bonus: faça tudo isso iteragir de alguma forma via console =D

class Mario: 
    def __init__(self, power):
        self.power = power
    
    def jump(self):
        return "pulou"

    def use_power(self):
        return "bola de fogo"

class Up_Heart(Mario):
    def use_power(self):
        return "ganhou vida extra"

class Stop_Watch(Mario):
    def use_power(self):
        return "inimigos imobilizados"

class Speed_Flower(Mario):
    def use_power(self):
        return "Tempo acelerado, valor das moedas e dos pontos triplicado"

class Slow_Flower(Mario):
    def use_power(self):
        return "Tempo desacelerado, valor das moedas e dos pontos triplicado"

class P_Wing(Mario):
    def use_power(self):
        return "Fim do nível"

if __name__ == "__main__":

    while True:
        jogar = Mario(None)
        
        valor = input("""
        JOGO MARIO
        1 - Pular
        2-  Use Power
            a- Up Heart
            b- Stop Watch
            c- Speed Flower
            d- Slow Flower
            e- P- Wing
        0- Sair
        Insira a opção desejada: """)

        if valor == "1":
            print(jogar.jump())
        elif valor == "2":
            print(jogar.use_power())
        elif (valor == "a"):
            jogar = Up_Heart(None)
            print(jogar.use_power())
        elif (valor == "b"):
            jogar = Stop_Watch(None)
            print(jogar.use_power())
        elif (valor == "c"):
            jogar = Speed_Flower(None)
            print(jogar.use_power())
        elif (valor == "d"):
            jogar = Slow_Flower(None)
            print(jogar.use_power())
        elif (valor == "e"):
            jogar = P_Wing(None)
            print(jogar.use_power())
        elif valor == "0":
            print("Obrigado por jogar :)")
            break
        else:
            print("Opção inválida")