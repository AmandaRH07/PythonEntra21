# o guia do mochileiro python
# explicito é melhor que implicito
def make_dict(*args):
    x, y = args
    return dict(**locals()) 

def make_dict_pro(x, y):
    return {'x': x, 'y': y}

print(*make_dict_pro('x', 'y'))

# esparso é melhor que denso
if (1+1 == 51 + 35 - 37) and "uma coisa complexa" == "palavra"[0]:
    pass
    # do something

condicao_um = (1+1 == 51 + 35 - 37)
condicao_dois = "uma coisa complexa" == "palavra"[0]
if condicao_um and condicao_dois:
    pass
    # do something


# erros nunca devem passar silenciosamente
def find_word(letter):
    words = ['ball', 'heart', 'edge']
    for word in words:
        if letter in words:
            return word
    raise Exception("Palavra não encontrada!")

try:
    find_word("o")
except:
    pass
    # raise

# os argumentos de funções devem ter uso intuitivo
def sendMsg(nome, sobrenome="", *args, **kwargs):
    print(nome)
    print(sobrenome)
    print(args)
    print(kwargs)

sendMsg("Bruno", "Sadoski", "blablablablab", "xD", title="Hello world", msg="You ate the best!")

# se a implementação é dificil de explicar, é uma má ideia!
# kung fu vs python!

# somos todos usuários responsáveis
# encapsulamento

# manter um unico ponto de retorno das funções
def make_choice(param1, param2, *args):
    if param1:
        return "something"
    if param2:
        return "other thing"

    the_thing = "no thing"
    if param1:
      the_thing = "something"
    if param1:
      the_thing = "other thing"
    return the_thing

