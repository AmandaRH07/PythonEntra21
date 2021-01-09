"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados. 
"""
import random
import exercises as cabecalho
from collections import Counter

cabecalho.cabecalho("lançamento de dados")

lista_valores = []

for i in range(1, 101):
    lista_valores.append(random.randint(1,6))
    
resultado = Counter(lista_valores)    

for jogada, ocorrencia in resultado.items():
    print(f'o lado do dado {jogada} ocorreu {ocorrencia} vezes')