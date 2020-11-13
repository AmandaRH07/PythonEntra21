# basics
print('Hello, World') 

# operadores 
print(1 + 1 * 1 / 1 ** 1) 

# tipos
print(type(12)) 
print(type("Oiiiii"))
print(type(48.65)) 
print(type(False))

#vars
eu_sou_uma_variavel = "variavel" 
print(eu_sou_uma_variavel)

# nome
print("Digite seu nome: ")
nome = input()
print("seu nome é " + nome)

# funcoes
def eu_sou_uma_funcao(variavel:str="palavra"):
    print("a palavra é: " + variavel)
    print("a palavra é: %s" % variavel)

eu_sou_uma_funcao("abacate!")


def eu_sou_uma_funcao_com_retorno():
    return "retorno", 125

x, y = eu_sou_uma_funcao_com_retorno()
print(x)

# condicional
segunda_feira=False
if segunda_feira:
    print("É verdade!")
else:
    print("É mentira!")

# repetições
for letra in ['a', 'b', 'c']:
    print(letra)

contador = 0
while contador < 10:
    print(contador)
    contador += 1

#list
print(type(["a", "b"]))

#tuple
print(type(("a", "b")))

#sets
print(type({"a", "b"}))

#sets
print(type({"a":1, "b":2}))
