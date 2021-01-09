"""
Faça um programa que gera uma lista dos números primos existentes entre 1 e 
um número inteiro informado pelo usuário. 
"""
import exercises as cabecalho

cabecalho.cabecalho("números primos")

valor = int(input("Insira o número: "))

primos = []

for dividendo in range(1, valor+1):
    cont = 0
    for divisor in range(1, valor+1):
        if dividendo % divisor == 0:
            cont += 1

    if cont == 2:
        primos.append(dividendo)

for primo in primos:
    print(primo)
