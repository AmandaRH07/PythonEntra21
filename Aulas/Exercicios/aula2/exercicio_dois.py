# Calcule o valor total dos itens e aplique descontos:

# se o valor for superior a 50, 2% de desconto
# se o valor for superior a 100, 5% de desconto
# se o valor for superior a 200, 10% de desconto

# descubra qual o item mais caro da lista

# ordene os itens da lista por ordem alfabética

dicionario_itens = {"Macarrão": 10.00, "Arroz": 20.00, "Feijão": 12.00, "Suco": 8.00, "Carne": 35.00, "Pão": 4.00, "Açúcar": 15.00}

total = 0
for i,v in dicionario_itens.items():
    total += v

print(f"O valor total da compra foi de: {total}")

if total < 50.00:
    print("Você não atingiu o valor para receber um desconto")
else:
    if total > 50.00 and total < 100.00:
        valorDesconto = "2%" 
        desconto = total - (total * 0.02)
    elif  total > 100.00 and total < 200.00:
        valorDesconto = "5%" 
        desconto = total - (total * 0.05)
    elif total > 200.00:
        valorDesconto = "10%" 
        desconto = total - (total * 0.1)
    print(f"Desconto de: {valorDesconto}. Novo total: {desconto}")

maior = 0
for i,v in dicionario_itens.items():
    if v > maior:
        maior = v
print(f"O maior valor é: {maior}")
#print(max(dicionario_itens, key=dicionario_itens.get))

print(sorted(dicionario_itens))