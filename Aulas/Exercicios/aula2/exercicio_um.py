# Crie uma lista com todas as letras do alfabeto

# Remova as vogais dessa lista e crie uma tupla com elas

# Crie uma coleção com as letras do seu nome (utilizando a lista e a tupla, sem remover itens).
# depois, adicione sua idade e o nome do seu livro favorito

alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
vogais = ["a", "e", "i", "o", "u"]
lista = []
nome = "amanda"
lista_nome = []

for letra in nome:
    for alf in alfabeto:
        if letra == alf:
            lista_nome.append(letra)

for letra in alfabeto:
    for vogal in vogais:
        if letra == vogal:
            lista.append(letra)
            alfabeto.remove(letra)

tupla = tuple(lista)
print(tupla)
print("*" * 30) 

lista_nome.append("18")
lista_nome.append("Por Lugares Incríveis")  
print(lista_nome)  
print("*" * 30)

"""
dicionarioNome = {}
dicionarioNome[0] = lista_nome

for i in dicionarioNome.values():
    print(i)
"""

cont = 0
for j in lista_nome:
    cont +=1
    dictNome = [[cont, j]]
    dicionarioNome = dict(dictNome)
    print(dicionarioNome)