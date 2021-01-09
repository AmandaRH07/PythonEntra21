#busca por igualdade
x = True
if x == True:
    pass

if x: 
    pass

# acessar elementos de dicionários
d = {'hello' : 'world'}
# if d.has_key('hello'): python2
#     print(d['hello'])

if 'hello' in d:
    print(d['hello'])

# compreensão de listas python
numbers = range(10)
print(*numbers)

pairs = []
for number in numbers:
    if number % 2 == 0:
        pairs.append(number)

print(pairs)

# odds = [number for number in numbers if number % 2 != 0]
odds = filter(lambda n: n % 2 != 0, numbers)
print(*odds)

# desempactotamento
name, extension = "meu_arquivo.jpeg".split(".")
print(f"o arquivo {name} é de extensão {extension}")
