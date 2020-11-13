# listas 
# ordenada, mutáveis, heterogeneas (qualquer tipo, com duplicados)
lista = ["maçã", "banana", "cereja", "goiaba", "pera"]
print(lista) 

# tuplas 
# ordenada, imutavel, homogenea (um único tipo)
tupla = ("a", "b", "c", "d", "e")
print(tupla) 

# coleções (sets) 
# não ordenada, imutavel, heterogeneas (sem duplicados)
colecao = {3, True, "cachorro", 0.12312, "e", "e"}
print(colecao) 

# adicionar 
lista.append("laranja")
print(*lista) 

#adicionar posicao especifica
lista.insert(1, "kiwi")
print(lista.index("kiwi")) 

# muda o conteúdo
lista[0] = "manga"
print(lista)

# remover e atribuir a variavel
fruta = lista.pop(2)
print("Removido: {}".format(fruta))

# contar itens
print(lista.count("kiwi"))

# remover
lista.remove("kiwi")
print(lista)

# ordenar
lista.sort()

# percorrer lista
for item in lista:
    print(item)

# item de uma lista
print(lista[-1])
# de x até y (sem y)
print(lista[0:2])

# do começo até y 
print(lista[:2])

# de x até o final
print(lista[1:])

