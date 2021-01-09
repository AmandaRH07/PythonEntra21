"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo: 
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

"""
import exercises as cabecalho

cabecalho.cabecalho("salário")

valor_hora = float(input("Insira o valor recebido por hora trabalhada: "))
horas_trabalhadas = int(input("Insira o número de horas trabalhadas no mês: "))

salario = valor_hora * horas_trabalhadas

# inss
inss  = salario * 0.08

# sindicato
sindicato  = salario * 0.05

# imposto de renda
imposto = salario * 0.11

salario_liquido = salario - inss - sindicato - imposto

print(f"""
DADOS: 
\tSalário Bruto: R$ {salario:.2f} 
\tINSS: R$ {inss:.2f} 
\tSindicato: R$ {sindicato:.2f} 
\tSalário Líquido: R$ {salario_liquido:.2f} """)