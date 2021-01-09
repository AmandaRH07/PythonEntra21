"""
Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
     8  3  4 
     1  5  9
     6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3. 
"""

import random 
import exercises as cabecalho
from itertools import permutations

cabecalho.cabecalho("quadrado mágico")

quadrado = list(permutations([1,2,3,4,5,6,7,8,9]))

def gera_valores():
     final_horizontal = False
     final_vertical = False
     final_diagonal = False
     cont = 0

     for valores in quadrado:
          soma_horizontal1 = valores[0] + valores[1] + valores[2]
          soma_horizontal2 = valores[3] + valores[4] + valores[5]
          soma_horizontal3 = valores[6] + valores[7] + valores[8]

          if (soma_horizontal1 == 15) and (soma_horizontal2 == 15) and (soma_horizontal3 == 15):
               final_horizontal = True

          soma_vertical1 = valores[0] + valores[3] + valores[6]
          soma_vertical2 = valores[1] + valores[4] + valores[7]
          soma_vertical3 = valores[2] + valores[5] + valores[8]

          if (soma_vertical1 == 15) and (soma_vertical2 == 15) and (soma_vertical3 == 15):
               final_vertical = True

          soma_diagonal1 = valores[0] + valores[4] + valores[8]
          soma_diagonal2 = valores[2] + valores[4] + valores[6]
     
          if (soma_diagonal1 == 15) and (soma_diagonal2 == 15):
               final_diagonal = True

          if final_horizontal == True and final_vertical == True and final_diagonal == True: 
               cont += 1 
               print(f""" Quadrado Nº {cont}
     {valores[0]} {valores[1]} {valores[2]}
     {valores[3]} {valores[4]} {valores[5]}
     {valores[6]} {valores[7]} {valores[8]}
               """)
               
          final_horizontal = False
          final_vertical = False
          final_diagonal = False
                  

def  main():
     tamanho = 1
     while tamanho > 0:
          gera_valores()
          tamanho-=1


if __name__ == "__main__":
    main()